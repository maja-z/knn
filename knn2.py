import math
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


def oblicz_odleglosc(punkt_a, punkt_b):
    suma = 0
    for i in range(len(punkt_a)):
        suma += (punkt_a[i] - punkt_b[i])**2
    return math.sqrt(suma)


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


iris = load_iris()

X = iris.data.tolist()
y = [iris.target_names[i] for i in iris.target]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=39
)

X = X_train
y = y_train


k = 3


poprawne_trafienia = 0
liczba_probek = len(X_test)

for i in range(liczba_probek):
    klient_testowy = X_test[i]
    prawdziwy_rozmiar = y_test[i]

    przewidziany_rozmiar = klasyfikacja_knn(klient_testowy, X, y, k)

    if przewidziany_rozmiar == prawdziwy_rozmiar:
        poprawne_trafienia += 1
        print(f"Próbka {i}: Prawdziwy={prawdziwy_rozmiar}, Wynik={przewidziany_rozmiar} -> OK")
    else:
        print(f"Próbka {i}: Prawdziwy={prawdziwy_rozmiar}, Wynik={przewidziany_rozmiar} -> BŁĄD")


skutecznosc = (poprawne_trafienia / liczba_probek) * 100
print(f"\nSkuteczność algorytmu: {skutecznosc:.2f}%")