from math import gcd

class Fraction:
    """
    class Fraction untuk merepresentasikan pecahan
    """
    def __init__(self, numerator, denominator):
        """
        membuat objek Fraction dengan pembilang dan penyebut
        :param numerator: Pembilang pecahan
        :param denominator: Penyebut pecahan
        """
        if denominator == 0:
            raise ValueError("Denominator tidak boleh 0")

        # Variabel untuk menyimpan pecahan asli
        self.original_num = numerator
        self.original_den = denominator

        # Variabel untuk menyimpan pecahan yang disederhanakan
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def simplify(self):
        """
        Menyederhanakan pecahan otomatis dengan cara FPB
        """
        pembagi = gcd(self.numerator, self.denominator)
        self.numerator //= pembagi
        self.denominator //= pembagi

        # untuk memastikan penyebut selalu positif dan tidak nol dan negetif
        if self.denominator == 0:
            raise ValueError("Denominator tidak boleh 0")
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    def __add__(self, other):
        """
        Menjumlahkan dua pecahan
        dengan rumus: (a/b) + (c/d) = (a*d + b*c) / (b*d)
        """
        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        """
        Mengurangkan dua pecahan
        dengan rumus: (a/b) - (c/d) = (a*d - b*c) / (b*d)
        """
        new_num = self.numerator * other.denominator - other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def to_float(self):
        """
        Mengubah pecahan menjadi bilangan desimal
        dengan rumus: a/b
        """
        return self.numerator / self.denominator

    def __str__(self):
        """
        Tampilkan dalam bentuk sederhana
        """
        return f"{self.numerator}/{self.denominator}"

    def original_str(self):
        """
        Tampilkan bentuk asli (sebelum disederhanakan)
        """
        return f"{self.original_num}/{self.original_den}"


def main():
    """
    Fungsi utama pada kalkulator pecahan ini yang berbasis input dari user
    dengan memakuskan dua pecahan dan melakukan operasi penjumlahan atau pengurangan
    sesuai pilihan user.
    Hasilnya akan ditampilkan dalam bentuk pecahan sederhana dan nilai desimal.
    """
    print("=== Kalkulator Pecahan ===")
    try:
        # Input user pecahan pertama
        n1 = int(input("Masukkan pembilang pecahan pertama: "))
        d1 = int(input("Masukkan penyebut pecahan pertama: "))
        f1 = Fraction(n1, d1)

        # Input user pecahan kedua
        n2 = int(input("\nMasukkan pembilang pecahan kedua: "))
        d2 = int(input("Masukkan penyebut pecahan kedua: "))
        f2 = Fraction(n2, d2)

        # menampilkan bentuk asli & sederhana dari pecahan yang user inpu
        print("\nPecahan pertama : ", f1.original_str(), "→ ", f1)
        print("Pecahan kedua   : ", f2.original_str(), "→ ", f2)

        # user di minta memilih operasi antara penjumlahan atau pengurangan
        print("\nPilih operasi:")
        print("1. Penjumlahan (+)")
        print("2. Pengurangan (-)")
        pilihan = input("Masukkan pilihan (1/2): ")

        # Melakukan operasi sesuai pilihan user
        if pilihan == "1":
            hasil = f1 + f2
            operasi = "+"
        elif pilihan == "2":
            hasil = f1 - f2
            operasi = "-"
        else:
            print("Pilihan tidak valid.")
            return

        # Menampilkan hasil operasi
        print("\n=== Hasil Operasi ===")
        print(f"\nHasil: {f1} {operasi} {f2} = {hasil}")
        print(f"Nilai desimal: {hasil.to_float():.4f}")

    except ValueError as e:
        print("Error:", e)

# ini fungsi utama untuk menjalankan kalkulator pecahan
# jika file ini dijalankan secara langsung
if __name__ == "__main__":
    main()