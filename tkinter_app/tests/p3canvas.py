from tkinter import *
from tkinter import ttk
import datetime
from tkinter_app.entities import config

print(config['DB_FILE'])

root = Tk()
root.geometry("732x150")
fontH = ("Courier", 14, "bold")
fontL = ("Courier", 14)
movimientos = [{'fecha': datetime.date(2020, 3, 16), 'hora': datetime.time(16, 13, 38), 'from': 'BNB', 'to': 'BTC', 'qfrom': 579.4876989299511, 'qto': 934.3138430430595, 'pu': 0.6202280992033256}, {'fecha': datetime.date(2020, 1, 18), 'hora': datetime.time(10, 43, 23), 'from': 'LTC', 'to': 'EUR', 'qfrom': 393.9316754154779, 'qto': 347.9068630715173, 'pu': 1.1322906134636945}, {'fecha': datetime.date(2020, 4, 2), 'hora': datetime.time(11, 54, 17), 'from': 'EUR', 'to': 'BNB', 'qfrom': 249.85542267218187, 'qto': 335.097716644812, 'pu': 0.7456195917235001}, {'fecha': datetime.date(2020, 7, 20), 'hora': datetime.time(14, 46, 26), 'from': 'ETH', 'to': 'BNB', 'qfrom': 576.1637779484013, 'qto': 367.640908029975, 'pu': 1.567191695385065}, {'fecha': datetime.date(2021, 1, 15), 'hora': datetime.time(15, 43, 5), 'from': 'BTC', 'to': 'BNB', 'qfrom': 183.73682831402925, 'qto': 439.7307569014893, 'pu': 0.41783938337338294}, {'fecha': datetime.date(2020, 1, 6), 'hora': datetime.time(11, 42, 59), 'from': 'BTC', 'to': 'ETH', 'qfrom': 190.58098378473852, 'qto': 680.4747855716527, 'pu': 0.2800706033870681}, {'fecha': datetime.date(2020, 9, 3), 'hora': datetime.time(1, 27, 45), 'from': 'BTC', 'to': 'BTC', 'qfrom': 9.615979761243953, 'qto': 961.9684408959617, 'pu': 0.00999614888851009}, {'fecha': datetime.date(2020, 12, 24), 'hora': datetime.time(6, 23, 1), 'from': 'ETH', 'to': 'LTC', 'qfrom': 894.1101723906464, 'qto': 598.635428016621, 'pu': 1.4935804507143564}, {'fecha': datetime.date(2020, 10, 12), 'hora': datetime.time(13, 51), 'from': 'EUR', 'to': 'LTC', 'qfrom': 808.0575224429001, 'qto': 946.0867266866111, 'pu': 0.8541051255130516}, {'fecha': datetime.date(2020, 4, 27), 'hora': datetime.time(4, 40, 45), 'from': 'ETH', 'to': 'LTC', 'qfrom': 668.0148110962846, 'qto': 517.3942886229285, 'pu': 1.291113616414747}, {'fecha': datetime.date(2020, 5, 6), 'hora': datetime.time(12, 54, 36), 'from': 'EUR', 'to': 'ETH', 'qfrom': 789.2108082453319, 'qto': 292.3893785998599, 'pu': 2.6991774189081643}, {'fecha': datetime.date(2021, 1, 3), 'hora': datetime.time(16, 48, 37), 'from': 'EUR', 'to': 'EUR', 'qfrom': 219.5243061501856, 'qto': 290.8842635223837, 'pu': 0.7546792098407656}, {'fecha': datetime.date(2020, 11, 5), 'hora': datetime.time(23, 32, 56), 'from': 'EUR', 'to': 'BTC', 'qfrom': 608.8479546964829, 'qto': 991.8391481839061, 'pu': 0.6138575552409944}, {'fecha': datetime.date(2020, 7, 19), 'hora': datetime.time(13, 11, 40), 'from': 'LTC', 'to': 'ETH', 'qfrom': 63.48143195126321, 'qto': 668.9129854029075, 'pu': 0.09490237644740344}, {'fecha': datetime.date(2020, 5, 25), 'hora': datetime.time(1, 59, 7), 'from': 'EUR', 'to': 'EUR', 'qfrom': 71.64783120278351, 'qto': 606.8980276283401, 'pu': 0.11805579840615353}]
cabecera1 = "   Fecha     Hora   From      Cantidad        To       Cantidad        Precio unitario  "
cabecera2 = "---------- -------- ---- ------------------- --- ------------------- -------------------"
fLinea = "{} {}  {} {:19.9f} {} {:19.9f} {:19.9f}"

# Crear cabeceras arriba a la izquierda
lblH1 = Label(root, text=cabecera1, font = fontH, width=88)
lblH1.pack(side=TOP, anchor=W)

lblH2 = Label(root, text=cabecera2, font = fontH, width=88)
lblH2.pack(side=TOP, anchor=W)

#Crear listbox scrollable abajo a la izquierda
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set, font=fontL, bd=0 )
for line in movimientos:
    mylist.insert(END, fLinea.format(line['fecha'], line['hora'], 
                                     line['from'], line['qfrom'],
                                     line['to'], line['qto'], line['pu']))

mylist.pack( side = LEFT, fill = BOTH , expand = True)
scrollbar.config( command = mylist.yview )


root.mainloop()
