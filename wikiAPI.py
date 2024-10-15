import wikipedia
import os

wikipedia.set_lang("es")
resultado = wikipedia.page(input("Inserte busqueda: "))
print(resultado.summary)
os.system('pause')