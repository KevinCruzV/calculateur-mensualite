# app/__init__.py

from flask import Flask, render_template, request

from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio import start_server, config, platform
import flask

import pandas as pd
import numpy as np
import datetime

import numpy_financial as npf

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    M = ''
    I = ''
    if request.method == 'POST' and 'montant' in request.form and 'montant' in request.form and 'taux-interet' in \
            request.form and 'duree' in request.form and 'taux-assu' in request.form:
        C = float(request.form.get('montant'))
        T = str(request.form.get('taux-interet'))
        T = T.replace(",", ".")
        T = float(T)
        N2 = int(request.form.get('duree'))
        N = N2 * 12
        ASSU = str(request.form.get('taux-assu'))
        ASSU = ASSU.replace(",", ".")
        ASSU = float(ASSU)
        t = (T / 12)
        q = 1 + t / 100  # calcul du coefficient multiplicateur associé à une hausse de t%
        M = (q ** N * (C) * (1 - q) / (1 - q ** N)) + C * ((ASSU / 100) / 12)
        M = round(M)
        # print("Votre mensualité sera de {0:.2f} euros".format(M))
        I = N * M - C  # calcul des intérêts versés
        I = round(I)
        # put_text(f"Votre mensulaité sera de {M} euros")
        # put_text(f"Le montant total des intérêts versés sera de {I} euros")
        # T2 = T * 1 / 100
        # rng = pd.date_range("01-01-2021", periods=N, freq='MS')
        # rng.name = "Date"
        # df = pd.DataFrame(index=rng, columns=['Mensualité', 'Capital Amorti', 'Intérêts', 'Capital restant dû'],
        #                    dtype='float')
        # df.reset_index(inplace=True)
        # df.index += 1
        # # df.index.name = "Periode (Mois)"
        # #
        # M = -1 * npf.pmt(T2 / 12, N, C) + C * ((ASSU / 100) / 12)
        # # df["Capital Amorti"] = -1 * npf.ppmt(T2 / 12, df.index, N, C)
        # I = -1 * npf.ipmt(T2 / 12, df.index, N, C)
        # df = df.round(2)
        #
        # df["Capital restant dû"] = 0
        # df.loc[1, "Capital restant dû"] = C - df.loc[1, "Capital Amorti"]
        #
        # for period in range(2, len(df) + 1):
        #     previous_balance = df.loc[period - 1, "Capital restant dû"]
        #     principal_paid = df.loc[period, "Capital Amorti"]
        #
        #     if previous_balance == 0:
        #         df.loc[period, ["Mensualité", 'Capital Amorti', "Intérêts", "Capital restant dû"]] == 0
        #         continue
        #     elif principal_paid <= previous_balance:
        #         df.loc[period, "Capital restant dû"] = previous_balance - principal_paid
        #
        # df["Date"] = pd.to_datetime(df["Date"], format='%d-%m-%Y')

        # put_text("TABLEAU D'AMORTISSEMENT").style('color: dark; font-size: 20px; font-weight:bold;')
        # put_collapse('Voir le tableau', [put_html(df.to_html(border=0))])

    return render_template('index.html', M=M, I=I)
