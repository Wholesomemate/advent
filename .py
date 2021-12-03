# Advent callender

import datetime

def message(date):
    if date == 1:
        print("Vandaag start het al en om te starten geven we iets lekkers.")
    elif date == 2:
        datum = input("Wat wil je deze winter echt doen? ")
        if datum != "":
            print("Dat verdient een maja pledge")
    elif date == 3:
        print("voor de kaarsen die gaan komen heb je een adventkalender nodig")
    elif date == 4:
        print("Vanavond geef ik een goede nachtrust mee")
    elif date == 5:
        print("Vandaag krijg je tweede kaars voor op de advents kalender")
    elif date == 6:
        print("Vandaag vieren we de feest van mijn beste vriend sinterklaas dus niks voor jouw.")
    elif date == 7:
        datum = input("Wat wil je echt voor kerst hebben? " )
        if datum != "":
            print("Dat verdient sneeuw")
    elif date == 8:
        datum = input("Maak af: All i want for ")
        if datum != "":
            print("Dat daar verdient een maja pledge")
    elif date == 9:
        print("Op de 25ste krijg je cadeaus maar ondertussen maak vrienden")
    elif date == 10:
        datum = input("Waar vind je Rendier ")
        if datum != "":
            print("Mooi, maar het hangt af waar je ze hebt gelaten")
            print('Toch verdien je iets lekkers')
    elif date == 11:
        print("Vanavond geef ik een goede nachtrust mee")
    elif date == 12:
        print("Vandaag krijg je derde kaars voor op de adventskrans")
    elif date == 13:
        print("Nog twee weken doorbijten en hiervoor krijg je iets lekkers om te helpen")
    elif date == 14:
        print('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    elif date == 15:
        print('We wensen jullie corona vrije feestdagen')
    elif date == 16:
        datum = input('Noem een rendier van mij op?')
        if datum != "":
            print("Voor dat te weten krijg je iets lekkers")
    elif date == 17:
        print('Hopelijk valt er vanavond sneeuw')
    elif date == 18:
        print('Vanavond geef ik je een goede nachtrust mee')
    elif date == 19:
        print("Vandaag krijg je de laatste kaars voor op je adventskrans")
    elif date == 20:
        print('Nog een week doorbijten en hiervoor krijg je iets lekker om te helpen')
    elif date == 21:
        datum = input('Wat is je favorite kerstliedje')
        if datum != "":
            print("dat verdient een maja pledge")
    elif date == 22:
        datum = input("Waar woon ik?")
        if datum != "":
            print("Mooi dat verdien echt een goede nachtrust")
    elif date == 23:
        print("Nog twee dagen tot kerst en voor zo lang te wachten verdien je toch echt wel sneeuw")
    elif date == 24:
        print("Vanavond heb ik het druk maar toch krijg je nog iets lekkers")
    else:
        print("Mijn dag is eindelijk aangekomen wacht nog even en het is tijd")

def item(date): 
    if date == 1:
        b = "lekkers" 
    elif date == 2:
        b =  "maja pledge"
    elif date == 3:
        b = "adventkrans" 
    elif date == 4:
        b = "nachtrust"
    elif date == 5:
        b = "kaars" 
    elif date == 7:
        b = "sneeuw"
    elif date == 8:
        b = "maja pledge"
    elif date == 9:
        b = "cadeaus en vrienden"
    elif date == 10:
        b = "lekkers"
    elif date == 11:
        b = "nachtrust"
    elif date == 12:
        b = "kaars"
    elif date == 13:
        b = "lekkers"
    elif date == 14:
        b = "rickroll"
    elif date == 15:
        b = "corona"
    elif date == 16:
        b = "lekkers"
    elif date == 17:
        b = "sneeuw"
    elif date == 18:
        b = "nachtrust"
    elif date == 19:
        b = "kaars"
    elif date == 20:
        b = "lekkers"
    elif date == 21:
        b = "maja pledge"
    elif date == 22:
        b = "nachtrust"
    elif date == 23:
        b = "sneeuw"
    elif date == 24:
        b = "lekkers"
    else:
        b = ""
    return b


def advent(date):
    boodschap = message(date)
    if input("wil je zien wat je al hebt gekregen y/n: ") == "y":
        items = []
        for i in range(1,date+1):
            wat = item(i)
            if wat != "":
                items.append(wat)
        unique = []
        for i in items:
            if i not in unique:
                count = 0
                for j in items:
                    if i == j:
                        count += 1
                print(i , ":" , str(count))
                unique.append(i)

x = datetime.datetime.now()
date = x.day

missed = input("do you want to see today y/n: ")
if missed == "y":
    message = advent(date)
else:
    new_missed = input("do you want to see another day y/n: ")
    if new_missed == "y":
        which = int(input("which day: "))
        if which < date:
            message = advent(which)
        else:
            print("nice try")
    else:
        print("why did you asked then?")
