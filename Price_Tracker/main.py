import os
import re
import json
from datetime import datetime

import requests
from bs4 import BeautifulSoup

# CONFIG (puoi leggere da env o hardcoded)
PRODUCT_URLS = [
    url.strip()
    for url in os.getenv(
        "PRODUCT_URLS",
        "https://www.nike.com/it/t/scarpa-p-6000-CVTvTry5",
    ).split(",")
]

PRICE_THRESHOLD = float(os.getenv("PRICE_THRESHOLD", "90"))

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")

HISTORY_FILE = "storico_prezzi_p6000.json"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0 Safari/537.36"
    )
}


def load_history():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save_history(history):
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)


def send_telegram_message(text: str):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "HTML",
    }
    resp = requests.post(url, json=payload, timeout=10)
    resp.raise_for_status()


def extract_price_from_nike(html: str) -> float | None:
    soup = BeautifulSoup(html, "html.parser")
    price_el = soup.select_one('[data-test="product-price"]')
    if not price_el:
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
    for el in soup.select(".price, .product-price, [class*='price'], [data-price]"):
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

    text = soup.get_text()
    m = re.search(r"([\d.,]+)\s*€", text.replace(".", "").replace(",", "."))
    if m:
        return float(m.group(1).replace(",", "."))
    return None


def get_price(url: str) -> float | None:
    resp = requests.get(url, headers=HEADERS, timeout=10)
    resp.raise_for_status()
    html = resp.text

    if "nike.com" in url:
        return extract_price_from_nike(html)
    return extract_price_from_generic(html)


def main():
    history = load_history()

    for url in PRODUCT_URLS:
        try:
            price = get_price(url)
        except Exception as e:
            print(f"Errore su {url}: {e}")
            continue

        if price is None:
            print(f"{url} -> prezzo non rilevato")
            continue

        print(f"{url} -> {price:.2f} €")

        prev = history.get(url, {}).get("last_price")
        history[url] = {
            "last_price": price,
            "last_check": datetime.now().isoformat(),
        }

        if price <= PRICE_THRESHOLD:
            drop_info = ""
            if prev is not None:
                drop_info = f" (prima: {prev:.2f} €)"

            telegram_text = (
                f"🔔 <b>Prezzo sceso Nike P-6000</b>\n"
                f"Prezzo: <b>{price:.2f} €</b>\n"
                f"Soglia: {PRICE_THRESHOLD:.2f} €{drop_info}\n"
                f"URL: <a href='{url}'>apri prodotto</a>"
            )
            send_telegram_message(telegram_text)

    save_history(history)


if __name__ == "__main__":
    main()
