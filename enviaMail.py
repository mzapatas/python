import smtplib
from email.message import EmailMessage
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import imghdr

miCorreo = "miCorreo@gmail.com"
miPass = "miClave"

cryptos = open("crypto.txt", "r")
lista_cryptos = cryptos.read().splitlines()
cryptos.close()

emails = open("emails.txt", "r")
lista_emails = emails.read().splitlines()
emails.close()

for activo in lista_cryptos:
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
    plt.savefig(activo+'.png', dpi=600)
    df.to_excel(activo+'.xlsx', sheet_name="Hoja1")
    
    with open (activo+'.png','rb') as f:
        img_data = f.read()
        img_type = imghdr.what(f.name)
        img_name = activo+"."+img_type
    
    with open (activo+'.xlsx','rb') as x:
        xls_data = x.read()
        xls_type = "vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        xls_name = activo+'.xlsx'

    msg = EmailMessage()
    msg["Subject"] = "Grafico anual crypto "+activo
    msg["From"] = miCorreo
    msg["To"] = miCorreo
    msg["Cc"] = lista_emails
    msg.set_content("Grafico anual de la criptomoneda "+activo)
    
    msg.add_attachment(img_data, maintype = "image", subtype = img_type, filename = img_name)
    msg.add_attachment(xls_data, maintype = "application", subtype = xls_type, filename = xls_name)

    with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
        smtp.login(miCorreo,miPass)
        smtp.send_message(msg)
