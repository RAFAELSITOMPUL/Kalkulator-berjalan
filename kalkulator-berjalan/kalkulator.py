class KalkulatorTransportasi:
    def __init__(self):
        # Daftar tarif transportasi umum
        self.tarif = {
            'bus': 5000,
            'kereta': 10000,
            'angkot': 3000,
            'metro': 7000
        }
    
    def hitung_biaya_perjalanan(self, jenis_transportasi, jarak):
        """
        Menghitung biaya perjalanan berdasarkan jenis transportasi dan jarak
        
        Args:
        - jenis_transportasi (str): Jenis transportasi yang digunakan
        - jarak (float): Jarak perjalanan dalam kilometer
        
        Returns:
        - float: Total biaya perjalanan
        """
        # Validasi jenis transportasi
        if jenis_transportasi.lower() not in self.tarif:
            return "Jenis transportasi tidak valid"
        
        # Ambil tarif dasar
        tarif_dasar = self.tarif[jenis_transportasi.lower()]
        
        # Hitung biaya berdasarkan jarak
        # Misal ada tambahan biaya per kilometer
        biaya_tambahan = jarak * 1000  # Rp 1000 per kilometer
        
        total_biaya = tarif_dasar + biaya_tambahan
        return total_biaya
    
    def tambah_tarif_baru(self, jenis_transportasi, tarif):
        """
        Menambahkan jenis transportasi baru beserta tarifnya
        
        Args:
        - jenis_transportasi (str): Nama jenis transportasi
        - tarif (int): Tarif dasar transportasi
        """
        self.tarif[jenis_transportasi.lower()] = tarif
        print(f"Tarif {jenis_transportasi} berhasil ditambahkan")
    
    def tampilkan_tarif(self):
        """
        Menampilkan daftar tarif transportasi yang tersedia
        """
        print("Daftar Tarif Transportasi:")
        for transportasi, tarif in self.tarif.items():
            print(f"{transportasi.capitalize()}: Rp {tarif}")

def main():
    # Membuat objek kalkulator
    kalkulator = KalkulatorTransportasi()
    
    while True:
        print("\n--- Kalkulator Perjalanan Transportasi Umum ---")
        print("1. Hitung Biaya Perjalanan")
        print("2. Tambah Tarif Baru")
        print("3. Lihat Daftar Tarif")
        print("4. Keluar")
        
        pilihan = input("Masukkan pilihan (1-4): ")
        
        if pilihan == '1':
            jenis = input("Masukkan jenis transportasi: ")
            try:
                jarak = float(input("Masukkan jarak perjalanan (km): "))
                biaya = kalkulator.hitung_biaya_perjalanan(jenis, jarak)
                print(f"Total biaya perjalanan: Rp {biaya}")
            except ValueError:
                print("Masukkan jarak dengan benar!")
        
        elif pilihan == '2':
            jenis = input("Masukkan jenis transportasi baru: ")
            try:
                tarif = int(input("Masukkan tarif dasar: "))
                kalkulator.tambah_tarif_baru(jenis, tarif)
            except ValueError:
                print("Masukkan tarif dengan benar!")
        
        elif pilihan == '3':
            kalkulator.tampilkan_tarif()
        
        elif pilihan == '4':
            print("Terima kasih telah menggunakan kalkulator!")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Jalankan program
if __name__ == "__main__":
    main()