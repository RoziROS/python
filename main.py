#Projekt który będzie na bierząco aktualizowany start - 06.02.2022.

import random
import time

login = None
haslo = None

#Funkcja menu wyświelająca się po zalogowaniu.
def menu():
    print("Aby skorzystac z kalkulatora, wybierz - 1")
    print("Aby skorzystac z losowego generatora liczb wybierz - 2")
    print("Aby uzyskac dostep do bazy danych genshina, wybierz - 3")
    print("Aby uzyskac dostpe do bazy danych osob, wybierz - 4")
    print("Wyjscie z programu - enter")
    time.sleep(1)
    wybor=input("Prosze wybrac: ")
    if wybor == "1":
        kalkulator()
        time.sleep(1)
    elif wybor == "2":
        generator()
        time.sleep(1)
    elif wybor == "3":
        genshin()
        time.sleep(1)
    elif wybor == "4":
        osoby()
        time.sleep(1)
    elif wybor == "":
        exit()

#Funkcja kalkulator.
def kalkulator():
    l1 = None
    l2 = None
    wybor = None

    print("Witaj w kalkulatorze.")
    time.sleep(1)
    l1 = int(input("Podaj pierwsza liczbe: "))
    l2 = int(input("Podaj druga liczbe: "))
    time.sleep(1)
    print("Co chesz zrobic z tymi liczbami?")
    print("Dodac, wybierz - 1")
    print("Odjac, wybierz - 2")
    print("Pomnozyc, wybierz - 3")
    print("Podzielic, wybierz - 4")
    print("Chce wroc do menu - enter")
    time.sleep(1)
    wybor = input("Wybierz teraz: ")
    if wybor == "1":
        print("Dodanie tych liczb daje:",l1+l2)
        kontynujkalk()
    elif wybor == "2":
        print("Odjecie tych liczb daje:",l1-l2)
        kontynujkalk()
    elif wybor == "3":
        print("Pomnozenie tych liczb daje:",l1*l2)
        kontynujkalk()
    elif wybor == "4":
        print("Podzielenie tych liczb daje:",l1/l2)
        kontynujkalk()
    elif wybor == "":
        menu()

#Funkcja pytająca czy można kontynuować w kalkulatorze.
def kontynujkalk():
    kont = None
    kont = input("Jak mozna kontynuowac, nacisnij - enter")
    if kont == "":
        kalkpon()

#Funkcja pytająca czy chcesz ponownie skorzystać z kalkulatora.
def kalkpon():
    wybor = None
    print("Jak chcesz ponownie skorzystac z kalkulatora, wybierz - 1")
    print("Jak chcesz wrocic do menu, kliknij - enter")
    wybor = input("Wybierz teraz: ")
    if wybor == "1":
        kalkulator()
    elif wybor == "":
        menu()      

#Funkcja losowego generatora liczb.
def generator():
    wybor = None
    x = random.randint(1,6)
    y = random.randint(1,100)
    z = random.randint(1,1000)

    print("Witaj w losowym generatorze liczb.")
    print("Niestety generator posiada tylko okreslone zakresy liczb.")
    time.sleep(1)
    print("Wyswielt losowa liczbe z zakresu 1:6, wybierz - 1")
    print("Wyswielt losowa liczbe z zakresu 1:100, wybierz - ")
    print("Wyswielt losowa liczbe z zakresu 1:1000, wybierz - 3")
    print("Powrot do menu - enter")
    time.sleep(1)
    wybor = input("Wybierz teraz: ")
    time.sleep(1)
    if wybor == "1":
        print(x)
        kontynujgenerator()
    elif wybor == "2":
        print(y)
        kontynujgenerator()
    elif wybor == "3":
        print(z)
        kontynujgenerator()
    elif wybor == "":
        menu()

#Funkcja pytająca czy można kontynuować w generatorze.
def kontynujgenerator():
    kont = None
    kont = input("Jak mozna kontynuowac, nacisnij - enter")
    if kont == "":
        generator()

#Funkcja pytająca czy chcesz ponownie skorzystać z generatora.
def generatorpon():
    wybor = None
    print("Jak chcesz ponownie skorzystac z generatora, wybierz - 1")
    print("Jak chcesz wrocic do menu, nacisnij - enter")
    while not wybor:
        wybor = input("Wybierz teraz: ")
    if wybor == "1":
        generator()
    elif wybor == "":
        menu()

