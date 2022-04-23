from scraper import CryptoCurrency
import time
import os



if __name__ == '__main__':
    while True:
        symbol1 = CryptoCurrency(symbol="LINKEUR")
        symbol2 = CryptoCurrency(symbol="GRTEUR")
        symbol3 = CryptoCurrency(symbol="BTCEUR")
        symbol4 = CryptoCurrency(symbol="ETHEUR")
        CryptoCurrency.show_prices()
        time.sleep(3)
        CryptoCurrency.clean_prices()
        os.system("cls")