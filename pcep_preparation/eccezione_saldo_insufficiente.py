class ContoBancario:
    def __init__(self, saldo):
        self.saldo = saldo

    def preleva(self, importo):
        try:
            if importo > self.saldo:
                raise ValueError("Saldo insufficiente")
            self.saldo -= importo
            print(f"Prelevato {importo} euro. Saldo attuale: {self.saldo} euro")
        except ValueError as e:
            print(f"Errore: {e}")

    def deposita(self, importo):
        try:
            if importo <= 0:
                raise ValueError("Importo non valido")
            self.saldo += importo
            print(f"Depositato {importo} euro. Saldo attuale: {self.saldo} euro")
        except ValueError as e:
            print(f"Errore: {e}")

    def mostra_saldo(self):
        print(f"Saldo attuale: {self.saldo} euro")

def main():
    conto = ContoBancario(1000)
    while True:
        print("\n1. Preleva")
        print("2. Deposita")
        print("3. Mostra Saldo")
        print("4. Esci")
        scelta = input("Scegli un'opzione: ")
        if scelta == "1":
            try:
                importo = float(input("Inserisci l'importo da prelevare: "))
                conto.preleva(importo)
            except ValueError:
                print("Errore: Inserisci un importo valido.")
        elif scelta == "2":
            try:
                importo = float(input("Inserisci l'importo da depositare: "))
                conto.deposita(importo)
            except ValueError:
                print("Errore: Inserisci un importo valido.")
        elif scelta == "3":
            conto.mostra_saldo()
        elif scelta == "4":
            break
        else:
            print("Opzione non valida")

if __name__ == "__main__":
    main()
