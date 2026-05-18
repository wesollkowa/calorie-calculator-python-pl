print("KALKULATOR KALORII")
while True:
    płeć = input("kobieta/mężczyzna [k/m]: ")
    if płeć != "k" and płeć != "m":
        koniec = input("nieprawidłowe dane... jeszcze raz [t/n]? ")
        if koniec == "n":
            break
        elif koniec != "t":
            koniec1 = input("nieprawidłowe dane... jeszcze raz [t/n]? ")
    elif płeć == "k" or płeć == "m":
        kg = float(input("waga [kg]: "))
        cm = float(input("wzrost [cm]: "))
        wiek = float(input("wiek: "))
        cel = input("jaki jest twój cel? [deficyt/utrzymanie wagi/nadwyżka]? ")
        print()
        print("wybierz współczynnik PAL (aktywność fizyczna):")
        print("1.2 - prawie całkowity brak aktywności, siedzący tryb życia")
        print("1.3 - mało ruchu, kilka tys. kroków dziennie")
        print("1.4 - lekka aktywność, troche spacerów")
        print("1.5 - umiarkowany ruch, regularne chodzenie")
        print("1.6 - aktywność kilka razy w tygodniu")
        print("1.7 - aktywny tryb życia, częste treningi")
        print("1.8 - wysoka aktywność fizyczna")
        print("1.9 - ciężkie treningi lub praca fizyczna")
        print("2.0 - bardzo wysoki wysiłek CODZIENNIE, sport wyczynowy")
        print()
        PAL = float(input())
        if PAL < 1.2 or PAL > 2:
            print("nieprawidłowy współczynnik PAL :(")
            print()
            continue
        if płeć == "k":
            PPM = 10*kg + 6.25*cm - 5*wiek - 161
            print("twoje PPM wynosi:", PPM, "kcal")
        elif płeć == "m":
            PPM = 10*kg + 6.25*cm - 5*wiek + 5
            print("twoje PPM wynosi:", PPM, "kcal")
        else:
            koniec = input("nieprawidłowe dane... jeszcze raz [t/n]? ")
            if koniec == "n":
                break
        CPM = round(PPM * PAL, 2)
        print("twoje CPM wynosi:", CPM, "kcal")
        if cel == "d" or cel == "deficyt":
            deficyt = round(CPM - 300, 2)
            print("bezpieczny deficyt wynosi ok.:", deficyt, "kcal")
        elif cel == "n" or cel == "nadwyżka" or cel == "nadwyzka":
            nadwyżka = round(CPM + 300, 2)
            print("bezpieczna nadwyżka wynosi ok.:", nadwyżka, "kcal")
        m = cm/100
        bmi = round(kg/(m**2), 2)
        print("twoje bmi wynosi", bmi)
        if bmi <18:
            print("niedowaga!!")
        elif 18<= bmi <= 24.9:
            print("prawidłowa masa ciała")
        elif 25 <= bmi < 30:
            print("nadwaga!")
        elif bmi >=30:
            print("otyłość!!!")
        print()
        koniec2 = input("jeszcze raz [t/n]? ")
        if koniec2 == "n":
            print("do zobaczenia!")
            break
        else:
            print()
