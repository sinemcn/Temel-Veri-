"""
Problem 1
Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini format metoduyla yapmaya çalışın.

Problem 2
Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)

Problem 3
Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.

Problem 4
Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.

Problem 5
Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.

Problem 6
Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.

Hipotenüs Formülü: a^2 + b^2 = c^2

"""

# Cevaplar

# 1-
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

çarpım = a * b * c

print("{} * {} * {} = {}".format(a,b,c,çarpım))

# 2-
boy = float(input("boy: "))
kilo = int(input("kilo: "))

print("Beden kitle indeksi: ",kilo / boy ** 2)

# 3-

yakan_miktar = float(input("Kilometrede yakan miktar: "))
kilometre = int(input("Kaç kilometre yaptınız: "))
print("Tutar: {}".format(yakan_miktar * kilometre))

# 4-
ad = input("Adınız: ")
soyad = input("Soyadınız: ")
numara = input("Numaranız: ")
print("{}\n{}\n{}".format(ad, soyad, numara))

# 5-
a = int(input("a: "))
b = int(input("b: "))

print("Değiştirilmeden önceki değerler\na: {} b: {}\n".format(a,b))

a,b = b,a

print("Değiştirildikten sonraki değerler\na: {} b: {}\n".format(a,b))

# 6-
a = int(input("a: "))
b = int(input("b: "))

c = (a**2 + b**2) ** 0.5

print("Hipotenüs :",c)