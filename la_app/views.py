from flask import request, render_template, url_for, redirect, flash
from la_app import app
from la_app.forms import TransactionForm
from tools.apicomm import getAPIData
from tools.dbaccess import HandleDB
from datetime import datetime

DBPATH = app.config['DBFILE']
API_KEY = app.config['API_KEY']

db = HandleDB(DBPATH)

def getWallet():
    query = """
    SELECT SUM(quantity_to) as total, currency_to
      FROM movimientos 
     GROUP BY currency_to;
    """
    monedas_to = db.consulta(query)
    monedas_to.append((0, 'EUR'))

    wallet = {}
    for item in monedas_to:
        wallet[item[1]] = item[0]

    query = """
    SELECT SUM(quantity_from) as total, currency_from
      FROM movimientos 
     GROUP BY currency_from;
    """
    monedas_from = db.consulta(query)

    for item in monedas_from:
        wallet[item[1]] -= item[0]
    
    return wallet
        
def cryptConversion(form):
    data = getAPIData(app.config['CONVERSION_URL'], form.quantity_from.data, form.currencys_from.data, form.currencys_to.data, API_KEY)
    return data['data']['quote'][form.currencys_to.data]['price']

@app.route('/', methods=['GET', 'POST'])
def index():
    form = TransactionForm()
    mensajes = []

    try:
        wallet = getWallet()
    except Exception as e:
        print("**ERROR**🔧: Acceso a base de datos - wallet: {} - {}". format(type(e).__name__, e))
        mensajes.append("Error en acceso a base de datos. Consulte con el administrador.")

        return render_template('index.html', form=form, movimientos=[], mensajes=mensajes)

    choices = ["EUR"] + [crypt for crypt in wallet if wallet[crypt] > 0]
    form.currencys_from.choices = choices

    try:
        movimientos = db.consultaToDict("SELECT fecha_alta, hora_alta, quantity_from, currency_from, quantity_to, currency_to FROM movimientos order by fecha_alta, hora_alta;")
    except Exception as e:
        print("**ERROR**🔧: Acceso a base de datos - consulta movimientos: {} - {}". format(type(e).__name__, e))
        mensajes.append("Error en acceso a base de datos. Consulte con el administrador.")

        return render_template('index.html', form=form, movimientos=[], mensajes=mensajes)

    if request.method == 'POST':
        if form.validate():
            if form.calc.data:
                try:
                    price = cryptConversion(form)
                except Exception as e:
                    print("**ERROR**🔧: Acceso a API - consulta conversion: {} - {}". format(type(e).__name__, e))
                    mensajes.append("Error en acceso a API. Consulte con el administrador.")
                    return render_template('index.html', form=form, movimientos=[], mensajes=mensajes)


                form.quantity_to.data = price
                return render_template('index.html', form=form, movimientos=movimientos, mensajes=[])

            elif form.accept.data:
                now = datetime.now()
                fecha = str(now.date())
                hora = str(now.time())
                try:
                    db.consulta("INSERT INTO MOVIMIENTOS (fecha_alta, hora_alta, currency_from, quantity_from, currency_to, quantity_to) VALUES (?,?,?,?,?,?);", 
                                fecha, hora, 
                                form.currencys_from.data,
                                form.quantity_from.data, 
                                form.currencys_to.data, 
                                form.quantity_to.data)
                    return redirect(url_for("index"))
                except Exception as e:
                    print("**ERROR**🔧: Acceso a base de datos - insert: {} - {}". format(type(e).__name__, e))
                    mensajes.append("Error en acceso a base de datos. Consulte con el administrador.")

                    return render_template('index.html', form=form, movimientos=[], mensajes=mensajes)


    return render_template('index.html', form=form, movimientos=movimientos, mensajes=mensajes)

