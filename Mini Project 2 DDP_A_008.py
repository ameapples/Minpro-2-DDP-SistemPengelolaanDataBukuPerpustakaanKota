# Sistem Pengelolaan Data Buku Perpustakaan Kota

import os
import pwinput
from prettytable import PrettyTable

# Data Akun Pengguna

akun = {
    "admin": {
        "password": "admin123",
        "role": "Admin Perpustakaan"
    },
    "pengunjung": {
        "password": "pengunjung123",
        "role": "Pengunjung"
    }
}

# Data Buku Perpustakaan

data_buku = [
    ["B001", "Bumi", "Tere Liye", 2014],
    ["B002", "Laut Bercerita", "Leila S. Chudori", 2017],
    ["B003", "Sherlock Holmes", "Arthur Conan Doyle", 1887],
    ["B004", "Norwegian Wood", "Haruki Murakami", 1987]
]

# Function Login

def login():
    print("\n================================")
    print("        LOGIN PERPUSTAKAAN")
    print("================================")

    username = input("Username : ").strip().lower()
    password = pwinput.pwinput(
        prompt="Password : ",
        mask="*"
    )

    if username in akun:
        if akun[username]["password"] == password:
            print("\nLogin berhasil!")
            print("Selamat datang,", username)
            print("Role :", akun[username]["role"])

            return akun[username]["role"]
        else:
            print("Password salah!")
    else:
        print("Username tidak ditemukan!")

    return None

# Function Tampilkan Data Buku

def tampilkan_buku():
    print("\n================================")
    print("        DAFTAR DATA BUKU")
    print("================================")

    if len(data_buku) == 0:
        print("Belum ada data buku.")

    else:
        tabel = PrettyTable()

        tabel.field_names = [
            "Kode",
            "Judul",
            "Penulis",
            "Tahun"
        ]

        for buku in data_buku:
            tabel.add_row([
                buku[0],
                buku[1],
                buku[2],
                buku[3]
            ])

        print(tabel)

# Function Tambah Data Buku

def tambah_buku():
    print("\n================================")
    print("        TAMBAH DATA BUKU")
    print("================================")

    kode = input("Masukkan kode buku: ")

    if kode == "":
        print("Kode buku tidak boleh kosong!")
        return

    # Mengecek kode buku
    for buku in data_buku:
        if buku[0] == kode:
            print("Kode buku sudah digunakan!")
            return

    judul = input("Masukkan judul buku: ")

    if judul == "":
        print("Judul buku tidak boleh kosong!")
        return

    penulis = input("Masukkan nama penulis: ")

    if penulis == "":
        print("Nama penulis tidak boleh kosong!")
        return

    while True:
        try:
            tahun = int(input("Masukkan tahun terbit: "))

            if tahun > 0:
                break
            else:
                print("Tahun harus lebih dari 0!")

        except ValueError:
            print("Tahun harus berupa angka!")

    data_buku.append([
        kode,
        judul,
        penulis,
        tahun
    ])

    print("Data buku berhasil ditambahkan!")

# Function Ubah Data Buku

def ubah_buku():
    print("\n================================")
    print("         UBAH DATA BUKU")
    print("================================")

    kode = input(
        "Masukkan kode buku yang ingin diubah: "
    )

    ditemukan = False

    for buku in data_buku:

        if buku[0] == kode:
            ditemukan = True

            print("\nData ditemukan!")
            print("Judul lama   :", buku[1])
            print("Penulis lama :", buku[2])
            print("Tahun lama   :", buku[3])

            judul_baru = input(
                "Masukkan judul baru: "
            )

            if judul_baru == "":
                print("Judul tidak boleh kosong!")
                return

            penulis_baru = input(
                "Masukkan penulis baru: "
            )

            if penulis_baru == "":
                print("Penulis tidak boleh kosong!")
                return

            while True:
                try:
                    tahun_baru = int(
                        input("Masukkan tahun terbit baru: ")
                    )

                    if tahun_baru > 0:
                        break
                    else:
                        print(
                            "Tahun harus lebih dari 0!"
                        )

                except ValueError:
                    print(
                        "Tahun harus berupa angka!"
                    )

            buku[1] = judul_baru
            buku[2] = penulis_baru
            buku[3] = tahun_baru

            print("Data buku berhasil diubah!")
            break

    if not ditemukan:
        print(
            "Data buku dengan kode tersebut "
            "tidak ditemukan."
        )

