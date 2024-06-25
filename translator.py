from dictionary import Dictionary


class Translator:

    def __init__(self):
        self.dictionary = Dictionary()

    def printMenu(self):
        print("Translator Alien-Italian")
        print("-------------------------")
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Stampa tutto il dizionario")
        print("5. Exit")
        print("-------------------------")

    def loadDictionary(self, filename):
        self.dictionary.load(filename)

    def handleAdd(self, entry):
        try:
            parti = entry.split(maxsplit=1)
            parola_aliena = parti[0]
            traduzioni = parti[1].split()
            self.dictionary.addWord(parola_aliena, traduzioni)
            print(f"Aggiunta la parola '{parola_aliena}' con traduzioni {', '.join(traduzioni)}")
        except IndexError:
            print("Errore: input non valido. Utilizzare il formato 'parola_aliena traduzione1 traduzione2 ...'.")

    def handleTranslate(self, query):
        traduzioni = self.dictionary.translate(query)
        if traduzioni:
            print(f"La traduzione di '{query}' è {', '.join(traduzioni)}")
        else:
            print(f"La parola '{query}' non è presente nel dizionario.")

    def handleWildCard(self, query):
        traduzioni = self.dictionary.translateWordWildCard(query)
        if traduzioni:
            print(f"Le traduzioni per '{query}' sono: {', '.join(traduzioni)}")
        else:
            print(f"Nessuna traduzione trovata per '{query}'")

    def handlePrintDictionary(self):
        self.dictionary.printDictionary()
