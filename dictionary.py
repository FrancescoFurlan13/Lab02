import re

class Dictionary:
    def __init__(self):
        self.dizionario = {}

    def load(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                parole = line.strip().split(maxsplit=1)
                if len(parole) == 2:
                    parola_aliena, traduzioni = parole
                    traduzioni = traduzioni.split()
                    if parola_aliena.lower() in self.dizionario:
                        self.dizionario[parola_aliena.lower()].extend(traduzioni)
                    else:
                        self.dizionario[parola_aliena.lower()] = traduzioni

    def addWord(self, parola_aliena, traduzioni):
        if parola_aliena.lower() in self.dizionario:
            self.dizionario[parola_aliena.lower()].extend(traduzioni)
        else:
            self.dizionario[parola_aliena.lower()] = traduzioni

    def translate(self, parola_aliena):
        return self.dizionario.get(parola_aliena.lower())

    def translateWordWildCard(self, query):
        # Sostituire "?" con "." per creare il pattern regex
        pattern = query.replace('?', '.')
        regex = re.compile(pattern, re.IGNORECASE)  # Ignora maiuscole/minuscole
        risultati = []
        for parola, traduzioni in self.dizionario.items():
            if regex.fullmatch(parola):
                risultati.extend(traduzioni)
        return risultati

    def printDictionary(self):
        if not self.dizionario:
            print("Il dizionario è vuoto.")
        else:
            for parola_aliena, traduzioni in sorted(self.dizionario.items()):
                print(f"{parola_aliena}: {', '.join(traduzioni)}")
