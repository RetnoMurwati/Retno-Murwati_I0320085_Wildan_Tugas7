#Tulis judul film yang disukai dengan kriteria :
#1. Judul harus diapit dengan tanda '-' dan minimal 30 karakter
#2. Huruf pertama harus huruf kapital
#3. Mencari banyaknya huruf yang sama dengan huruf pertama judul yang ditulis

#Input judul yang disukai
judul1 = input("Masukkan salah satu judul film yang Anda sukai :")

#huruf kapital pada huruf pertama
judul2 = judul1.capitalize()

#minimal 30 karakter dengan diapit tanda > dan <
judul3 = judul2.center(30, '-')
print(judul3)

#Banyaknya huruf a pada judul
print("Banyaknya huruf a :", judul2.find('a'))

