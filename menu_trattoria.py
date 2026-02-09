from menu_base import Menu

class MenuTrattoria(Menu):
    def carica_da_file(self):
        try:
            with open(self.percorso, "r") as f:
                for riga in f:
                    nome, prezzo = riga.strip().split(",")
                    self.piatti[nome] = prezzo
        except Exception as e:
            print(f"Errore caricamento piatti trattoria: {e}")