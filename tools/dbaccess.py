import sqlite3

class HandleDB:
    def __init__(self, dbpath):
        self.path = dbpath
        self.conn = None
        self.cursor = None

    def consulta(self, query, *params):
        rows = self.__consulta(query, tuple(params))
        self.conn.close()
        return rows

    def consultaToDict(self, query, *params):
        rows = self.__consulta(query, tuple(params))
        rows = self.__toDictionary(rows)
        self.conn.close()
        return rows

    def consultaFromDataForm(self, query, data, *names):
        params = [data[name] for name in names ]
        rows = self.__consulta(query, params)
        rows = self.__toDictionary(rows)
        self.conn.close()
        return rows

    def __consulta(self, query, params):
        self.conn = sqlite3.connect(self.path)
        self.cursor = self.conn.cursor()

        self.cursor.execute(query, params)
        self.conn.commit()
        return self.cursor.fetchall()

    def __toDictionary(self, rows):
        if len(rows) == 0:
            return rows

        columnNames = []
        for columnName in self.cursor.description:
            columnNames.append(columnName[0])

        listaDeDiccionarios = []

        for fila in rows:
            d = {}
            for ix, columnName in enumerate(columnNames):
                d[columnName] = fila[ix]
            listaDeDiccionarios.append(d)

        return listaDeDiccionarios


