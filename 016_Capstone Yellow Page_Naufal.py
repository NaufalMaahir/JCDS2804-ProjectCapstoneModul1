import os
from tabulate import tabulate
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

# Data kontak perusahaan (10 daftar)
kontak = [
    {"nama": "PT. Alpha", "telepon": "0211111111", "email": "contact@alpha.co.id",
     "alamat": "Jl. Alpha No.1", "daerah": "Jakarta", "industri": "Teknologi", "peran": "Penyedia Software"},
    {"nama": "PT. Beta", "telepon": "0222222222", "email": "info@beta.co.id",
     "alamat": "Jl. Beta No.2", "daerah": "Bandung", "industri": "Manufaktur", "peran": "Pabrik"},
    {"nama": "PT. Gamma", "telepon": "0313333333", "email": "sales@gamma.co.id",
     "alamat": "Jl. Gamma No.3", "daerah": "Surabaya", "industri": "Keuangan", "peran": "Bank"},
    {"nama": "PT. Delta", "telepon": "0414444444", "email": "support@delta.co.id",
     "alamat": "Jl. Delta No.4", "daerah": "Semarang", "industri": "Teknologi", "peran": "Penyedia IT"},
    {"nama": "PT. Epsilon", "telepon": "0515555555", "email": "info@epsilon.co.id",
     "alamat": "Jl. Epsilon No.5", "daerah": "Yogyakarta", "industri": "Pendidikan", "peran": "Lembaga Pendidikan"},
    {"nama": "PT. Zeta", "telepon": "0616666666", "email": "contact@zeta.co.id",
     "alamat": "Jl. Zeta No.6", "daerah": "Jakarta", "industri": "Teknologi", "peran": "Startup"},
    {"nama": "PT. Eta", "telepon": "0717777777", "email": "info@eta.co.id",
     "alamat": "Jl. Eta No.7", "daerah": "Bandung", "industri": "Manufaktur", "peran": "Supplier"},
    {"nama": "PT. Theta", "telepon": "0818888888", "email": "sales@theta.co.id",
     "alamat": "Jl. Theta No.8", "daerah": "Surabaya", "industri": "Keuangan", "peran": "Asuransi"},
    {"nama": "PT. Iota", "telepon": "0919999999", "email": "contact@iota.co.id",
     "alamat": "Jl. Iota No.9", "daerah": "Medan", "industri": "Energi", "peran": "Minyak & Gas"},
    {"nama": "PT. Kappa", "telepon": "0220000000", "email": "info@kappa.co.id",
     "alamat": "Jl. Kappa No.10", "daerah": "Jakarta", "industri": "Teknologi", "peran": "Startup"}
]

# Data kontak yang dihapus (recycle bin)
kontak_dihapus = []

def tampilkan_kontak(sort_by="terbaru", filter_daerah=None, filter_industri=None):
    if not kontak:
        return Fore.RED + "Tidak ada kontak." + Style.RESET_ALL
    data = kontak
    if filter_daerah:
        data = [k for k in data if k["daerah"].lower() == filter_daerah.lower()]
    if filter_industri:
        data = [k for k in data if k["industri"].lower() == filter_industri.lower()]
    if sort_by == "terbaru":
        data = list(reversed(data))
    elif sort_by == "terlama":
        data = data
    elif sort_by == "industri":
        data = sorted(data, key=lambda x: x["industri"].lower())
    elif sort_by == "daerah":
        data = sorted(data, key=lambda x: x["daerah"].lower())
    if not data:
        return Fore.RED + "Tidak ada kontak dengan kriteria tersebut." + Style.RESET_ALL
    tabel = [[i+1, k["nama"], k["telepon"], k["email"], k["alamat"], k["daerah"], k["industri"], k["peran"]]
             for i, k in enumerate(data)]
    return Fore.BLUE + tabulate(tabel, headers=["No", "Nama", "Telepon", "Email", "Alamat", "Daerah", "Industri", "Peran"], tablefmt="grid") + Style.RESET_ALL

def tambah_kontak(nama, telepon, email, alamat, daerah, industri, peran):
    # Validasi email sederhana
    if "@" not in email or "." not in email:
        return Fore.RED + "Format email tidak valid." + Style.RESET_ALL
    # Validasi nomor telepon: maksimal 13 digit
    if len(telepon) > 13:
        return Fore.RED + "Nomor telepon tidak valid, maksimal 13 digit." + Style.RESET_ALL
    kontak.append({
        "nama": nama, "telepon": telepon, "email": email,
        "alamat": alamat, "daerah": daerah, "industri": industri, "peran": peran
    })
    return Fore.GREEN + f"Kontak '{nama}' berhasil ditambahkan!" + Style.RESET_ALL

