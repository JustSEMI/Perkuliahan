def tambah(x, y):
    return x + y
def kurang(x, y):
    return x - y
def kali(x, y):
    return x * y
def bagi(x, y):
    return x / y

while True:
    print(f"=================================================")
    print(f"WORKSHOP PEMROGRAMAN DASAR")
    print(f"SELAMAT DATANG DI PROGRAM KALKULATOR SEDERHANA")
    print(f"=================================================")
    print(f"PILIH OPERASI YANG DIINGINKAN")
    print(f"1. Penjumlahan")
    print(f"2. Pengurangan")
    print(f"3. Perkalian")
    print(f"4. Pembagian")
    print(f"5. Keluar")
    print(f"=================================================")

    pilihan = input("Silahkan masukan pilihan Anda ( 1, 2, 3, 4, atau 5 ) : ")
    if pilihan == '5':
        print("Terima kasih! Program selesai.")
        break
    if pilihan not in ['1', '2', '3', '4']:
        print(f"Maaf, opsi yang anda masukkan salah ('{pilihan}'). Silakan pilih 1-5.")
        continue 

    try:
        bil1 = float(input("Masukkan bilangan pertama: "))
        bil2 = float(input("Masukkan bilangan kedua: "))
    except ValueError:
        print("Input tidak valid. Harap masukkan ANGKA, bukan huruf.")
        continue


    if pilihan == '1':
        print(f"Hasil: {bil1} + {bil2} = {tambah(bil1, bil2)}")
        break
    elif pilihan == '2':
        print(f"Hasil: {bil1} - {bil2} = {kurang(bil1, bil2)}")
        break
    elif pilihan == '3':
        print(f"Hasil: {bil1} * {bil2} = {kali(bil1, bil2)}")
        break
    elif pilihan == '4':
        if bil2 == 0:
            print("Error: Tidak bisa melakukan pembagian dengan nol.")
        else:
            print(f"Hasil: {bil1} / {bil2} = {bagi(bil1, bil2)}")
        break