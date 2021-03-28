import sys
from string_and_bytes import *
from COM_ports import *
from communication import *


def main():
    while True:
        print("XMODEM Python")
        print("Lukasz Janiszewski, Jakub Muszynski")
        print()
        print("Wybierz opcję:\n"
              "1. Rozpocznij program\n"
              "2. Zakończ program")
        wybor_uzytkownika = int(input("Twój wybór: "))
        while wybor_uzytkownika not in [1, 2]:
            print("Wybrano zla opcje!")
            wybor_uzytkownika = int(input("Twój wybór: "))
        if wybor_uzytkownika == 2:
            sys.exit()
        print()
        print("Wybierz tryb pracy:\n"
              "1. Wysyłanie\n"
              "2. Odbieranie")
        tryb_pracy = int(input("Twój wybór: "))
        while tryb_pracy not in [1, 2]:
            print("Wybrano zla opcje!")
            tryb_pracy = int(input("Twój wybór: "))
        print()
        connected_ports = available_ports()
        print("Wybierz port:")
        iteration = 1
        if not connected_ports:
            print("BRAK DOSTEPNYCH PORTOW!")
        else:
            for connected_port in connected_ports:
                print(str(iteration) + ". " + str(connected_port))
                iteration += 1
            wybrany_port = int(input("Twój wybór: "))
            while wybrany_port not in range(1, iteration-1):
                print("Wybrano zla opcje!")
                wybrany_port = int(input("Twój wybór: "))
        print()
        print("Z jakiego algorytmu obliczania sumy kontrolnej chcesz skorzystać?\n"
              "1. Domyślny algorytm protokołu Xmodem \n"
              "2. CRC16")
        algorytm_sumy = int(input("Twój wybór: "))
        while algorytm_sumy not in [1, 2]:
            print("Wybrano zla opcje!")
            algorytm_sumy = int(input("Twój wybór: "))
        if algorytm_sumy == 2:
            crc = True
        else:
            crc = False
        print()
        print("Wpisz wiadomosc jaka chcesz wyslac:")
        wiadomosc = str(input())
        bytesText = string_to_bytes(wiadomosc)
        print()
        print(prepare_packets(bytesText, crc))

        # Wywołanie funkcji wysylania i odbierania

        print()
        print()


if __name__ == '__main__':
    main()

