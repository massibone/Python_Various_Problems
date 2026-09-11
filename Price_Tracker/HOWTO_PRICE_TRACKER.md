# How-To: Price Tracker con GitHub Actions + Telegram

Questo documento spiega come:

- configurare il price tracker,
- aggiungere nuovi prodotti,
- verificare che GitHub Actions giri,
- controllare che Telegram riceva gli alert,
- e risolvere i problemi più comuni.

---

## 1) Struttura della repo

La repo deve avere almeno:

```text
Python_Various_Problems/
├─ .github/
│  └─ workflows/
│     └─ price_tracker.yml
├─ Price_Tracker/
│  ├─ config.yml
│  ├─ main.py
│  └─ requirements.txt
└─ ...
```

- `.github/workflows/price_tracker.yml`: workflow GitHub Actions.
- `Price_Tracker/config.yml`: lista dei prodotti da monitorare.
- `Price_Tracker/main.py`: script che controlla i prezzi e invia i messaggi.
- `Price_Tracker/requirements.txt`: dipendenze Python.

---

## 2) Configurazione iniziale

### 2.1) Creare il bot Telegram

1. Apri Telegram e cerca **@BotFather**.
2. Invia `/newbot` e scegli:
   - un nome (es. "Price Tracker Bot"),
   - uno username (deve finire con `bot`, es. `PriceTrackerBot`).
3. BotFather ti restituisce un **token** tipo:
   ```text
   123456:ABCdefGHIjklMNOpqrsTUVwxyz
   ```
4. Cerca il tuo bot in Telegram e avvialo con `/start`.

### 2.2) Ottenere il tuo CHAT_ID

1. Cerca **@RawDataBot** su Telegram.
2. Avvialo con `/start`.
3. Ti risponde con un messaggio che contiene il tuo **user ID** (es. `123456789`).
4. Quel numero è il tuo `CHAT_ID`.

### 2.3) Impostare i secrets su GitHub

1. Vai su GitHub, nella tua repo.
2. Clicca su **Settings → Secrets and variables → Actions → New repository secret**.
3. Aggiungi:

- `TELEGRAM_BOT_TOKEN` → il token da BotFather
- `TELEGRAM_CHAT_ID` → il tuo ID numerico da @RawDataBot

---

## 3) Configurare i prodotti da monitorare

Modifica `Price_Tracker/config.yml`:

```yaml
products:
  - name: "Nike P-6000 bianche (Nike)"
    url: "https://www.nike.com/it/t/scarpa-nike-p-6000-V04wEyXX/CD6404-107"
    threshold: 130
    enabled: true

  - name: "Nike P-6000 bianche (Altro retailer)"
    url: "https://www.example.com/prodotto"
    threshold: 85
    enabled: true
```

Per ogni prodotto definisci:

- `name`: nome descrittivo (appare nei messaggi Telegram),
- `url`: URL della pagina prodotto,
- `threshold`: prezzo massimo per cui vuoi ricevere l'avviso,
- `enabled`: `true`/`false` per attivare/disattivare.

---

## 4) Verificare che GitHub Actions giri

### 4.1) Controllo manuale (on demand)

1. Vai su GitHub, nella repo.
2. Clicca sulla scheda **Actions** in alto.
3. Nella colonna di sinistra, clicca su **Price tracker**.
4. Clicca su **Run workflow** (a destra).
5. Aspetta 2–3 minuti.

### 4.2) Leggere il log

1. Clicca sul run appena finito (il primo in lista).
2. Clicca su **check-prices**.
3. Espandi **Run price tracker**.
4. Dovresti vedere righe tipo:

```text
Nike P-6000 bianche (Nike) -> 119.99 €
Nike P-6000 bianche (Altro retailer) -> prezzo non rilevato
```

Se vedi errori (es. 403, 404), controlla:

- che l'URL sia corretto e si apra nel browser,
- che il sito non blocchi le richieste automatiche.

---

## 5) Verificare Telegram

1. Apri Telegram sul telefono.
2. Cerca il tuo bot (es. `@PriceTrackerBot`).
3. Apri la chat e assicurati di avergli mandato almeno una volta `/start`.

Se un prodotto ha prezzo ≤ soglia, riceverai un messaggio tipo:

> 🔔 **Prezzo sceso: Nike P-6000 bianche (Nike)**  
> Prezzo: **119,99 €**  
> Soglia: 130,00 €  
> URL: apri prodotto

Se non arriva nulla:

- controlla che il prezzo sia effettivamente ≤ soglia,
- verifica che `TELEGRAM_BOT_TOKEN` e `TELEGRAM_CHAT_ID` siano corretti nei secrets.

---

## 6) Aggiungere un nuovo prodotto in futuro

1. Apri `Price_Tracker/config.yml`.
2. Aggiungi un nuovo blocco:

```yaml
  - name: "Adidas XYZ"
    url: "https://www.adidas.it/..."
    threshold: 70
    enabled: true
```

3. Fai commit.
4. Al prossimo giro (o lanciando manualmente il workflow), il nuovo prodotto viene controllato automaticamente.

---

## 7) Modificare la frequenza dei controlli

Apri `.github/workflows/price_tracker.yml` e modifica:

```yaml
on:
  schedule:
    - cron: "0 */6 * * *"
```

Esempi:

- ogni 3 ore: `0 */3 * * *`
- ogni 12 ore: `0 */12 * * *`
- una volta al giorno alle 09:00 UTC: `0 9 * * *`

Fai commit e il nuovo schedule si applica dal giro successivo.

---

## 8) Risoluzione problemi comuni

### 8.1) Errore 404 su un URL

Significa che la pagina non esiste più o l'URL è sbagliato.

- Apri l'URL nel browser,
- se dà 404, cerca la pagina prodotto corretta e aggiorna `config.yml`.

### 8.2) Errore 403 su un URL

Il sito blocca le richieste automatiche.

- Prova con un altro retailer,
- o modifica `main.py` per aggiungere più header (ma non è garantito).

### 8.3) Telegram non riceve messaggi

Controlla:

- che il bot sia avviato con `/start`,
- che `TELEGRAM_BOT_TOKEN` e `TELEGRAM_CHAT_ID` siano corretti,
- che non ci siano spazi o a capo nel token (altrimenti l'URL diventa invalido).

### 8.4) Il workflow usa un `config.yml` vecchio

Assicurati che:

- `main.py` legga `config.yml` dalla stessa cartella (`Price_Tracker/config.yml`),
- il workflow punti a `working-directory: Price_Tracker`,
- i run che guardi siano successivi all'ultimo commit su `config.yml`.

---

## 9) Riferimenti utili

- Repo: https://github.com/massibone/Python_Various_Problems
- Workflow: `.github/workflows/price_tracker.yml`
- Config: `Price_Tracker/config.yml`
- Script: `Price_Tracker/main.py`