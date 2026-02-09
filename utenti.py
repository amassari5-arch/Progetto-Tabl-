from abc import ABC, abstractmethod
import re
import pickle
import os
from locali import Pizzeria, Ristorante, Trattoria
from menu_pizzeria import MenuPizzeria
from menu_ristorante import MenuRistorante
from menu_trattoria import MenuTrattoria
from prenotazioni import GestorePrenotazione
from recensione import Recensione

# Classe base per le persone (Classe Astratta)
class Persona(ABC):
    def __init__(self, nome, cognome, email, password):
        self._nome = nome
        self._cognome = cognome
        self._email = email
        self._password = password

    @abstractmethod
    def get_info_sintetica(self):
        pass

# Classe per il cliente che eredita da Persona
class Cliente(Persona):
    def __init__(self, nome, cognome, email, password):
        super().__init__(nome, cognome, email, password)
        self.lista_prenotazioni = []

    def get_info_sintetica(self):
        return f"Cliente: {self._nome} {self._cognome} - Contatto: {self._email}"

    def aggiungi_prenotazione(self, tavolo):
        self.lista_prenotazioni.append(tavolo)

# cervello programma
class SistemaTablo:
    def __init__(self):
        self.database_utenti = {}
        self.storico_recensioni = []
        self.percorso_db = os.path.join("..", "data", "utenti.bin")

        # Catalogo con i locali
        self.catalogo_locali = {
            "Pizzeria": [
                Pizzeria("Napoli Mix", "Via Toledo 1", "Pizza croccante.", MenuPizzeria("pizze.txt")),
                Pizzeria("Vesuvio", "Via Roma 5", "Forno a legna.", MenuPizzeria("pizze.txt")),
                Pizzeria("Gourmet 2.0", "Corso Italia 10", "Ingredienti bio.", MenuPizzeria("pizze.txt")),
                # Nuovi inserimenti
                Pizzeria("L'Antica Ruota", "Via dei Tribunali 3", "Pizza a portafoglio.",
                         MenuPizzeria("pizze.txt")),
                Pizzeria("Farinati", "Piazza Garibaldi 12", "Impasti a lunga lievitazione.",
                         MenuPizzeria("pizze.txt")),
                Pizzeria("Zio Sam", "Via degli Americani 8", "Pizza formato gigante.", MenuPizzeria("pizze.txt"))
            ],
            "Ristorante": [
                Ristorante("Il Lusso", "Piazza Duomo", "Ambiente elegante.", MenuRistorante("piatti_ristorante.txt")),
                Ristorante("Sapore di Mare", "Lungomare 4", "Pesce fresco.", MenuRistorante("piatti_ristorante.txt")),
                Ristorante("La Brace", "Via Monti 2", "Carne alla griglia.", MenuRistorante("piatti_ristorante.txt")),
                # Nuovi inserimenti
                Ristorante("Cracco's Style", "Galleria Vittorio Emanuele", "Cucina stellata.",
                           MenuRistorante("piatti_ristorante.txt")),
                Ristorante("Il Giardino Pensile", "Via Belvedere 45", "Cena con vista città.",
                           MenuRistorante("piatti_ristorante.txt")),
                Ristorante("Fusion Hub", "Via Paolo Sarpi 9", "Incontro tra Oriente e Occidente.",
                           MenuRistorante("piatti_ristorante.txt"))
            ],
            "Trattoria": [
                Trattoria("Da Nonna Rosa", "Vicolo Stretto", "Piatti fatti a mano.",
                          MenuTrattoria("piatti_trattoria.txt")),
                Trattoria("Il Casale", "Strada Provinciale", "Cucina rustica.", MenuTrattoria("piatti_trattoria.txt")),
                Trattoria("Sapori Antichi", "Via Vecchia 8", "Ricette della terra.",
                          MenuTrattoria("piatti_trattoria.txt")),
                # Nuovi inserimenti
                Trattoria("L'Oste Briaco", "Piazza del Mercato 4", "Vino della casa e salumi.",
                          MenuTrattoria("piatti_trattoria.txt")),
                Trattoria("La Vecchia Roma", "Via dei Fori 11", "Carbonara e Amatriciana DOC.",
                          MenuTrattoria("piatti_trattoria.txt")),
                Trattoria("Podere Toscano", "Via delle Vigne 1", "Specialità del contadino.",
                          MenuTrattoria("piatti_trattoria.txt"))
            ]
        }
        self.carica_dati()

    # Gestione recensioni
    def lascia_recensione(self, cliente):
        print("\n" + "═" * 40)
        print("       LASCIA UNA RECENSIONE")
        print("═" * 40)


        tutti_i_locali = []
        for categoria in self.catalogo_locali.values():
            for locale in categoria:
                tutti_i_locali.append(locale)

        print("Seleziona il locale da recensire:")
        for i, locale in enumerate(tutti_i_locali, 1):
            print(f"{i}. {locale.get_nome()} ({locale.__class__.__name__})")

        try:
            scelta = int(input("\nInserisci il numero del locale: ")) - 1
            if 0 <= scelta < len(tutti_i_locali):
                locale_scelto = tutti_i_locali[scelta]
                nome_locale = locale_scelto.get_nome()

                voto = int(input("Quante stelle dai (1-5)? "))
                commento = input("Scrivi un breve commento: ")

                nuova_rec = Recensione(cliente, nome_locale, voto, commento)
                self.storico_recensioni.append(nuova_rec)

                # Salvataggio tramite Memento Pattern
                self.salva_dati()
                print(f"\n OK Grazie! Recensione per '{nome_locale}' pubblicata.")
            else:
                print("\n ! Scelta non valida.")
        except ValueError:
            print("\n ! Errore: Inserisci un numero valido.")

    def mostra_recensioni(self):
        print("\n" + "=" * 30)
        print("  RECENSIONI DEI CLIENTI")
        print("=" * 30)
        if not self.storico_recensioni:
            print("Nessuna recensione presente.")
        else:
            for rec in self.storico_recensioni:
                print(rec)

    # Controllo password
    def verifica_password(self, password):
        if len(password) < 8:
            return False
        pattern_speciale = r"[\!\@\#\$\%\^\&\*\(\)\-\_\=\+\?\@\#\*]"
        return bool(re.search(pattern_speciale, password))

    def salva_dati(self):
        try:
            with open(self.percorso_db, "wb") as f:
                # Salviamo un dizionario che contiene sia utenti che recensioni
                dati = {
                    "utenti": self.database_utenti,
                    "recensioni": self.storico_recensioni
                }
                pickle.dump(dati, f)
        except Exception as e:
            print(f"Errore: {e}")

    def carica_dati(self):
        if os.path.exists(self.percorso_db):
            try:
                with open(self.percorso_db, "rb") as f:
                    dati = pickle.load(f)
                    if isinstance(dati, dict):
                        self.database_utenti = dati.get("utenti", {})
                        self.storico_recensioni = dati.get("recensioni", [])
                    else:
                        self.database_utenti = dati
            except Exception:
                self.database_utenti = {}

    # Gestione utenti
    def registra_nuovo_utente(self):
        print("\n" + "=" * 30)
        print("   REGISTRAZIONE TABLÒ")
        print("=" * 30)
        nome = input("Inserisci il tuo nome: ")
        cognome = input("Inserisci il tuo cognome: ")
        email = input("Inserisci il tuo email: ")

        if email in self.database_utenti:
            print("\n ERRORE: Email già registrata.")
            return None

        while True:
            password = input("Scegli una password (min 8 car. + speciale): ")
            if self.verifica_password(password):
                break
            print("Password non valida. Riprova.")

        nuovo_cliente = Cliente(nome, cognome, email, password)
        self.database_utenti[email] = nuovo_cliente
        self.salva_dati()
        return nuovo_cliente

    def accedi_utente(self):
        email = input("Email: ")
        if email in self.database_utenti:
            utente = self.database_utenti[email]
            password = input("Password: ")
            if utente._password == password:
                print(f"Bentornato {utente._nome}")
                return utente
        print("Credenziali errate.")
        return None

    def seleziona_locale(self):
        gestore = GestorePrenotazione(self.catalogo_locali)
        return gestore.avvia_procedura()


    def mostra_storico_cliente(self, cliente):
        print("\n" + "═" * 45)
        print(f"   STORICO PRENOTAZIONI DI: {cliente._nome.upper()}")
        print("═" * 45)

        if not cliente.lista_prenotazioni:
            print("Non hai ancora effettuato nessuna prenotazione.")
        else:
            for i, t in enumerate(cliente.lista_prenotazioni, 1):
                print(f"{i}. DATA: {t.data} | ORA: {t.ora}")
                print(f"   DETTAGLI: {t.numero_persone} persone")
                print(f"   TOTALE ORDINE: €{t.calcola_totale():.2f}")
                print("-" * 45)
        print("═" * 45)

    def get_media_voti(self, nome_locale):
        recensioni_del_locale = [rec for rec in self.storico_recensioni if rec.locale_nome == nome_locale]

        if not recensioni_del_locale:
            return 0.0

        totale_voti = sum(rec.voto for rec in recensioni_del_locale)
        media = totale_voti / len(recensioni_del_locale)

        return round(media, 1)

    def mostra_media_locali(self):
        print("\n" + "═" * 40)
        print("       CLASSIFICA MEDIA VOTI")
        print("═" * 40)

        for categoria, lista_locali in self.catalogo_locali.items():
            print(f"\n--- {categoria.upper()} ---")
            for locale in lista_locali:
                nome = locale.get_nome()
                media = self.get_media_voti(nome)

                stelle_piene = "★" * int(media)
                stelle_vuote = "☆" * (5 - int(media))

                print(f"{nome:25} | {media} {stelle_piene}{stelle_vuote}")
