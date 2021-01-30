CREATE TABLE "movimientos" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"fecha_alta"	TEXT NOT NULL,
	"hora_alta"	TEXT NOT NULL,
	"currency_from"	TEXT NOT NULL,
	"quantity_from"	REAL NOT NULL,
	"currency_to"	TEXT NOT NULL,
	"quantity_to"	REAL
)