def cari_kontak(term):
    hasil = []
    for i, k in enumerate(kontak):
        if term.lower() in k["nama"].lower():
            hasil.append((i, k))
    return hasil

def cari_kontak_dihapus(term):
    hasil = []
    for i, k in enumerate(kontak_dihapus):
        if term.lower() in k["nama"].lower():
            hasil.append((i, k))
    return hasil

def hapus_kontak(term):
    hasil = cari_kontak(term)
    if not hasil:
        return Fore.RED + "Kontak tidak ditemukan." + Style.RESET_ALL
    if len(hasil) > 1:
        return Fore.RED + "Terlalu banyak hasil, spesifikkan nama lagi." + Style.RESET_ALL
    konfirmasi = input(f"Apakah Anda yakin ingin menghapus kontak '{hasil[0][1]['nama']}'? (y/n): ")
    if konfirmasi.lower() == 'y':
        kontak.remove(hasil[0][1])
        kontak_dihapus.append(hasil[0][1])
        return Fore.GREEN + f"Kontak '{hasil[0][1]['nama']}' berhasil dipindahkan ke daftar kontak dihapus!" + Style.RESET_ALL
    return Fore.RED + "Penghapusan dibatalkan." + Style.RESET_ALL

def tampilkan_kontak_dihapus():
    if not kontak_dihapus:
        return Fore.RED + "Daftar kontak dihapus kosong." + Style.RESET_ALL
    tabel = [[i+1, k["nama"], k["telepon"], k["email"], k["alamat"], k["daerah"], k["industri"], k["peran"]]
             for i, k in enumerate(kontak_dihapus)]
    return Fore.BLUE + tabulate(tabel, headers=["No", "Nama", "Telepon", "Email", "Alamat", "Daerah", "Industri", "Peran"], tablefmt="grid") + Style.RESET_ALL

def pulihkan_kontak(term):
    hasil = cari_kontak_dihapus(term)
    if not hasil:
        return Fore.RED + "Kontak tidak ditemukan dalam daftar kontak dihapus." + Style.RESET_ALL
    if len(hasil) > 1:
        return Fore.RED + "Terlalu banyak hasil, spesifikkan nama lagi." + Style.RESET_ALL
    konfirmasi = input(f"Apakah Anda yakin ingin memulihkan kontak '{hasil[0][1]['nama']}'? (y/n): ")
    if konfirmasi.lower() == 'y':
        kontak_dihapus.remove(hasil[0][1])
        kontak.append(hasil[0][1])
        return Fore.GREEN + f"Kontak '{hasil[0][1]['nama']}' berhasil dipulihkan!" + Style.RESET_ALL
    return Fore.RED + "Pemulihan dibatalkan." + Style.RESET_ALL

def hapus_permanen_kontak(term):
    hasil = cari_kontak_dihapus(term)
    if not hasil:
        return Fore.RED + "Kontak tidak ditemukan dalam daftar kontak dihapus." + Style.RESET_ALL
    if len(hasil) > 1:
        return Fore.RED + "Terlalu banyak hasil, spesifikkan nama lagi." + Style.RESET_ALL
    konfirmasi = input(f"Apakah Anda yakin ingin menghapus kontak '{hasil[0][1]['nama']}' secara permanen? (y/n): ")
    if konfirmasi.lower() == 'y':
        kontak_dihapus.remove(hasil[0][1])
        return Fore.GREEN + f"Kontak '{hasil[0][1]['nama']}' berhasil dihapus secara permanen!" + Style.RESET_ALL
    return Fore.RED + "Penghapusan permanen dibatalkan." + Style.RESET_ALL

