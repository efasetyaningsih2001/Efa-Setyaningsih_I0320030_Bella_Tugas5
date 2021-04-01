#Input nama dan jenis kelamin
Nama = input("Masukkan nama Anda: ")
JenisKelamin = input("Apakah jenis kelamin Anda (P/L): ")

if JenisKelamin == 'P':
    print("Selamat datang, Nyonya ", Nama, "!")
elif JenisKelamin == 'L':
    print("Selamat datang, Tuan ", Nama, "!")
else:
    pass
print()