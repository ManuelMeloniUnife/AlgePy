class Matrix:
    def __init__(self, data):
        # verifico che i dati siano una lista di liste:
        if not all(isinstance(row, list) for row in data):
            raise TypeError("""Errore: 
                            \nLe matrici DEVONO essere implementate come liste di liste 
                            \nEsempio: A = MATRIX([[1, 2, 3], [4, 5, 6], [7, 8, 9]])""")

        # verifico che tutte le righe abbiano la stessa lunghezza:
        row_lengths = {len(row) for row in data}
        if len(row_lengths) > 1:
            raise ValueError("""Errore:
                            \nLe righe delle matrici DEVONO avere tutte la stessa lunghezza.""")

        self.data = data
        # Numero righe
        self.rows = len(data)
        # Numero colonne, gestisce il caso di matrice vuota
        self.cols = len(data[0]) if data else 0

    def __str__(self):
        # Rappresentazione leggibile della matrice
        return "\n\n\n".join(["\t".join(map(str, row)) for row in self.data])

    def __repr__(self):
        # Rappresentazione tecnica utile per il debugging
        return f"Matrix((self.data))"
