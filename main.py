import translator as tr

t = tr.Translator()

# Caricamento del dizionario all'inizio
t.loadDictionary("dictionary.txt")

while True:
    t.printMenu()

    txtIn = input("Seleziona un'opzione: ").strip()

    # Controllo input
    if not txtIn.isdigit() or not (1 <= int(txtIn) <= 5):
        print("Opzione non valida. Riprova.")
        continue

    if int(txtIn) == 1:
        entry = input(
            "Inserisci la nuova parola e la traduzione (es. alien_word traduzione1 traduzione2 ...): ").strip()
        t.handleAdd(entry)
    elif int(txtIn) == 2:
        query = input("Inserisci la parola aliena da tradurre: ").strip()
        t.handleTranslate(query)
    elif int(txtIn) == 3:
        query = input("Inserisci la parola aliena con wildcard (es. par?la): ").strip()
        t.handleWildCard(query)
    elif int(txtIn) == 4:
        t.handlePrintDictionary()
    elif int(txtIn) == 5:
        print("Uscita dal programma.")
        break
