import requests
from os import path
import argparse
import sys
import os

parser = argparse.ArgumentParser()
parser.add_argument('-t','--target',help='indicar dominio')
parser = parser.parse_args()

def main():
    if parser.target:
        if path.exists('subdomains.txt'):
            wordlist = open('subdomains.txt','r')
            wordlist = wordlist.read().split('\n')

            for subdominio in wordlist:
                url = "http://"+subdominio+"."+parser.target
                try:
                    requests.get(url)
                except requests.ConnectionAbortedError:
                    os.system('pause')
                else:
                    print("(+) Subdominio encontrado: " + url)

            for subdominio in wordlist:
                url = "https://"+subdominio+"."+parser.target
                try:
                    requests.get(url)
                except requests.ConnectionAbortedError:
                    os.system('pause')
                else:
                    print("(+) Subdominio encontrado: " + url)   
    else:
        print("(-) Ingrese un dominio")
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()