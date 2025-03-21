def zmien_wartosc(arg):
    """Modyfikuje argument w zależności od jego typu"""
    if isinstance(arg, list):  #Jeśli jest listą
        print(f"Przed zmianą (lista): {arg}")
        arg[0] = 'kalafior'
        print(f"Po zmianie (lista): {arg}")
    elif isinstance(arg, int):  #Jeśli jest liczbą całkowitą
        print(f"Przed zmianą (int): {arg}")
        arg = 65482652
        print(f"Po zmianie (int): {arg} (tylko wewnątrz funkcji!)")
    else:
        print("Nieobsługiwany typ danych!")

#Test dla listy - mutowalny typ
moja_lista = [1, 2, 3]
zmien_wartosc(moja_lista)  #Modyfikuje oryginalną listę
print(f"Po wywołaniu funkcji (lista): {moja_lista}\n")  #Zmiana widoczna na zewnątrz

#Test dla liczby - niemutowalny typ
moja_liczba = 42
zmien_wartosc(moja_liczba)  #Nie zmienia oryginalnej liczby
print(f"Po wywołaniu funkcji (int): {moja_liczba}")  #Oryginalna liczba się NIE zmienia