#Funkcja baza danych genshina.
def genshin():
    postaci = ("Hu Tao - 1","Zhongli - 2","Ganyu - 3","Chce wrocic do menu - enter")

    bronie_HuTao = ["Bronie: ","1. Staff Of Homa","2. Dragon's Bane","3. Deathmatch"]
    art_HuTao = ["Artefakty: ","1. Crimson Witch of Flames x4","2. Shimenawa's Reminiscence x4"]
    team_HuTao = ["Teamy: ","1. Hu Tao/Zhongli/Xingqiu/Sucrose"]
    build_HuTao = "Bronie - 1        Artefakty - 2        TeamComp - 3"

    bronie_Zhongli = ["Bronie: ","1. Staff of Homa","2. PJWS","3. Vortex"]
    art_Zhongli = ["Artefakty: ","1. Archaic petra x2 Noblesse x2","2. Emblem of Severend Fate x4"]
    team_Zhongli = ["Teamy: ","Zhongli jest supp/subdps wiec nie ma strikte pod niego teamow"]
    build_Zhongli = "Bronie - 1        Artefakty - 2        TeamComp - 3"

    bronie_Ganyu = ["Bronie: ","1. Amos' Bow","2. Thundering Pulse","3. Skyward Harp"]
    art_Ganyu = ["Artefakty: ","1. Shimenawa's Reminiscence x4","2. Wanderer's Troupe x4"]
    team_Ganyu= ["Teamy: ","Ganyu/Zhongli/Bennett/Xaingling"]
    build_Ganyu = "Bronie - 1        Artefakty - 2        TeamComp - 3"

    wybor = None
    wybor2 = None

    print("Witaj w bazie danych genshina.")
    print("Ktora postac cie interesuje?")
    for value in postaci:
        print(value)
    time.sleep(1)
    wybor = input("Podaj teraz: ")
    time.sleep(1)
    if wybor == "1":
        print(build_HuTao)
        while not wybor2:
            time.sleep(1)
            wybor2 = input("Jakie chcesz infomacje: ")
        if wybor2 == "1":
            for x in (bronie_HuTao):
                print(x)
            kontynujgenshin()
        elif wybor2 == "2":
            for x in (art_HuTao):
                print(x)
            kontynujgenshin()
        elif wybor2 == "3":
            for x in (team_HuTao):
                print(x)
            kontynujgenshin()
    elif wybor == "2":
        print(build_Zhongli)
        time.sleep(1)
        while not wybor2:
            wybor2 = input("Jakie chcesz infomacje: ")
        if wybor2 == "1":
            for x in (bronie_Zhongli):
                print(x)
            kontynujgenshin()
        elif wybor2 == "2":
            for x in (art_Zhongli):
                print(x)
            kontynujgenshin()
        elif wybor2 == "3":
            for x in (team_Zhongli):
                print(x)
            kontynujgenshin()
    elif wybor == "3":
        print(build_Ganyu)
        time.sleep(1)
        while not wybor2:
            wybor2 = input("Jakie chcesz infomacje: ")
        if wybor2 == "1":
            for x in (bronie_Ganyu):
                print(x)
            kontynujgenshin()
        elif wybor2 == "2":
            for x in (art_Ganyu):
                print(x)
            kontynujgenshin()
        elif wybor2 == "3":
            for x in (team_Ganyu):
                print(x)
            kontynujgenshin()
    elif wybor == "":
        menu()

#Funkcja pytająca czy można kontynuować w bazie danych genshina.
def kontynujgenshin():
    kont = None
    kont = input("Jak mozna kontynuowac, nacisnij - enter")
    if kont == "":
        genshin()

#Funkcja pytająca czy chcesz ponownie skorzystać z bazy danych genshina.
def genshinpon():
    wybor = None
    print("Jak chcesz ponownie skorzystac z bazy danych genshina, wybierz - 1")
    print("Jak chcesz wrocic do menu, nacisnij - enter")
    while not wybor:
        wybor = input("Wybierz teraz: ")
    if wybor == "1":
        genshin()
    elif wybor == "":
        menu()

#Funkcja baza danych osób.
def osoby():
    daneNR = {"Imie:":"Nikodem Rosenkranz","Wiek:":17,"Wzrost:":170.5,"Kolor oczu:":"niebieskie"}
    daneAR = {"Imie:":"Alicja Rosenkranz","Wiek:":38,"Wzrost:":165.0,"Kolor oczu:":"niebieskie"}
    daneAK = {"Imie:":"Adrian Kozlowski","Wiek:":41,"Wzrost:":182.5,"Kolor oczu:":"zielone"}
    daneKR = {"Imie:":"Klaudiusz Rosenkranz","Wiek:":21,"Wzrost:":174.5,"Kolor oczu:":"piwne"}

    wybor = None

    print("Witaj w bazie danych osob.")
    print("Kogo danych potrzebujesz?")
    print("Nikodem Rosenkranz - NR")
    print("Alicja Rosenkranz - AR")
    print("Adrian Kozlowski - AK")
    print("Klaudiusz Rosenkranz - KR")
    print("Powrot do menu - enter")
    time.sleep(1)
    wybor = input("Wybierz teraz: ")
    if wybor == "NR":
        for key, value in daneNR.items():
            print(key, value)
        osobykontynuj()
    elif wybor == "AR":
        for key, value in daneAR.items():
            print(key, value)
        osobykontynuj()
    elif wybor == "AK":
        for key, value in daneAK.items():
            print(key, value)
        osobykontynuj()
    elif wybor == "KR":
        for key, value in daneKR.items():
            print(key, value)
        osobykontynuj()
    elif wybor == "":
        menu()

#Funkcja pytająca czy można kontynuować w bazie danych osób.
def osobykontynuj():
    kont = None
    kont = input("Jak mozna kontynuowac, nacisnij - enter")
    if kont == "":
        osoby()

#Funkcja pytająca czy chcesz ponownie skorzystać z bazy danych osób.
def osobypon():
    wybor = None
    print("Jak chcesz ponownie skorzystac z bazy danych osob, wybierz - 1")
    print("Jak chcesz wrocic do menu, wybierz - 2")
    while not wybor:
        wybor = input("Wybierz teraz: ")
    if wybor == "1":
        osoby()
    elif wybor == "2":
        menu()

#System logowania.
while not login:
    login = input("Podaj login: ")
    if login == "Login":
        while not haslo:
            haslo = input("Podaj haslo: ")
            if haslo == "Haslo":
                time.sleep(1)
                print("Zalogowales sie poprawnie.")
                time.sleep(1)
                menu()
        else:
            print("Bledne haslo.")
            exit()
else:
    print("Bledny login.")