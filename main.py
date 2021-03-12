# 1. Sukurti 4 skirtingus data tipus.

data1 = True
data2 = 5
data3 = "hello"
data4 = 5.5

# 2. Sukurti 3 skirtingas data struktūras su minimum 3 įrašais ir atvaizduoti kiekvieną struktūrą į atskira eilute.

def structure1():
    print("hello1")
    print("hello2")
    print("hello3")

structure1()

# 3. Kokiu stilium rašomi kintamūjų pavadinimai iš dviejų ar daugiau žodžių python'e? pvz: MANO_KINTAMASIS = 1, Mano_Kintamasis = 2 ir t.t.

#Rašomi su apatiniu brūkšniu

# 4. Kaip sukurti kintamajį reprezentuojantį float data tipą?

task4 = float(5.5)

# 5. Parašyti funkcija kuri visada išprintins visus įrašus po vieną iš sarašo padavus bet kokį sarašą kaip parametrą.

list1 = [5, "hello", 6, True]

def task5(list):
    for x in list:
        print(x)

task5(list1)
# 2 Dalis:
#
# 6. Kokias reikšmes turės x ir y kintamieji?
# kintamasis = "IlgasSakinys"
# x = kintamasis[2:5]
# y = kintamasis[7:9]

# X turės gasS
# Y turės kin

# 7. Kuo skiriasi mutable nuo not mutable data strukturos?



# 8. Jeigu norėtumėm patobulinti mūsų funkcija kuri išspauzdina sarašo įrašus žinant, kad type(kintamasis) gražina kintamojo data tipą parašyti funkcija kuri patikrina ar parametras funkcijoje yra list ar dictionary ir išspauzdinti kiekvieną įrašą į atskira eilute.

listt = [1,5,6,7]
dictionary = {"test1": "test2", "test3": "test4"}

print(type(test1))

def task8(check):
    if type(check) == list:
        for i in check:
            print(i)
    elif type(check) == dict:
        for i,v in check.items():
            print(i,v)
    else:
        print("data tipas nera list arba dictionary")

task8(listt)