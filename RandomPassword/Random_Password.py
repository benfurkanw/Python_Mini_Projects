import random

dosya_açma = open("dosya.txt" , "w")

harfler = "abcdefghijklmnpgrstuvwxyz"
büyük_harfler = "ABCDEFGHJKLMNOPGRSTUVWXYZ"
sayilar = "0123456789"
sembol = "*?/+!-_"

hepsi = harfler + büyük_harfler + sayilar + sembol
i = 0
while i <=10:
    password = "" .join(random.sample(hepsi,16))
    dosya_açma.write(password + "\n")
    i+=1