from menu_base import Menu

class MenuRistorante(Menu):
    def carica_da_file(self):
        try:
            with open(self.percorso, "r") as f:
                for riga in f:
                    nome, prezzo = riga.strip().split(",")
                    self.piatti[nome] = prezzo
        except Exception as e:
            print(f"Errore caricamento piatti ristorante: {e}")