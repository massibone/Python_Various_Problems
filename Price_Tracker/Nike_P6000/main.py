import os
import re
import time
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

# ---------------- CONFIG ----------------

PRODUCT_URLS = [
    url.strip()
    for url in os.getenv(
        "PRODUCT_URLS",
        "https://www.nike.com/it/t/scarpa-p-6000-CVTvTry5",
    ).split(",")
]

PRICE_THRESHOLD = float(os.getenv("PRICE_THRESHOLD", "90"))
CHECK_INTERVAL_HOURS = int(os.getenv("CHECK_INTERVAL_HOURS", "6"))

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")

SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")
EMAIL_TO = os.getenv("EMAIL_TO", "")

HISTORY_FILE = "storico_prezzi_p6000.json"
ALERT_LOG = "alert_prezzi.log"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0 Safari/537.36"
    )
}

# ---------------- UTILS ----------------


def load_history():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save_history(history):
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)


def log_alert(msg: str):
    print(msg)
    with open(ALERT_LOG, "a", encoding="utf-8") as f:
        f.write(msg + "\n")


# ---------------- NOTIFICHE ----------------


def send_telegram_message(text: str):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "HTML",
    }
    try:
        resp = requests.post(url, json=payload, timeout=10)
        resp.raise_for_status()
    except Exception as e:
        print(f"Errore invio Telegram: {e}")


def send_email_alert(subject: str, body: str):
    if not SMTP_USER or not SMTP_PASSWORD or not EMAIL_TO:
        return

    msg = MIMEMultipart()
    msg["From"] = SMTP_USER
    msg["To"] = EMAIL_TO
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain", "utf-8"))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=10) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(msg)
    except Exception as e:
        print(f"Errore invio email: {e}")


def notify_alert(url: str, price: float, prev_price: float | None):
    now = datetime.now().isoformat()
    drop_info = ""
    if prev_price is not None:
        drop_info = f" (prima: {prev_price:.2f} €)"

    text = (
        f"[{now}] PREZZO SCESO!\n"
        f"URL: {url}\n"
        f"Prezzo: {price:.2f} € (soglia: {PRICE_THRESHOLD:.2f} €){drop_info}\n"
    )

    log_alert(text)

    # Telegram
    telegram_text = (
        f"🔔 <b>Prezzo sceso Nike P-6000</b>\n"
        f"Prezzo: <b>{price:.2f} €</b>\n"
        f"Soglia: {PRICE_THRESHOLD:.2f} €\n"
        f"URL: <a href='{url}'>apri prodotto</a>"
    )
    send_telegram_message(telegram_text)

    # Email
    subject = f"Prezzo sceso: Nike P-6000 a {price:.2f} €"
    body = (
        f"Ciao,\n\n"
        f"Il prezzo di una Nike P-6000 che stai monitorando è sceso.\n\n"
        f"Prezzo attuale: {price:.2f} €\n"
        f"Soglia impostata: {PRICE_THRESHOLD:.2f} €\n"
        f"URL: {url}\n\n"
        f"Buon acquisto!\n"
    )
    send_email_alert(subject, body)


# ---------------- ESTRAZIONE PREZZO ----------------


def extract_price_from_nike(html: str) -> float | None:
    soup = BeautifulSoup(html, "html.parser")

    # Prova selettore tipico di Nike
    price_el = soup.select_one('[data-test="product-price"]')
    if not price_el:
        # fallback su classi contenenti "price"
        for el in soup.select(".product-price, [class*='price']"):
            text = el.get_text(strip=True)
            if "€" in text:
                m = re.search(r"([\d.,]+)\s*€", text.replace(".", "").replace(",", "."))
                if m:
                    return float(m.group(1).replace(",", "."))
        return None

    text = price_el.get_text(strip=True)
    m = re.search(r"([\d.,]+)\s*€", text.replace(".", "").replace(",", "."))
    if m:
        return float(m.group(1).replace(",", "."))
    return None


def extract_price_from_generic(html: str) -> float | None:
    soup = BeautifulSoup(html, "html.parser")

    for el in soup.select(
        ".price, .product-price, [class*='price'], [data-price]"
    ):
        text = el.get_text(strip=True)
        if "€" in text:
            m = re.search(r"([\d.,]+)\s*€", text.replace(".", "").replace(",", "."))
            if m:
                return float(m.group(1).replace(",", "."))

        price_attr = el.get("data-price")
        if price_attr:
            try:
                return float(price_attr.replace(",", "."))
            except ValueError:
                continue

    # fallback: cerca nel testo della pagina
    text = soup.get_text()
    m = re.search(r"([\d.,]+)\s*€", text.replace(".", "").replace(",", "."))
    if m:
        return float(m.group(1).replace(",", "."))
    return None


def get_price(url: str) -> float | None:
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        resp.raise_for_status()
    except Exception as e:
        print(f"Errore nel download di {url}: {e}")
        return None

    html = resp.text

    if "nike.com" in url:
        price = extract_price_from_nike(html)
    else:
        price = extract_price_from_generic(html)

    return price


# ---------------- MAIN LOOP ----------------


def main():
    history = load_history()

    while True:
        print(f"\n[{datetime.now().isoformat()}] Controllo prezzi...")
        for url in PRODUCT_URLS:
            price = get_price(url)

            prev = history.get(url, {}).get("last_price")

            if price is None:
                print(f"{url} -> prezzo non rilevato")
                continue

            print(f"{url} -> {price:.2f} €")

            history[url] = {
                "last_price": price,
                "last_check": datetime.now().isoformat(),
            }

            if price <= PRICE_THRESHOLD:
                notify_alert(url, price, prev)

        save_history(history)
        print(f"Attesa {CHECK_INTERVAL_HOURS} ore...")
        time.sleep(CHECK_INTERVAL_HOURS * 3600)


if __name__ == "__main__":
    main()
