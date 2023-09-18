import math

def Pole_Kwadratu(a):
    return a**2

def Pole_prostokąta (a, b):
    return a * b

def Pole_Trapezu(a, b, h):
    return ((a+b) *h)/2

def Pole_Trójkąta (a, h):
    return (a * h)/2

def Pole_Trójkąta_równobocznego(a):
    return (((a**2)*3**(1/2))) / 4

def Tw_Pitagorasa(a, b):
    return (a**2+ b**2)**(1/2)

def Pole_Koła(n):
    return (n*n) * 3.14

def Pole_równoległoboku_i_rombu1(a, b):
    return a * b

def Pole_rombu2(e, f):
    return (e*f)/2

def kalkulator():
    print("Witaj w kalkulatorze!")
    while True:
        print("Dostępne opcje")
        print("1, Pole kwadratu")
        print("2, Pole prostokąta")
        print("3, Pole trapezu")
        print("4, Pole trójkąta równobocznego")
        print("5, Twierdzenie pitagorasa - przeciwprostokątna")
        print("6, Pole koła")
        print("7, Pole Równoległoboku i Rombu_1 (boki)")
        print("8, Pole Rombu_2 (przekątne)")
        print("9, trójkąt")
        print("10, wyjście")

        print("Dostępne opcje : 1/2/3/4/5/6/7/8/9/10  ")
        wybor = input("Twój wybór : ")

        if wybor == '10':
            print("Koniec")
            break

        if wybor not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'):
            print("Error 404 - wybrałeś znak spoza zakresu")
            print("")    
            input("Naciśnij Enter aby kontynuować ...")
            print("") 
            continue

        if wybor == "1":
            a = float(input("Podaj długość boku : "))
            wynik = Pole_Kwadratu(a)
            print (f"Pole kwadratu wynosi: {wynik}")
        elif wybor == '2':
            a = float(input("Podaj długość boku 1 : "))
            b = float(input("Podaj długość boku 2 : "))
            wynik = Pole_prostokąta(a, b)
            print (f"Pole prostokąta wynosi: {wynik}")
        elif wybor == '3':
            a = float(input("Podaj długość boku 1 : "))
            b = float(input("Podaj długość boku 2 : "))
            h = float(input("Podaj wysokość : ")) 
            wynik = Pole_Trapezu(a, b, h)
            print (f"Pole Trapezu wynosi: {wynik}")
        elif wybor == '9':
            a = float(input("Podaj długość boku 1 : "))
            h = float(input("Podaj wysokość : "))
            wynik = Pole_Trójkąta (a, h)
            print(f"Pole Trójkata wvnosi: {wynik}")
        elif wybor == '4':
            a = float(input("Podaj długość boku : "))
            wynik = Pole_Trójkąta_równobocznego(a)
            print(f"Pole Trójkąta Równobocznego wynosi: {wynik}")
        elif wybor == '5':
            a = float(input("Podaj długość przyprostokątnej 1 : "))
            b = float(input("Podaj długość przyprostokątnej 2 : "))
            wynik = Tw_Pitagorasa(a, b)
            print(f"Przeciwprostokątna wynosi: {wynik}")
        elif wybor == '6':
            r = float(input("Podaj długość promienia : "))
            wynik = Pole_Koła(r)
            print(f"Pole koła wynosi: {wynik}")
        elif wybor == '7':
            a = float(input("Podaj długość boku 1 : "))
            b = float(input("Podaj długość boku 2 : "))
            wynik = Pole_równoległoboku_i_rombu1(a, b)
            print(f"Pole Równoległoboku i rombu_2 wynosi: {wynik}")
        elif wybor == '8':
            e = float(input("Podaj długość przekątnej 1 : ")) 
            f = float(input("Podaj długość przekątnej 2 : "))
            wynik = Pole_rombu2(e, f)
            print(f"Pole Rombu_1 wynosi: {wynik}")
        print("")    
        input("Naciśnij Enter aby kontynuować ...")
        print("")        

if __name__=="__main__":
    kalkulator()