# Function Hapus Data Buku

def hapus_buku():
    print("\n================================")
    print("         HAPUS DATA BUKU")
    print("================================")

    kode = input(
        "Masukkan kode buku yang ingin dihapus: "
    )

    ditemukan = False

    for buku in data_buku:

        if buku[0] == kode:
            ditemukan = True

            print("\nData buku ditemukan!")
            print("Kode    :", buku[0])
            print("Judul   :", buku[1])
            print("Penulis :", buku[2])
            print("Tahun   :", buku[3])

            konfirmasi = input(
                "Yakin ingin menghapus? (y/n): "
            )

            if konfirmasi.lower() == "y":
                data_buku.remove(buku)
                print("Data buku berhasil dihapus!")

            elif konfirmasi.lower() == "n":
                print("Data buku tidak jadi dihapus.")

            else:
                print(
                    "Pilihan tidak valid! "
                    "Masukkan y atau n."
                )

            break

    if not ditemukan:
        print(
            "Data buku dengan kode tersebut "
            "tidak ditemukan."
        )

# Menu Admin Perpustakaan

def menu_admin():
    while True:

        print("\n================================")
        print("    MENU ADMIN PERPUSTAKAAN")
        print("================================")
        print("1. Tambah Data Buku")
        print("2. Tampilkan Data Buku")
        print("3. Ubah Data Buku")
        print("4. Hapus Data Buku")
        print("5. Logout")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah_buku()

        elif pilihan == "2":
            tampilkan_buku()

        elif pilihan == "3":
            ubah_buku()

        elif pilihan == "4":
            hapus_buku()

        elif pilihan == "5":
            print("Berhasil logout.")
            break

        else:
            print(
                "Pilihan tidak valid! "
                "Silakan pilih 1-5."
            )


# Menu Pengunjung Perpustakaan

def menu_pengunjung():
    while True:

        print("\n================================")
        print("       MENU PENGUNJUNG")
        print("================================")
        print("1. Tampilkan Data Buku")
        print("2. Logout")

        pilihan = input("Pilih menu (1-2): ")

        if pilihan == "1":
            tampilkan_buku()

        elif pilihan == "2":
            print("Berhasil logout.")
            break

        else:
            print(
                "Pilihan tidak valid! "
                "Silakan pilih 1-2."
            )

# Function Jeda

def jeda():
    input("\nTekan Enter untuk melanjutkan...")

# Program Utama

def main():
    while True:
        try:
            os.system("cls" if os.name == "nt" else "clear")
            print("=" * 35)
            print("       PERPUSTAKAAN KOTA")
            print("=" * 35)
            print("1. Login")
            print("0. Keluar")
            pilihan = input("Pilih menu: ")

            os.system("cls" if os.name == "nt" else "clear")
            if pilihan == "1":
                role = login()

                if role == "Admin Perpustakaan":
                    menu_admin()

                elif role == "Pengunjung":
                    menu_pengunjung()

                else:
                    jeda()

            elif pilihan == "0":
                print("Program selesai. Terima kasih!")
                break

            else:
                print("Pilihan tidak valid! Silakan pilih 1 atau 0.")
                jeda()

        except (KeyboardInterrupt, EOFError):
            # Ctrl+C atau Ctrl+D ditekan: keluar dengan rapi
            print("\n\nProgram dihentikan. Terima kasih!")
            break

        except Exception as error:
            # Error lain yang tidak terduga: program tetap berjalan
            print("\nTerjadi kesalahan:", error)
            print("Kembali ke menu utama.")
            try:
                jeda()
            except (KeyboardInterrupt, EOFError):
                break


main()