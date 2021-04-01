#Membuat program grading nilai
Nama = input("Masukkan nama Anda: ")
Nilai = int(input("Masukkan nilai Anda: "))
Hasil = "Hallo," + Nama + "! Nilai Anda setelah dikonversi adalah "

if 85 <= Nilai <= 100:
    print(Hasil,"A")
elif 80 <= Nilai <= 84:
    print(Hasil,"A-")
elif 75 <= Nilai <= 79:
    print(Hasil,"B+")
elif 70<= Nilai <= 74:
    print(Hasil,"B")
elif 65 <= Nilai <= 69:
    print(Hasil,"C+")
elif 60 <= Nilai <= 64:
    print(Hasil,"C")
elif Nilai < 60:
    print(Hasil,"E")
else:
    pass
print()