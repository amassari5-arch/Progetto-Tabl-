class ComponentePiatto:
    def get_prezzo(self): pass
    def get_nome(self): pass

class PiattoBase(ComponentePiatto):

    def __init__(self, nome, prezzo):
        self.nome = nome
        self.prezzo = float(prezzo)

    def get_prezzo(self):
        return self.prezzo

    def get_nome(self):
        return self.nome


class Extrapiatto(ComponentePiatto):

    def __init__(self, componente):
        self.componente = componente


class Tartufo(Extrapiatto):
    def get_prezzo(self):
        return self.componente.get_prezzo() + 15.0

    def get_nome(self):
        return f"{self.componente.get_nome()} + Tartufo"


class Patatine(Extrapiatto):
    def get_prezzo(self):
        return self.componente.get_prezzo() + 3.5

    def get_nome(self):
        return f"{self.componente.get_nome()} + Patatine"


class Bruschetta(Extrapiatto):
    def get_prezzo(self):
        return self.componente.get_prezzo() + 5.0

    def get_nome(self):
        return f"{self.componente.get_nome()} + Bruschette"


# Classe tavolo
class Tavolo:
    def __init__(self, numero_persone, data, ora):
        self.numero_persone = numero_persone
        self.data = data
        self.ora = ora
        self.ordine_piatti = []

    def aggiungi_piatto(self, nome_piatto, prezzo):
        self.ordine_piatti.append((nome_piatto, prezzo))

    def calcola_totale(self):
        totale = 0.0
        for _, prezzo in self.ordine_piatti:
            totale += float(prezzo)
        return totale

    def get_info_tavolo(self):
        return f"Posti: {self.numero_persone} | Giorno: {self.data} | Orario: {self.ora}"

    def genera_riepilogo(self):
        print("\n" + "=" * 30)
        print("      RIEPILOGO FINALE")
        print("=" * 30)
        print(self.get_info_tavolo())
        print("-" * 30)
        for p, pr in self.ordine_piatti:
            print(f"- {p}: €{pr:.2f}")
        print("-" * 30)
        print(f"TOTALE: €{self.calcola_totale():.2f}")