def cari_dan_kelola_kontak():
    term = input("Masukkan kata kunci pencarian: ")
    hasil = cari_kontak(term)
    if not hasil:
        print(Fore.RED + "Kontak tidak ditemukan." + Style.RESET_ALL)
        return
    print("Hasil pencarian:")
    tabel = [[i+1, item[1]["nama"], item[1]["telepon"], item[1]["email"],
              item[1]["alamat"], item[1]["daerah"], item[1]["industri"], item[1]["peran"]]
             for i, item in enumerate(hasil)]
    print(Fore.BLUE + tabulate(tabel, headers=["No", "Nama", "Telepon", "Email", "Alamat", "Daerah", "Industri", "Peran"], tablefmt="grid") + Style.RESET_ALL)
    pilihan = input("Pilih nomor kontak untuk dikelola (atau tekan enter untuk batal): ")
    if not pilihan.strip():
        return
    try:
        pilihan = int(pilihan) - 1
        if pilihan < 0 or pilihan >= len(hasil):
            print(Fore.RED + "Pilihan tidak valid." + Style.RESET_ALL)
            return
    except ValueError:
        print(Fore.RED + "Input tidak valid." + Style.RESET_ALL)
        return
    idx, data = hasil[pilihan]
    print("1. Edit Kontak")
    print("2. Hapus Kontak")
    aksi = input("Pilih aksi: ")
    if aksi == "1":
        new_nama = input("Masukkan Nama baru (kosongkan jika tidak ingin mengubah): ") or None
        new_telepon = input("Masukkan Nomor Telepon baru (kosongkan jika tidak ingin mengubah): ") or None
        new_email = input("Masukkan Email baru (kosongkan jika tidak ingin mengubah): ") or None
        new_alamat = input("Masukkan Alamat baru (kosongkan jika tidak ingin mengubah): ") or None
        new_daerah = input("Masukkan Daerah baru (kosongkan jika tidak ingin mengubah): ") or None
        new_industri = input("Masukkan Industri baru (kosongkan jika tidak ingin mengubah): ") or None
        new_peran = input("Masukkan Peran baru (kosongkan jika tidak ingin mengubah): ") or None
        print(update_contact(idx, new_nama, new_telepon, new_email, new_alamat, new_daerah, new_industri, new_peran))
    elif aksi == "2":
        print(hapus_kontak(data["nama"]))
    else:
        print("Aksi dibatalkan.")

def menu_kontak_dihapus():
    while True:
        print("\nMenu Daftar Kontak Dihapus")
        print(tampilkan_kontak_dihapus())
        print("1. Pulihkan Kontak")
        print("2. Hapus Permanen Kontak")
        print("3. Kembali ke Menu Utama")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            term = input("Masukkan kata kunci kontak yang ingin dipulihkan: ")
            print(pulihkan_kontak(term))
        elif pilihan == "2":
            term = input("Masukkan kata kunci kontak yang ingin dihapus permanen: ")
            print(hapus_permanen_kontak(term))
        elif pilihan == "3":
            break
        else:
            print(Fore.RED + "Pilihan tidak valid." + Style.RESET_ALL)

def main():
    while True:
        bersihkan_layar()
        print("\nYellow Pages - Daftar Kontak Perusahaan")
        print("1. Lihat Kontak")
        print("2. Tambah Kontak")
        print("3. Cari dan Kelola Kontak")
        print("4. Daftar Kontak Dihapus")
        print("5. Keluar")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            print("1. Urutkan berdasarkan kontak terbaru")
            print("2. Urutkan berdasarkan kontak terlama")
            print("3. Urutkan berdasarkan industri")
            print("4. Urutkan berdasarkan daerah")
            print("5. Filter berdasarkan daerah dan industri")
            sort_choice = input("Pilih metode sorting/filter (default berdasarkan kontak terbaru): ")
            if sort_choice == "2":
                print(tampilkan_kontak("terlama"))
            elif sort_choice == "3":
                print(tampilkan_kontak("industri"))
            elif sort_choice == "4":
                print(tampilkan_kontak("daerah"))
            elif sort_choice == "5":
                daerah = input("Masukkan nama daerah: ")
                industri = input("Masukkan nama industri: ")
                print(tampilkan_kontak("terbaru", daerah, industri))
            else:
                print(tampilkan_kontak("terbaru"))
            input("Tekan Enter untuk melanjutkan...")
        elif pilihan == "2":
            nama = input("Masukkan Nama Perusahaan: ")
            telepon = input("Masukkan Nomor Telepon: ")
            email = input("Masukkan Email: ")
            alamat = input("Masukkan Alamat: ")
            daerah = input("Masukkan Daerah: ")
            industri = input("Masukkan Industri: ")
            peran = input("Masukkan Peran: ")
            print(tambah_kontak(nama, telepon, email, alamat, daerah, industri, peran))
            input("Tekan Enter untuk melanjutkan...")
        elif pilihan == "3":
            cari_dan_kelola_kontak()
            input("Tekan Enter untuk melanjutkan...")
        elif pilihan == "4":
            menu_kontak_dihapus()
            input("Tekan Enter untuk melanjutkan...")
        elif pilihan == "5":
            print("Terima kasih telah menggunakan Yellow Pages!")
            break
        else:
            print(Fore.RED + "Pilihan tidak valid, coba lagi." + Style.RESET_ALL)
            input("Tekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()
