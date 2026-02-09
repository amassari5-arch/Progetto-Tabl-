# Gestione recensione
class Recensione:
    def __init__(self, cliente, locale_nome, voto, commento):
        self.cliente = cliente
        self.locale_nome = locale_nome
        self.voto = self._valida_voto(voto)
        self.commento = commento

    def _valida_voto(self, vot):
        try:
            vot_int = int(vot)
            return max(1, min(5, vot_int))
        except ValueError:
            print("! ERRORE: Voto non valido!")
            return 1

    def __str__(self):
        stelle = "★" * self.voto + "☆" * (5 - self.voto)
        return f"{stelle} | {self.cliente._nome} ha lasciato questa recensione sul locale : [{self.locale_nome}]: {self.commento}"