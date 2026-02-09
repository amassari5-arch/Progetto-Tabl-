# Gestione della revisione e modifica dell'ordine
class GestoreOrdini:
    def __init__(self, tavolo):
        self.tavolo = tavolo

    def mostra_e_modifica(self):
        if not self.tavolo.ordine_piatti:
            print("\n ! L'ordine attuale è vuoto.")
            return

        print("\n" + "=" * 40)
        print("       RIEPILOGO PRENOTAZIONE")
        print("=" * 40)

        # Mostriamo le info del tavolo (posti, data, ora)
        print(self.tavolo.get_info_tavolo())
        print("-" * 40)

        print("PIATTI PRENOTATI:")
        for i, (piatto, prezzo) in enumerate(self.tavolo.ordine_piatti, 1):
            print(f"{i}. {piatto} (€{prezzo})")

        print(f"\nTOTALE ATTUALE: €{self.tavolo.calcola_totale():.2f}")
        print("=" * 40)

        print("\n Cosa desideri fare?")
        print("1. Cancella intero ordine e ricomincia")
        print("2. Torna al menu principale")

        scelta = input("Scelta: ")

        if scelta == "1":
            self.tavolo.ordine_piatti.clear()
            print("\n OK Ordine e prenotazione svuotati con successo.")
        else:
            print("\n OK Prenotazione confermata.")