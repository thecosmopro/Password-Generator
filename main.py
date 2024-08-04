import random

#Kullanıcının parolasının içerebileceği tüm karakterleri içeren bir değişken oluşturun
karakter_deposu = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

#Bir değişken oluşturun ve kullanıcıdan parolanın uzunluğunu girmesini isteyin
uzunluk = int(input("Parolanın uzunluğunu gir:"))

#Programın oluşturulan parolayı saklayacağı bir değişken oluşturun
parola = ""

#uzunluk kadar döngü
for i in range(uzunluk):
    #karakter depomuzdan rastgele bir karakter seçilecek
    karakter = random.choice(karakter_deposu)
    #Seçilen rastgele elemanı parola değişkenine ekleme
    parola += karakter

#Parolayı Yaz
print(parola)