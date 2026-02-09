from abc import ABC, abstractmethod


# Classe base per ogni locale
class Locale(ABC):
    def __init__(self, nome, indirizzo, descrizione, oggetto_menu, capienza):
        self._nome = nome
        self._indirizzo = indirizzo
        self._descrizione = descrizione
        self.gestore_menu = oggetto_menu

        # Gestione capienza
        self.posti_totali = capienza
        self.posti_occupati = 0

        self.orari_apertura = {
            "Lunedì": "19:00 - 23:30",
            "Martedì": "19:00 - 23:30",
            "Mercoledì": "19:00 - 23:30",
            "Giovedì": "19:00 - 23:30",
            "Venerdì": "19:00 - 00:30",
            "Sabato": "12:30 - 15:00, 19:00 - 01:00",
            "Domenica": "12:30 - 15:00, 19:00 - 23:30"
        }

    @abstractmethod
    def get_tipo(self):
        pass

    def get_nome(self):
        return self._nome

    def posti_liberi(self, numero_persone):
        return (self.posti_occupati + numero_persone) <= self.posti_totali

    def prenota_posti(self, numero_persone):
        self.posti_occupati += numero_persone

    def mostra_dettagli(self):
        print(f"\n" + "═" * 30)
        print(f"      {self._nome.upper()}")
        print("═" * 30)
        print(f"Tipo: {self.get_tipo()}")
        print(f"Indirizzo: {self._indirizzo}")
        print(f"Descrizione: {self._descrizione}")
        print(f"Capienza Totale: {self.posti_totali} posti")
        print(f"Posti Liberi: {self.posti_totali - self.posti_occupati}")

        print("\nOrari di apertura:")

        for giorno, orario in self.orari_apertura.items():
            print(f"  {giorno:10}: {orario}")


# Classi locali
class Pizzeria(Locale):
    def __init__(self, nome, indirizzo, descrizione, oggetto_menu):
        super().__init__(nome, indirizzo, descrizione, oggetto_menu, 80)

    def get_tipo(self):
        return "Pizzeria"


class Trattoria(Locale):
    def __init__(self, nome, indirizzo, descrizione, oggetto_menu):
        super().__init__(nome, indirizzo, descrizione, oggetto_menu, 60)

    def get_tipo(self):
        return "Trattoria"


class Ristorante(Locale):
    def __init__(self, nome, indirizzo, descrizione, oggetto_menu):
        super().__init__(nome, indirizzo, descrizione, oggetto_menu, 40)

    def get_tipo(self):
        return "Ristorante"