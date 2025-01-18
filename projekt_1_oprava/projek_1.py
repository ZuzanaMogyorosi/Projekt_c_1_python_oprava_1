"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Zuzana Mogyorósi
email: zuzana.mogyorosi@gmail.com
discord: Zuzana M. - zuzanamogyorosi
"""

import task_template
import string

uzivatelske_jmeno = input("Zadejte vaše uživatelské jméno: \n")
uzivatelske_heslo = input("Zadejte vaše heslo: \n")

registrovani_uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
}

# kontrola přihlášení pomocí dict.get()
if registrovani_uzivatele.get(uzivatelske_jmeno) == uzivatelske_heslo:
    print("----------------------------------------")
    print(f"Vítejte {uzivatelske_jmeno}! Můžete analyzovat texty.")
    print("Máme 3 texty k analyzování.")
    print("----------------------------------------")

    print("Vyberte jeden z následujících textů:")
    print("1: Text 1")
    print("2: Text 2")
    print("3: Text 3")
    
    vyber = input("Zadejte číslo textu (1-3): \n")
    
    if vyber in ["1", "2", "3"]:
        vybrany_text = task_template.TEXTS[int(vyber) - 1]
    else:
        print("Neplatný výběr. Program bude ukončen.")
        exit()

    print("----------------------------------------")
    print("Zvolený text k analýze: \n")
    print(vybrany_text)
    
    slova = vybrany_text.split() # rozdělení textu na seznam slov podle mezer
    slova_ciste = [slovo.strip(string.punctuation) for slovo in slova] # očištění slov od interpunkce
    pocet_slov = len(slova_ciste) # spočítá slova
    pocet_slov_velke_pismeno = sum(1 for slovo in slova_ciste if slovo.istitle()) # počet slov začínajících velkým písmenem
    pocet_slov_velkymi_pismeny = sum(1 for slovo in slova_ciste if slovo.isupper()) # počet slov psaných velkými písmeny 
    pocet_slov_malymi_pismeny = sum(1 for slovo in slova_ciste if slovo.islower()) # počet slov psaných malými písmeny 
    
    # vyhledávání čísel
    pocet_cisel = 0
    soucet_cisel = 0

    for slovo in slova_ciste:
        if slovo.isdigit():
            pocet_cisel += 1
            soucet_cisel += int(slovo)

    
    # výpis výsledků analýzy
    print("Analýza textu: \n")
    print(f"Počet slov: {pocet_slov}")
    print(f"Počet slov začínajících velkým písmenem: {pocet_slov_velke_pismeno}")
    print(f"Počet slov psaných velkými písmeny: {pocet_slov_velkymi_pismeny}")
    print(f"Počet slov psaných malými písmeny: {pocet_slov_malymi_pismeny}")
    print(f"Počet čísel: {pocet_cisel}")
    print(f"Součet všech čísel: {soucet_cisel}")
    
    # výpočet četnosti délek slov
    delky_slov = [len(slovo) for slovo in slova_ciste]
    
    cetnost_delky = {}
    for delka in delky_slov:
        cetnost_delky[delka] = cetnost_delky.get(delka, 0) + 1
    
    # výpis grafu četnosti délek slov 
    print("-------------------------------------------------------")
    print("Zde je graf, který určuje počet slov se stejnou délkou.")
    print("-------------------------------------------------------")
    print("DÉLKA|VÝSKYTY             |POČET")
    print("-------------------------------------------------------")
    for delka in sorted(cetnost_delky):
        stars = '*' * cetnost_delky[delka]
        print(f"{delka:>5}|{stars:<20}|{cetnost_delky[delka]}")
    
else:
    # přihlášení neúspěšné
    print("Neregistrovaný uživatel nebo chybné heslo.")
