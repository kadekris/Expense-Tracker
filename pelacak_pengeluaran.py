import csv
from datetime import datetime

class Pengeluaran:
    def __init__(self, id, deskripsi, jumlah, tanggal, kategori):
        self.id = id
        self.deskripsi = deskripsi
        self.jumlah = jumlah
        self.tanggal = tanggal
        self.kategori = kategori

class PelacakPengeluaran:
    def __init__(self):
        self.daftar_pengeluaran = []
        self.kategori = set()
        self.anggaran_bulanan = 0

    def tambah_pengeluaran(self, deskripsi, jumlah, kategori):
        id = len(self.daftar_pengeluaran) + 1
        tanggal = datetime.now().strftime("%Y-%m-%d")
        pengeluaran = Pengeluaran(id, deskripsi, jumlah, tanggal, kategori)
        self.daftar_pengeluaran.append(pengeluaran)
        self.kategori.add(kategori)
        print(f"Pengeluaran berhasil ditambahkan. ID: {id}")

    def perbarui_pengeluaran(self, id, deskripsi, jumlah, kategori):
        for pengeluaran in self.daftar_pengeluaran:
            if pengeluaran.id == id:
                pengeluaran.deskripsi = deskripsi
                pengeluaran.jumlah = jumlah
                pengeluaran.kategori = kategori
                self.kategori.add(kategori)
                print(f"Pengeluaran dengan ID {id} berhasil diperbarui.")
                return
        print(f"Pengeluaran dengan ID {id} tidak ditemukan.")

    def hapus_pengeluaran(self, id):
        for pengeluaran in self.daftar_pengeluaran:
            if pengeluaran.id == id:
                self.daftar_pengeluaran.remove(pengeluaran)
                print(f"Pengeluaran dengan ID {id} berhasil dihapus.")
                return
        print(f"Pengeluaran dengan ID {id} tidak ditemukan.")

    def lihat_pengeluaran(self, kategori=None):
        if not self.daftar_pengeluaran:
            print("Tidak ada pengeluaran yang ditemukan.")
            return

        pengeluaran_terfilter = self.daftar_pengeluaran
        if kategori:
            pengeluaran_terfilter = [p for p in self.daftar_pengeluaran if p.kategori == kategori]

        print("ID | Tanggal | Deskripsi | Jumlah | Kategori")
        print("-" * 50)
        for pengeluaran in pengeluaran_terfilter:
            print(f"{pengeluaran.id} | {pengeluaran.tanggal} | {pengeluaran.deskripsi} | Rp{pengeluaran.jumlah:.2f} | {pengeluaran.kategori}")

    def lihat_ringkasan(self):
        if not self.daftar_pengeluaran:
            print("Tidak ada pengeluaran yang ditemukan.")
            return

        total = sum(pengeluaran.jumlah for pengeluaran in self.daftar_pengeluaran)
        rata_rata = total / len(self.daftar_pengeluaran)
        print(f"Total pengeluaran: Rp{total:.2f}")
        print(f"Rata-rata pengeluaran: Rp{rata_rata:.2f}")
        print(f"Jumlah pengeluaran: {len(self.daftar_pengeluaran)}")

    def lihat_ringkasan_bulanan(self, bulan):
        tahun = datetime.now().year
        pengeluaran_bulanan = [p for p in self.daftar_pengeluaran if p.tanggal.startswith(f"{tahun}-{bulan:02d}")]
        
        if not pengeluaran_bulanan:
            print(f"Tidak ada pengeluaran yang ditemukan untuk bulan {bulan}.")
            return

        total = sum(pengeluaran.jumlah for pengeluaran in pengeluaran_bulanan)
        print(f"Total pengeluaran untuk bulan {bulan}: Rp{total:.2f}")
        print(f"Jumlah pengeluaran: {len(pengeluaran_bulanan)}")

        if self.anggaran_bulanan > 0:
            if total > self.anggaran_bulanan:
                print(f"Peringatan: Anda telah melebihi anggaran bulanan sebesar Rp{self.anggaran_bulanan:.2f}")
            else:
                sisa = self.anggaran_bulanan - total
                print(f"Sisa anggaran: Rp{sisa:.2f}")

    def atur_anggaran_bulanan(self, anggaran):
        self.anggaran_bulanan = anggaran
        print(f"Anggaran bulanan diatur menjadi Rp{anggaran:.2f}")

    def ekspor_ke_csv(self, nama_file):
        with open(nama_file, 'w', newline='') as csvfile:
            penulis = csv.writer(csvfile)
            penulis.writerow(['ID', 'Tanggal', 'Deskripsi', 'Jumlah', 'Kategori'])
            for pengeluaran in self.daftar_pengeluaran:
                penulis.writerow([pengeluaran.id, pengeluaran.tanggal, pengeluaran.deskripsi, pengeluaran.jumlah, pengeluaran.kategori])
        print(f"Pengeluaran diekspor ke {nama_file}")

def main():
    pelacak = PelacakPengeluaran()
    
    while True:
        print("\nMenu Pelacak Pengeluaran:")
        print("1. Tambah pengeluaran")
        print("2. Perbarui pengeluaran")
        print("3. Hapus pengeluaran")
        print("4. Lihat pengeluaran")
        print("5. Lihat ringkasan")
        print("6. Lihat ringkasan bulanan")
        print("7. Atur anggaran bulanan")
        print("8. Ekspor pengeluaran ke CSV")
        print("9. Keluar")
        
        pilihan = input("Masukkan pilihan Anda (1-9): ")
        
        if pilihan == '1':
            deskripsi = input("Masukkan deskripsi pengeluaran: ")
            jumlah = float(input("Masukkan jumlah pengeluaran: "))
            kategori = input("Masukkan kategori pengeluaran: ")
            pelacak.tambah_pengeluaran(deskripsi, jumlah, kategori)
        
        elif pilihan == '2':
            id = int(input("Masukkan ID pengeluaran yang akan diperbarui: "))
            deskripsi = input("Masukkan deskripsi baru: ")
            jumlah = float(input("Masukkan jumlah baru: "))
            kategori = input("Masukkan kategori baru: ")
            pelacak.perbarui_pengeluaran(id, deskripsi, jumlah, kategori)
        
        elif pilihan == '3':
            id = int(input("Masukkan ID pengeluaran yang akan dihapus: "))
            pelacak.hapus_pengeluaran(id)
        
        elif pilihan == '4':
            kategori = input("Masukkan kategori untuk filter (atau tekan Enter untuk semua): ")
            pelacak.lihat_pengeluaran(kategori if kategori else None)
        
        elif pilihan == '5':
            pelacak.lihat_ringkasan()
        
        elif pilihan == '6':
            bulan = int(input("Masukkan bulan (1-12): "))
            pelacak.lihat_ringkasan_bulanan(bulan)
        
        elif pilihan == '7':
            anggaran = float(input("Masukkan anggaran bulanan: "))
            pelacak.atur_anggaran_bulanan(anggaran)
        
        elif pilihan == '8':
            nama_file = input("Masukkan nama file untuk ekspor CSV: ")
            pelacak.ekspor_ke_csv(nama_file)
        
        elif pilihan == '9':
            print("Terima kasih telah menggunakan Pelacak Pengeluaran. Sampai jumpa!")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()