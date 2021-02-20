# | USER |   PASSWORD  |
# -----------------------
# | bob  |     123     |
# | ann  |    pass123  |
# | mike | password123 |
# | liz  |    pass123  |

ODDELOVAC = 40 * "="
POMLCKA = 40 * "-"
UVITACI_VETA = "Welcome to the app,"
# Nas slovnik
data = {
    'uzivatel1': 'heslo',
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

# Zeptej se na uzivatelske jmeno a heslo
jmeno = input("Zadej jmeno: ")
heslo = input("Zadej heslo: ")

# Podminkovy vyraz
if data.get(jmeno) == heslo:
    print("Povolení pokračovat!")

else:
    print("Heslo, nebo uživatelské jméno je špatně!")
    exit()


nadrazeny_slovnik = dict()
text1 = {"text": "Situated about 10 miles west of Kemmerer, Fossil Butte is a ruggedly impressive topographic feature that rises sharply some 1000 feet above Twin Creek Valley to an elevation of more than 7500 feet above sea level. The butte is located just north of US 30N and the Union Pacific Railroad, which traverse the valley."}
text2 = {"text": "At the base of Fossil Butte are the bright red, purple, yellow and gray beds of the Wasatch Formation. Eroded portions of these horizontal beds slope gradually upward from the valley floor and steepen abruptly. Overlying them and extending to the top of the butte are the much steeper buff-to-white beds of the Green River Formation, which are about 300 feet thick."}
text3 = {"text": "The monument contains 8198 acres and protects a portion of the largest deposit of freshwater fish fossils in the world. The richest fossil fish deposits are found in multiple limestone layers, which lie some 100 feet below the top of the butte. The fossils represent several varieties of perch, as well as other freshwater genera and herring similar to those in modern oceans. Other fish such as paddlefish, garpike and stingray are also present."}

nadrazeny_slovnik[1] = text1
nadrazeny_slovnik[2] = text2
nadrazeny_slovnik[3] = text3

nadrazeny_slovnik = [0, text1, text2, text3]
soucet_textu = len(nadrazeny_slovnik[1::])
cislo_textu = int(input("Zadejte cislo textu: "))

if cislo_textu == 0:
    print("Cisla textu zacinaji od 1. Zkuste to znova.")
    cislo_textu = int(input("Zadejte cislo textu: "))
elif cislo_textu > soucet_textu:
    print("Tolik textu neni k dispozici. Zkuste to znova.")
    cislo_textu = int(input("Zadejte cislo textu: "))

else:
    nadrazeny_slovnik[cislo_textu]

jedno_cislo = cislo_textu
konecny_text = nadrazeny_slovnik[jedno_cislo]["text"]

text1 = konecny_text

texty = {}
vysledek_vybraneho_textu = konecny_text
slovnik1 = {}

texty['text1'] = slovnik1

p_slova1 = vysledek_vybraneho_textu.split()

slova1 = []

for word in p_slova1:
  slova1.append(word.strip('.,!:?'))

slovnik1['pocet_slov1'] = len(slova1)

# slova s prvnim velkym pismenem titlecase
VELKA_PRVNI_PISMENA = []
abeceda1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for word in slova1:
  if set(word[0]) <= set(abeceda1):
      VELKA_PRVNI_PISMENA.append(word)

slovnik1['VELKA_PRVNI_PISMENA'] = len(VELKA_PRVNI_PISMENA)
VELKAPISMENAPRVNIMISTO = slovnik1['VELKA_PRVNI_PISMENA']

# SLOVA S VELKYMI PISMENY uppercase

SLOVA_V_TEXTU_VELKA_VSECHNA_PISMENA = []
abeceda = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for word in slova1:
    if set(word) <= set('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        SLOVA_V_TEXTU_VELKA_VSECHNA_PISMENA.append(word)

slovnik1['SLOVA_V_TEXTU_VELKA_VSECHNA_PISMENA'] = len(SLOVA_V_TEXTU_VELKA_VSECHNA_PISMENA)
SLOVAVTEXTUVELKAVSECHNAPISMENA = slovnik1['SLOVA_V_TEXTU_VELKA_VSECHNA_PISMENA']

# slova malym pismenem lowercase
slova_malym_PISMEM = []

for word in slova1:
    if set(word) <= set('abcdefghijklmnopqrstuvwxyz'):
        slova_malym_PISMEM.append(word)

slovnik1['slova_malym_PISMEM'] = len(slova_malym_PISMEM)
malaPISMENAcelaSLOVA = slovnik1['slova_malym_PISMEM']

# celkovy pocet a soucet cisel v textu

jednicky1 = []
for word in slova1:
  if len(word) == 1:
    jednicky1.append(word)
slovnik1['pocet_slov_1'] = len(jednicky1)

dvojky1 = []
for word in slova1:
  if len(word) == 2:
    dvojky1.append(word)
slovnik1['pocet_slov_2'] = len(dvojky1)

trojky1 = []
for word in slova1:
  if len(word) == 3:
    trojky1.append(word)
slovnik1['pocet_slov_3'] = len(trojky1)

ctyrky1 = []
for word in slova1:
  if len(word) == 4:
    ctyrky1.append(word)
slovnik1['pocet_slov_4'] = len(ctyrky1)

petky1 = []
for word in slova1:
  if len(word) == 5:
    petky1.append(word)
slovnik1['pocet_slov_5'] = len(petky1)

sestky1 = []
for word in slova1:
  if len(word) == 6:
    sestky1.append(word)
slovnik1['pocet_slov_6'] = len(sestky1)

sedmicky1 = []
for word in slova1:
  if len(word) == 7:
    sedmicky1.append(word)
slovnik1['pocet_slov_7'] = len(sedmicky1)

osmicky1 = []
for word in slova1:
  if len(word) == 8:
    osmicky1.append(word)
slovnik1['pocet_slov_8'] = len(osmicky1)

devitky1 = []
for word in slova1:
  if len(word) == 9:
    devitky1.append(word)
slovnik1['pocet_slov_9'] = len(devitky1)

desitky1 = []
for word in slova1:
  if len(word) == 10:
    desitky1.append(word)
slovnik1['pocet_slov_10'] = len(desitky1)

jedenactky1 = []
for word in slova1:
  if len(word) == 11:
    jedenactky1.append(word)
slovnik1['pocet_slov_11'] = len(jedenactky1)

# --------------Po spuštění by program měl vypadat zhruba nějak takto-----------
print(ODDELOVAC)
print(" !FINALOVA VERZE PROJEKTU!")
print(ODDELOVAC)
print("username: ", jmeno)
print("password: ", heslo)
print(POMLCKA)
print(UVITACI_VETA, jmeno)
print("We have", soucet_textu ,"texts to be analyzed.")
print(POMLCKA)
print("Enter a number btw.", "1 and 3", "to select:", cislo_textu)
print(POMLCKA)
print("There are ", slovnik1['pocet_slov1'], "words in the selected text.")
print("There are", VELKAPISMENAPRVNIMISTO, "titlecase words.")
print("There are", SLOVAVTEXTUVELKAVSECHNAPISMENA, "uppercase words.")
print("There are", malaPISMENAcelaSLOVA, "lowercase words.")

celkovy_pocet_cisel_v_textu = p_slova1
def pocet_cisel(cislo_v_textu):
    return  len([int(i) for i in cislo_v_textu if type(i)== int or i.isdigit()])

print("There are", pocet_cisel(celkovy_pocet_cisel_v_textu), "numeric strings.")

celkovy_vysledek_cisel_v_textu = p_slova1
def pocet_cisel(cislo_v_textu):
    return  sum([int(i) for i in cislo_v_textu if type(i)== int or i.isdigit()])

print("The sum of all the numbers", pocet_cisel(celkovy_vysledek_cisel_v_textu))

print(POMLCKA)

#vysledek LEN|  OCCURENCES  | NR
print("LEN|  OCCURENCES  | NR.")
print(" 1", "|", slovnik1['pocet_slov_1'] * "*", "           |", slovnik1['pocet_slov_1'])
print(" 2", "|", slovnik1['pocet_slov_2'] * "*", "   |", slovnik1['pocet_slov_2'])
print(" 3", "|", slovnik1['pocet_slov_3'] * "*", "      |", slovnik1['pocet_slov_3'])
print(" 4", "|", slovnik1['pocet_slov_4'] * "*", " |", slovnik1['pocet_slov_4'])
print(" 5", "|", slovnik1['pocet_slov_5'] * "*", "|", slovnik1['pocet_slov_5'])
print(" 6", "|", slovnik1['pocet_slov_6'] * "*", "         |", slovnik1['pocet_slov_6'])
print(" 7", "|", slovnik1['pocet_slov_7'] * "*", "        |", slovnik1['pocet_slov_7'])
print(" 8", "|", slovnik1['pocet_slov_8'] * "*", "       |", slovnik1['pocet_slov_8'])
print(" 9", "|", slovnik1['pocet_slov_9'] * "*", "           |", slovnik1['pocet_slov_9'])
print("10", "|", slovnik1['pocet_slov_10'] * "*", "           |", slovnik1['pocet_slov_10'])
print("11", "|", slovnik1['pocet_slov_11'] * "*", "           |", slovnik1['pocet_slov_11'])
