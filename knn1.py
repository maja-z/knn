
import math
from data import X, y, X_test, y_test

def oblicz_odleglosc(punkt_a, punkt_b):
   
    return math.sqrt(
        (punkt_a[0] - punkt_b[0])**2 + # wzrost
        (punkt_a[1] - punkt_b[1])**2 + # waga
        (punkt_a[2] - punkt_b[2])**2   # obwod talii
    )

def klasyfikacja_knn(nowy_obiekt, dane_treningowe, etykiety, k):

    lista_odleglosci = []

    for i in range(len(dane_treningowe)):
        dystans = oblicz_odleglosc(nowy_obiekt, dane_treningowe[i])
       
        lista_odleglosci.append((dystans, etykiety[i]))

    lista_odleglosci.sort()

    najblizsi_sasiedzi = lista_odleglosci[:k]

    glosy = {}

    for dystans, rozmiar in najblizsi_sasiedzi:
        if rozmiar in glosy:
            glosy[rozmiar] += 1
        else:
            glosy[rozmiar] = 1

    wynik = max(glosy, key=glosy.get)
    
    return wynik

k = 3


poprawne_trafienia = 0
liczba_probek = len(X_test) 

for i in range(liczba_probek):
    klient_testowy = X_test[i]   
    prawdziwy_rozmiar = y_test[i] 
    
   
    przewidziany_rozmiar = klasyfikacja_knn(klient_testowy, X, y, k)
    
    if przewidziany_rozmiar == prawdziwy_rozmiar:
        poprawne_trafienia += 1
        print(f"Klient {i}: Prawdziwy rozmiar={prawdziwy_rozmiar}, Wynik={przewidziany_rozmiar} -> OK")
    else:
        print(f"Klient {i}: Prawdziwy rozmiar={prawdziwy_rozmiar}, Wynik={przewidziany_rozmiar} -> BŁĄD")

skutecznosc = (poprawne_trafienia / liczba_probek) * 100
print(f"\nSkuteczność algorytmu: {skutecznosc:.2f}%")
