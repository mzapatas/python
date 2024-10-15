import subprocess
import argparse
import sys

p = argparse.ArgumentParser()
p.add_argument('-t','--target', help="Indica una URL")
p = p.parse_args()

def main():

    if p.target:
        subprocess.call("wad -u"+p.target+">tecno.txt",shell=True)
    else:
        print("Ingrese una URL")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
