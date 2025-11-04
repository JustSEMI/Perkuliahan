import os

data = []
FILE_NAME   = "crud.txt"

def load_data():
    """Baca data dari file txt (jika ada)"""
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                if "," in line:
                    nama, alamat = line.strip().split(",", 1)
                    data.append({"nama": nama, "alamat": alamat})
    except FileNotFoundError:
        pass

def save_data():
    """Simpan data ke file txt"""
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for d in data:
            file.write(f"{d['nama']},{d['alamat']}\n")

def tampilkan_menu():
    print("\n===============================")
    print("        MENU UTAMA")
    print("===============================")
    print("1. Tambah data")
    print("2. Ubah data")
    print("3. Hapus data")
    print("4. Tampil data")
    print("5. Keluar")
    pilihan = input("Pilihlah no menu di atas: ")
    return pilihan

def tambah_data():
    print("\n--- TAMBAH DATA ---")
    nama = input("Masukkan nama: ")
    alamat = input("Masukkan alamat: ")
    data.append({"nama": nama, "alamat": alamat})
    save_data()
    print("✅ Data berhasil ditambahkan dan disimpan!")

def ubah_data():
    if not data:
        print("\n⚠️ Belum ada data untuk diubah.")
        return
    
    print("\n--- UBAH DATA ---")
    tampil_data()
    try:
        indeks = int(input("Pilih nomor data yang akan diubah: ")) - 1
        if 0 <= indeks < len(data):
            nama_baru = input("Masukkan nama baru: ")
            alamat_baru = input("Masukkan alamat baru: ")
            data[indeks]["nama"] = nama_baru
            data[indeks]["alamat"] = alamat_baru
            save_data()
            print("✅ Data berhasil diubah dan disimpan!")
        else:
            print("❌ Nomor data tidak valid.")
    except ValueError:
        print("❌ Input harus berupa angka.")

def hapus_data():
    if not data:
        print("\n⚠️ Belum ada data untuk dihapus.")
        return
    
    print("\n--- HAPUS DATA ---")
    tampil_data()
    try:
        indeks = int(input("Pilih nomor data yang akan dihapus: ")) - 1
        if 0 <= indeks < len(data):
            data.pop(indeks)
            save_data()
            print("✅ Data berhasil dihapus dan disimpan!")
        else:
            print("❌ Nomor data tidak valid.")
    except ValueError:
        print("❌ Input harus berupa angka.")

def tampil_data():
    print("\n--- DATA TERSIMPAN ---")
    if not data:
        print("Belum ada data.")
    else:
        for i, item in enumerate(data, start=1):
            print(f"{i}. {item['nama']} , {item['alamat']}")

load_data()

while True:
    pilihan = tampilkan_menu()
    
    if pilihan == "1":
        tambah_data()
    elif pilihan == "2":
        ubah_data()
    elif pilihan == "3":
        hapus_data()
    elif pilihan == "4":
        tampil_data()
    elif pilihan == "5":
        print("Program selesai.")
        break
    else:
        print("❌ Pilihan tidak valid, coba lagi.")