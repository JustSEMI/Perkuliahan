def C_to_R(C):
    return C * 4/5
def C_to_F(C):
    return (C * 9/5) + 32
def C_to_K(C):
    return C + 273.15

def R_to_C(R):
    return R * 5/4
def R_to_F(R):
    return (R * 9/4) + 32
def R_to_K(R):
    return R * 5/4 + 273.15

def F_to_C(F):
    return (F - 32) * 5/9
def F_to_R(F):
    return (F - 32) * 4/9
def F_to_K(F):
    return (F - 32) * 5/9 + 273.15

def K_to_C(K):
    return K - 273.15
def K_to_R(K):
    return (K - 273.15) * 4/5
def K_to_F(K):
    return (K - 273.15) * 9/5 + 32

SATUAN_NAMA = {
    '1': "Celcius",
    '2': "Reamur",
    '3': "Fahrenheit",
    '4': "Kelvin"
}

def konversi_suhu():
    print("=============================================")
    print("WORKSHOP PEMROGRAMAN DASAR")
    print("SELAMAT DATANG DI PROGRAM KONVERSI SUHU")
    print("=============================================")
    print("MASUKAN SATUAN SUHU YANG AKAN DIKONVERSI")
    print("1. CELCIUS")
    print("2. REAMUR")
    print("3. FAHRENHEIT")
    print("4. KELVIN")

    satuan_awal_pilih = input(f"MASUKAN PILIHAN ANDA (1, 2, 3, ATAU 4) : ")

    if satuan_awal_pilih not in SATUAN_NAMA:
        print("Pilihan satuan awal tidak valid.")
        return

    satuan_awal_nama = SATUAN_NAMA[satuan_awal_pilih]
    
    print(f"\n=={satuan_awal_nama}==")
    
    try:
        suhu_awal = float(input(f"Suhu {satuan_awal_nama} = "))
    except ValueError:
        print("Input suhu tidak valid. Harap masukkan ANGKA.")
        return

    print("\nMAU DIUBAH KE SATUAN SUHU YANG MANA ?")

    pilihan_tujuan = {}
    i = 1
    for key, name in SATUAN_NAMA.items():
        if key != satuan_awal_pilih:
            print(f"{i}. {name}")
            pilihan_tujuan[str(i)] = key
            i += 1

    satuan_tujuan_pilih_idx = input("Pilih = ")
    
    if satuan_tujuan_pilih_idx not in pilihan_tujuan:
        print("Pilihan konversi tidak valid.")
        return

    satuan_tujuan_key = pilihan_tujuan[satuan_tujuan_pilih_idx]
    satuan_tujuan_nama = SATUAN_NAMA[satuan_tujuan_key]
    
    suhu_hasil = None

    if satuan_awal_pilih == '1':
        if satuan_tujuan_key == '2':
            suhu_hasil = C_to_R(suhu_awal)
        elif satuan_tujuan_key == '3':
            suhu_hasil = C_to_F(suhu_awal)
        elif satuan_tujuan_key == '4':
            suhu_hasil = C_to_K(suhu_awal)

    elif satuan_awal_pilih == '2':
        if satuan_tujuan_key == '1':
            suhu_hasil = R_to_C(suhu_awal)
        elif satuan_tujuan_key == '3':
            suhu_hasil = R_to_F(suhu_awal)
        elif satuan_tujuan_key == '4':
            suhu_hasil = R_to_K(suhu_awal)

    elif satuan_awal_pilih == '3':
        if satuan_tujuan_key == '1':
            suhu_hasil = F_to_C(suhu_awal)
        elif satuan_tujuan_key == '2':
            suhu_hasil = F_to_R(suhu_awal)
        elif satuan_tujuan_key == '4':
            suhu_hasil = F_to_K(suhu_awal)

    elif satuan_awal_pilih == '4':
        if satuan_tujuan_key == '1': 
            suhu_hasil = K_to_C(suhu_awal)
        elif satuan_tujuan_key == '2':
            suhu_hasil = K_to_R(suhu_awal)
        elif satuan_tujuan_key == '3':
            suhu_hasil = K_to_F(suhu_awal)
            
    if suhu_hasil is not None:
        print(f"\nSuhu {satuan_tujuan_nama} = {suhu_hasil}")

konversi_suhu()