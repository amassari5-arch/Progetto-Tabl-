from tavolo import Tavolo, PiattoBase, Tartufo, Patatine, Bruschetta


# Gestisce scelta locale e ordinazione
class GestorePrenotazione:
    def __init__(self, catalogo_locali):
        self.catalogo_locali = catalogo_locali

    def avvia_procedura(self):
        print("\n--- SCEGLI LA TIPOLOGIA ---")
        tipologie = list(self.catalogo_locali.keys())
        for i, tipo in enumerate(tipologie, 1):
            print(f"{i}. {tipo}")

        scelta_t = int(input("\nInserisci il numero: ")) - 1
        tipo_scelto = tipologie[scelta_t]

        print(f"\n--- SCEGLI IL LOCALE ({tipo_scelto}) ---")
        lista = self.catalogo_locali[tipo_scelto]
        for i, loc in enumerate(lista, 1):
            print(f"{i}. {loc.get_nome()}")

        scelta_l = int(input("\nInserisci il numero: ")) - 1
        locale_final = lista[scelta_l]

        locale_final.mostra_dettagli()
        locale_final.gestore_menu.carica_da_file()

        # Prenotazione
        print("\n" + "=" * 30)
        print("   DATI PRENOTAZIONE")
        print("=" * 30)

        giorni_validi = ["lunedì", "martedì", "mercoledì", "giovedì", "venerdì", "sabato", "domenica"]

        while True:
            giorno = input("Per quale giorno vuoi prenotare? (es. Sabato): ").strip().lower()
            if giorno in giorni_validi:
                giorno = giorno.capitalize()
                break
            else:
                print(f" ! Errore: '{giorno}' non è un giorno valido. Riprova.")

        ora = input("A che ora? (es. 20:30): ")

        try:
            persone = int(input("In quante persone sarete?: "))
        except ValueError:
            print("\n ! ERRORE: Inserisci un numero valido per le persone.")
            return None

        if not locale_final.posti_liberi(persone):
            print("\n" + "!" * 40)
            print("      LOCALE AL COMPLETO")
            print("!" * 40)
            print(f"Spiacenti, non abbiamo spazio per {persone} persone.")
            print(f"Posti attualmente liberi: {locale_final.posti_totali - locale_final.posti_occupati}")
            print("Ti invitiamo a scegliere un altro locale.")
            print("!" * 40)
            return None

        locale_final.prenota_posti(persone)
        nuova_prenotazione = Tavolo(persone, giorno, ora)
        print(f"\n OK Tavolo prenotato! Posti rimanenti in sala: {locale_final.posti_totali - locale_final.posti_occupati}")

        print("\n--- MENU DISPONIBILE ---")
        if not locale_final.gestore_menu.piatti:
            print("Menu al momento non disponibile.")
        for piatto, prezzo in locale_final.gestore_menu.piatti.items():
            print(f"- {piatto}: €{prezzo}")

        while True:
            ordine = input("\nInserisci il nome del piatto (o 'fine' per terminare): ")
            if ordine.lower() == "fine":
                break

            if ordine in locale_final.gestore_menu.piatti:
                prezzo_piatto = locale_final.gestore_menu.piatti[ordine]
                piatto_ord = PiattoBase(ordine, prezzo_piatto)

                print(f"Desideri un extra per '{ordine}'?")
                print("1. Tartufo (+€15.00)")
                print("2. Patatine (+€3.50)")
                print("3. Bruschetta (+€5.00)")
                print("0. Nessun extra")

                scelta_ex = input("Scelta: ")

                if scelta_ex == "1":
                    piatto_ord = Tartufo(piatto_ord)
                elif scelta_ex == "2":
                    piatto_ord = Patatine(piatto_ord)
                elif scelta_ex == "3":
                    piatto_ord = Bruschetta(piatto_ord)

                nuova_prenotazione.aggiungi_piatto(piatto_ord.get_nome(), piatto_ord.get_prezzo())
                print(f"--> {piatto_ord.get_nome()} aggiunto correttamente!")
            else:
                print("! ERRORE: Piatto non trovato nel menu.")

        nuova_prenotazione.genera_riepilogo()
        return nuova_prenotazione

