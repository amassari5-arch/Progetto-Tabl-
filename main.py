from utenti import SistemaTablo
from gestione_ordini import GestoreOrdini


def menu_principale():

    sistema = SistemaTablo()


    utente_loggato = None
    tavolo_attivo = None

    while True:
        print("\n" + "═" * 40)
        print("           BENVENUTO SU TABLÒ")
        print("═" * 40)

        if utente_loggato:
            print(f" Utente: {utente_loggato._nome} {utente_loggato._cognome}")

        print("1. Registrati (Nuovo Utente)")
        print("2. Accedi (Utente Esistente)")
        print("3. Prenota un Tavolo e Ordina")
        print("4. Gestisci / Cancella Prenotazione")
        print("5. Lascia una Recensione")
        print("6. Leggi tutte le Recensioni")
        print("7. Visualizza Classifica Locali (Media Voti)")
        print("8. Visualizza lo storico dei tuoi ordini")
        print("9. Esci e Salva")
        print("═" * 40)

        scelta = input("\nSeleziona un'opzione: ")

        if scelta == "1":
            utente_loggato = sistema.registra_nuovo_utente()

        elif scelta == "2":
            utente_loggato = sistema.accedi_utente()

        elif scelta == "3":
            if utente_loggato:

                from prenotazioni import GestorePrenotazione
                gestore = GestorePrenotazione(sistema.catalogo_locali)

                risultato_prenotazione = gestore.avvia_procedura()

                if risultato_prenotazione is not None:
                    utente_loggato.aggiungi_prenotazione(risultato_prenotazione)
                    tavolo_attivo = risultato_prenotazione
                    sistema.salva_dati()
                    print("\n Prenotazione effettuata con successo.")
                else:
                    print("\n locale pieno.")
            else:
                print("\n ! ACCESSO NEGATO: Devi prima registrarti o accedere!")

        elif scelta == "4":

            if tavolo_attivo:
                gestore = GestoreOrdini(tavolo_attivo)
                gestore.mostra_e_modifica()
            else:
                print("\n ! Non hai ancora effettuato una prenotazione.")

        elif scelta == "5":
            if utente_loggato:
                sistema.lascia_recensione(utente_loggato)
                sistema.salva_dati()
            else:
                print("\n ! ACCESSO NEGATO: Solo gli utenti loggati possono recensire.")

        elif scelta == "6":
            sistema.mostra_recensioni()

        elif scelta == "7":
            try:
                sistema.mostra_media_locali()
            except AttributeError:
                print("\n ! Errore")

        elif scelta == "8":
            if utente_loggato:
                sistema.mostra_storico_cliente(utente_loggato)
            else:
                print("\n ! ACCESSO NEGATO: Devi prima accedere per vedere il tuo storico.")

        elif scelta == "9":
            sistema.salva_dati()
            print("\n I dati sono stati salvati correttamente. Grazie per aver scelto Tablò!")
            break

        else:
            print("\n ! Scelta non valida. Inserisci un numero da 1 a 7.")


if __name__ == "__main__":
    menu_principale()