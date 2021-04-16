#Menghitung volume tabung :
# 1. Menggunakan tinggi maksimum yang dibulatkan ke bawah dari data
# 2. Menggunakan jari jari minimum yang dibulatkan ke bawah dari data yang ada
# 3. Hasil perhitungan dibulatkan ke atas

#Input tinggi dan jari jari tabung
t1 = float(input("Masukkan tinggi tabung pertama : "))
t2 = float(input("Masukkan tinggi tabung kedua : "))
t3 = float(input("Masukkan tinggi tabung ketiga : "))

r1 = float(input("Masukkan jari-jari pertama : "))
r2 = float(input("Masukkan jari-jari kedua : "))
r3 = float(input("Masukkan jari-jari ketiga : "))

#Menentukan tinggi maksimum dan jari jari minimum setelah dibulatkan
import math
t = max(t1,t2,t3)
tmaks = math.floor(t)
r = min(r1,r2,r3)
rmin = math.floor(r)

#Menghitung volume tabung
phi = 3.14
v = phi * (rmin ** 2) * tmaks

print('-----'*6)
#Hasil dibulatkan ke atas
print("\nVolume tabung =", math.ceil(v))
