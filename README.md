Progetto Tablò

Descrizione breve
Il software nasce come un aggregatore intelligente che centralizza l'offerta gastronomica locale (Pizzerie, Trattorie, Ristoranti) in un'unica interfaccia. Permette all'utente di cercare locali, prenotare un tavolo (specificando giorno, ora e numero di coperti) e personalizzare l'ordine dei piatti in anticipo, visualizzando il prezzo aggiornato in tempo reale. Il sistema gestisce inoltre l'autenticazione degli utenti, lo storico delle prenotazioni e un sistema di recensioni per valutare l'esperienza.

Requisiti minimi della macchina
* Python: 3.10 o superiore
* RAM: 2GB (minimo)
* OS: Windows 10+, macOS 10.15+, o Linux (Ubuntu 20.04+)
* Spazio su disco: 100MB (per l'installazione e la persistenza dei dati nel database locale)

Istruzioni per il venv (Ambiente Virtuale)
Per preparare l'ambiente di esecuzione ed evitare conflitti con altre librerie, esegui i seguenti comandi nel terminale all'interno della cartella del progetto:

1. Crea l'ambiente: `python -m venv venv`
2. Attiva l'ambiente:
   - Su Windows: `.\venv\Scripts\activate`
   - Su macOS/Linux: `source venv/bin/activate`
3. Installa le librerie: `pip install -r requirements.txt`

Comando di avvio
Dopo aver attivato l'ambiente virtuale, avvia l'applicazione con il seguente comando:
```bash
python main.py
