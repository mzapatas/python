import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

fscope = open("crypto.txt", "r")
scope = fscope.read().splitlines()
fscope.close()

for activo in scope:
    datos = yf.Ticker(activo).history(period="1y")
    df = pd.DataFrame(datos)
    precio = datos["Close"]
    # volumen = datos["Volume"]
    df.index = df.index.tz_localize(None)
    plt.figure(activo, figsize=(12,6))
    plt.title(activo)
    plt.xlabel('Tiempo')
    plt.ylabel('Valores')
    plt.plot(precio)
    img = plt.savefig(activo+'.png', dpi=600)
    df.to_excel(activo+'.xlsx', sheet_name="Hoja1")
    # plt.show()
