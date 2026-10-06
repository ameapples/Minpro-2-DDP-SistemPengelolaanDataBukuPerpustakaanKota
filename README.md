# Sistem Pengelolaan Data Buku Perpustakaan Kota

Ini adalah program yang saya buat untuk mengelola data buku perpustakaan melalui terminal (CLI) menggunakan Python. Di program ini saya membuat sistem login dengan dua peran: **Admin Perpustakaan** yang bisa menambah, melihat, mengubah, dan menghapus data buku, serta **Pengunjung** yang hanya bisa melihat daftar buku.

> Nazwa Dwi Amelia Putri
> 
> NIM: 008
> 
> Mini Project 2 - Praktikum Dasar-Dasar Pemrograman (DDP) - Kelas A

---

## Daftar Isi

1. [Latar Belakang](#latar-belakang)
2. [Fitur](#fitur)
3. [Persyaratan & Instalasi](#persyaratan--instalasi)
4. [Cara Menjalankan](#cara-menjalankan)
5. [Akun Login](#akun-login)
6. [Struktur Data](#struktur-data)
7. [Penjelasan Kode Program](#penjelasan-kode-program)
8. [Flowchart](#flowchart)
9. [Validasi & Penanganan Error](#validasi--penanganan-error)

---

## Latar Belakang

Pencatatan buku di perpustakaan akan lebih rapi jika dilakukan lewat sistem, bukan manual. Karena itu saya membuat program sederhana yang memisahkan hak akses pengguna: admin bertugas mengelola data, sedangkan pengunjung hanya perlu melihat koleksi buku yang tersedia.

---

## Fitur

| Fitur | Admin | Pengunjung |
|---|:---:|:---:|
| Login dengan password tersamarkan (`*`) | Ya | Ya |
| Tampilkan data buku (tabel) | Ya | Ya |
| Tambah data buku | Ya | - |
| Ubah data buku | Ya | - |
| Hapus data buku (dengan konfirmasi) | Ya | - |
| Logout | Ya | Ya |

---

## Persyaratan & Instalasi

- Python 3.8 atau lebih baru
- Library eksternal yang saya gunakan:
  - [`pwinput`](https://pypi.org/project/pwinput/) untuk input password dengan masking karakter
  - [`prettytable`](https://pypi.org/project/prettytable/) untuk menampilkan data dalam bentuk tabel

Instalasi library:

```bash
pip install pwinput prettytable
```

Library `os` bawaan Python saya pakai untuk membersihkan layar terminal.

---

## Cara Menjalankan

```bash
python "Mini Project 2 DDP_A_008.py"
```

Menu utama akan tampil:

```
===================================
       PERPUSTAKAAN KOTA
===================================
1. Login
0. Keluar
```

---

## Akun Login

| Username | Password | Role |
|---|---|---|
| `admin` | `admin123` | Admin Perpustakaan |
| `pengunjung` | `pengunjung123` | Pengunjung |

Username tidak peka huruf besar/kecil (otomatis diubah ke huruf kecil dan spasi di tepi dihapus), sedangkan password peka huruf besar/kecil.

---

## Struktur Data

### `akun` (dictionary)

Saya menyimpan data akun dalam dictionary dengan username sebagai *key*. Setiap akun berisi `password` dan `role`.

```python
akun = {
    "admin": {"password": "admin123", "role": "Admin Perpustakaan"},
    "pengunjung": {"password": "pengunjung123", "role": "Pengunjung"}
}
```

### `data_buku` (list of list)

Setiap buku saya simpan sebagai list dengan urutan `[kode, judul, penulis, tahun]`.

```python
data_buku = [
    ["B001", "Bumi", "Tere Liye", 2014],
    ["B002", "Laut Bercerita", "Leila S. Chudori", 2017],
    ["B003", "Sherlock Holmes", "Arthur Conan Doyle", 1887],
    ["B004", "Norwegian Wood", "Haruki Murakami", 1987]
]
```

| Indeks | Isi | Tipe |
|:---:|---|---|
| 0 | Kode buku | `str` |
| 1 | Judul | `str` |
| 2 | Penulis | `str` |
| 3 | Tahun terbit | `int` |

> Data disimpan di memori, sehingga akan kembali ke data awal setiap program dijalankan ulang.

---

## Penjelasan Kode Program

### 1. Import Library

```python
import os
import pwinput
from prettytable import PrettyTable
```

- `os` saya gunakan untuk menjalankan perintah `cls` (Windows) atau `clear` (Linux/macOS).
- `pwinput` saya gunakan agar password yang diketik tampil sebagai `*`.
- `PrettyTable` saya gunakan untuk mencetak daftar buku dalam bentuk tabel yang rapi.

### 2. `login()`

Fungsi ini meminta username dan password, lalu memverifikasinya terhadap dictionary `akun`.

1. Username dibaca dengan `input(...).strip().lower()`.
2. Password dibaca dengan `pwinput.pwinput(prompt="Password : ", mask="*")`.
3. Jika username ada **dan** password cocok, fungsi mencetak pesan sukses dan **mengembalikan role** pengguna.
4. Jika username tidak ditemukan atau password salah, fungsi mencetak pesan kesalahan dan mengembalikan `None`.

### 3. `tampilkan_buku()`

Fungsi untuk menampilkan seluruh data buku.

- Jika `data_buku` kosong, tampil pesan "Belum ada data buku."
- Jika ada isi, saya membuat objek `PrettyTable` dengan kolom `Kode`, `Judul`, `Penulis`, `Tahun`, menambahkan tiap buku sebagai baris, lalu mencetak tabelnya.

### 4. `tambah_buku()`

Fungsi untuk menambah buku baru. Saya menerapkan validasi berikut secara berurutan:

1. **Kode** tidak boleh kosong dan tidak boleh sama dengan kode buku yang sudah ada.
2. **Judul** tidak boleh kosong.
3. **Penulis** tidak boleh kosong.
4. **Tahun** diminta berulang (`while True`) sampai pengguna memasukkan angka bulat lebih dari 0. Input non-angka ditangani dengan `try-except ValueError`.

Jika semua valid, buku ditambahkan dengan `data_buku.append([...])`. Jika ada validasi yang gagal, fungsi langsung `return` (proses dibatalkan).

### 5. `ubah_buku()`

Fungsi untuk mengubah data buku berdasarkan kode.

1. Pengguna memasukkan kode buku.
2. Program mencari kode tersebut di `data_buku` dengan perulangan `for`.
3. Jika ditemukan, data lama (judul, penulis, tahun) ditampilkan, lalu program meminta judul, penulis, dan tahun baru dengan validasi yang sama seperti fungsi tambah.
4. Nilai di dalam list diperbarui langsung (`buku[1]`, `buku[2]`, `buku[3]`). Kode buku sengaja tidak bisa diubah.
5. Jika kode tidak ditemukan (`ditemukan` tetap `False`), tampil pesan data tidak ditemukan.

### 6. `hapus_buku()`

Fungsi untuk menghapus buku berdasarkan kode.

1. Pengguna memasukkan kode buku.
2. Jika ditemukan, detail buku ditampilkan dan pengguna diminta konfirmasi `y/n`.
3. `y`: buku dihapus dengan `data_buku.remove(buku)`.
4. `n`: penghapusan dibatalkan.
5. Input lain: tampil pesan "Pilihan tidak valid!" dan tidak ada yang dihapus.
6. Jika kode tidak ditemukan, tampil pesan data tidak ditemukan.

Saya menambahkan konfirmasi ini agar data tidak terhapus karena salah ketik.

### 7. `menu_admin()`

Perulangan `while True` yang menampilkan menu admin dan memanggil fungsi sesuai pilihan:

| Pilihan | Aksi |
|:---:|---|
| 1 | `tambah_buku()` |
| 2 | `tampilkan_buku()` |
| 3 | `ubah_buku()` |
| 4 | `hapus_buku()` |
| 5 | Logout (`break`, kembali ke menu utama) |
| lainnya | Pesan "Pilihan tidak valid!" |

### 8. `menu_pengunjung()`

Menu untuk pengunjung dengan dua pilihan: `1` menampilkan data buku dan `2` logout. Pilihan lain menampilkan pesan tidak valid.

### 9. `jeda()`

Fungsi ini menahan layar dengan `input("Tekan Enter untuk melanjutkan...")` agar pesan sempat terbaca sebelum layar dibersihkan.

### 10. `main()`

Program utama dalam perulangan `while True`:

1. Membersihkan layar dan menampilkan menu utama (`1. Login`, `0. Keluar`).
2. Pilihan `1`: memanggil `login()`. Role yang dikembalikan menentukan menu: `"Admin Perpustakaan"` ke `menu_admin()`, `"Pengunjung"` ke `menu_pengunjung()`, selain itu (login gagal) ke `jeda()`.
3. Pilihan `0`: mencetak pesan penutup lalu keluar dari perulangan.
4. Pilihan lain: pesan tidak valid, lalu `jeda()`.
5. Seluruh isi perulangan saya bungkus dengan `try-except` (lihat bagian penanganan error).

Program dijalankan dengan memanggil `main()` di akhir file.

---

## Flowchart

Flowchart yang saya buat terbagi menjadi 8 bagian. Penghubung bernomor (lingkaran) dipakai untuk berpindah antar bagian:

> **Keterangan:** 1 = kembali ke menu utama, 2 = kembali ke menu admin, 3 = kembali ke menu pengunjung, 4 = lanjut ke baris berikutnya, 5 = menuju Jeda, 6 = menuju Selesai pada fungsi tersebut.

### 1. Alur Utama dan Login

Program dimulai dengan membersihkan layar dan menampilkan menu utama, lalu menerima input `1` atau `0`.

- Pilihan `1`: input username dan password. Jika username tidak ada, tampil "Username tidak ditemukan" lalu Jeda. Jika password tidak cocok, tampil "Password salah" lalu Jeda. Jika cocok, login berhasil dan role dicek: Admin menuju menu admin (bagian 2), Pengunjung menuju menu pengunjung (bagian 3), selain itu menuju Jeda.
- Pilihan `0`: tampil "Program selesai" lalu program berakhir.
- Pilihan lain: "Pilihan tidak valid", Jeda, lalu kembali ke menu utama.

### 2. Menu Admin

Menampilkan menu admin, menerima pilihan 1-5, lalu bercabang ke fungsi tambah (bagian 5), tampilkan (bagian 4), ubah (bagian 6), hapus (bagian 7), atau logout (kembali ke menu utama). Setelah tiap fungsi selesai, alur kembali ke menu admin. Pilihan di luar 1-5 menampilkan "Pilihan tidak valid" dan kembali ke menu admin.

### 3. Menu Pengunjung

Menampilkan menu pengunjung dan menerima pilihan 1-2: pilihan 1 menjalankan fungsi tampilkan buku (bagian 4), pilihan 2 logout ke menu utama, selain itu "Pilihan tidak valid" lalu kembali ke menu pengunjung.

### 4. Fungsi Tampilkan Data Buku

Mencetak judul "DAFTAR DATA BUKU", lalu mengecek apakah data kosong. Jika kosong, tampil "Data belum ada". Jika tidak, tabel diisi dari data dan dicetak, kemudian selesai.

### 5. Fungsi Tambah Buku

Alurnya: input kode, cek kosong, cek duplikat, input judul, cek kosong, input penulis, cek kosong, input tahun. Tahun diulang hingga berupa angka lebih dari 0 ("Tahun tidak valid!" mengembalikan alur ke input tahun). Setelah valid, buku ditambahkan ke `data_buku` dan tampil "Buku berhasil ditambahkan". Setiap kegagalan validasi (kode kosong, kode sudah digunakan, judul kosong, penulis kosong) langsung menuju Selesai.

### 6. Fungsi Ubah Buku

Alurnya: input kode, cek keberadaan kode, tampil data lama, input judul baru, cek kosong, input penulis baru, cek kosong, input tahun baru (diulang sampai valid), ubah data buku, lalu "Berhasil diubah". Jika kode tidak ada tampil "Data tidak ditemukan", dan validasi kosong langsung menuju Selesai.

### 7. Fungsi Hapus Buku

Alurnya: input kode, cek keberadaan, tampil data buku, input konfirmasi `y/n`. Jika `y`, data dihapus dari `data_buku` dan tampil "Berhasil dihapus". Jika `n`, tampil "Data tidak jadi dihapus". Jika selain itu, tampil "Pilihan tidak valid! Masukkan y atau n". Kode yang tidak ada menampilkan "Data tidak ditemukan".

### 8. Penanganan Error di Program Utama (try-except)

Jika terjadi error di `main()`: bila penyebabnya `Ctrl+C` / `Ctrl+D`, tampil "Program dihentikan. Terima kasih!" lalu selesai. Bila error lain, tampil "Terjadi kesalahan, kembali ke menu utama", dilanjutkan Jeda. Jika saat Jeda pengguna menekan `Ctrl+C` / `Ctrl+D`, program selesai; jika tidak, kembali ke menu utama.

---

## Validasi & Penanganan Error

| Situasi | Penanganan |
|---|---|
| Username tidak terdaftar | Pesan "Username tidak ditemukan!" |
| Password salah | Pesan "Password salah!" |
| Kode buku kosong / duplikat | Penambahan dibatalkan |
| Judul atau penulis kosong | Proses tambah/ubah dibatalkan |
| Tahun bukan angka atau <= 0 | Diminta mengulang input (`try-except ValueError`) |
| Kode buku tidak ditemukan (ubah/hapus) | Pesan data tidak ditemukan |
| Konfirmasi hapus selain `y`/`n` | Pesan tidak valid, tidak ada data dihapus |
| Pilihan menu tidak valid | Pesan tidak valid dan menu ditampilkan kembali |
| `Ctrl+C` / `Ctrl+D` | Program keluar dengan rapi |
| Error tak terduga | Pesan error ditampilkan, program kembali ke menu utama |

---

## Catatan

- Data buku bersifat sementara (disimpan di memori, tidak ke file/database).
- Kredensial akun saya tulis langsung di kode karena program ini dibuat untuk keperluan pembelajaran.

## Output Program dan Penjelasannya

### Output 1: Login Admin dan Tambah Data Buku

<img width="1366" height="768" alt="Screenshot (195)" src="https://github.com/user-attachments/assets/3535d540-3204-4b6a-8650-49f4178a62d3" />

```
================================
        LOGIN PERPUSTAKAAN
================================
Username : admin
Password : ********

Login berhasil!
Selamat datang, admin
Role : Admin Perpustakaan

================================
    MENU ADMIN PERPUSTAKAAN
================================
1. Tambah Data Buku
2. Tampilkan Data Buku
3. Ubah Data Buku
4. Hapus Data Buku
5. Logout
Pilih menu (1-5): 1

================================
        TAMBAH DATA BUKU
================================
Masukkan kode buku: B005
Masukkan judul buku: Dilan 1990
Masukkan nama penulis: Pidi Baiq
Masukkan tahun terbit: 2014
Data buku berhasil ditambahkan!
```

**Penjelasan:**
- Program diawali dengan layar login. Pengguna memasukkan username `admin` dan password yang tampil sebagai tanda bintang (`********`) agar tidak terlihat.
- Karena username dan password sesuai, program menampilkan pesan "Login berhasil!" beserta sapaan dan **role** pengguna, yaitu Admin Perpustakaan.
- Program lalu menampilkan **Menu Admin** yang berisi 5 pilihan: tambah, tampilkan, ubah, hapus, dan logout.
- Pengguna memilih menu **1** (Tambah Data Buku), kemudian mengisi kode `B005`, judul `Dilan 1990`, penulis `Pidi Baiq`, dan tahun terbit `2014`.
- Setelah data tersimpan, muncul pesan "Data buku berhasil ditambahkan!" dan program kembali menampilkan menu admin.

---

### Output 2: Tampilkan Data Buku dan Awal Proses Ubah Data

<img width="1366" height="768" alt="Screenshot (196)" src="https://github.com/user-attachments/assets/650a7074-cad8-4cb6-9cf4-39587c97c695" />

```
Pilih menu (1-5): 2

================================
        DAFTAR DATA BUKU
================================
+------+-----------------+-------------------+-------+
| Kode |      Judul      |      Penulis      | Tahun |
+------+-----------------+-------------------+-------+
| B001 |       Bumi      |     Tere Liye     |  2014 |
| B002 |  Laut Bercerita |  Leila S. Chudori |  2017 |
| B003 | Sherlock Holmes | Arthur Conan Doyle|  1887 |
| B004 |  Norwegian Wood |  Haruki Murakami  |  1987 |
| B005 |    Dilan 1990   |     Pidi Baiq     |  2014 |
+------+-----------------+-------------------+-------+

Pilih menu (1-5): 3

================================
         UBAH DATA BUKU
================================
Masukkan kode buku yang ingin diubah: B002

Data ditemukan!
Judul lama   : Laut Bercerita
Penulis lama : Leila S. Chudori
```

**Penjelasan:**
- Pengguna memilih menu **2** (Tampilkan Data Buku). Data ditampilkan dalam bentuk tabel dengan kolom Kode, Judul, Penulis, dan Tahun.
- Tabel berisi 5 buku (B001 sampai B005). Buku B005 *Dilan 1990* muncul, yang membuktikan proses tambah data pada Output 1 berhasil.
- Setelah kembali ke menu, pengguna memilih menu **3** (Ubah Data Buku) dan memasukkan kode `B002`.
- Program mencari kode tersebut. Karena ada, program menampilkan "Data ditemukan!" beserta data lama (judul dan penulis) sebagai acuan sebelum diubah.

---

### Output 3: Ubah Data Buku dan Awal Proses Hapus Data

<img width="1366" height="768" alt="Screenshot (197)" src="https://github.com/user-attachments/assets/7d1678cb-d1e9-46c2-b7e4-ecedf709ef49" />

```
================================
         UBAH DATA BUKU
================================
Masukkan kode buku yang ingin diubah: B002

Data ditemukan!
Judul lama   : Laut Bercerita
Penulis lama : Leila S. Chudori
Tahun lama   : 2017
Masukkan judul baru: Bumi Manusia
Masukkan penulis baru: Pramoedya Ananta Toer
Masukkan tahun terbit baru: 1980
Data buku berhasil diubah!

================================
    MENU ADMIN PERPUSTAKAAN
================================
1. Tambah Data Buku
2. Tampilkan Data Buku
3. Ubah Data Buku
4. Hapus Data Buku
5. Logout
Pilih menu (1-5): 4

================================
         HAPUS DATA BUKU
================================
Masukkan kode buku yang ingin dihapus: B005

Data buku ditemukan!
Kode    : B005
Judul   : Dilan 1990
Penulis : Pidi Baiq
Tahun   : 2014
Yakin ingin menghapus? (y/n): y
```

**Penjelasan:**
- Lanjutan proses ubah data: program menampilkan data lama lengkap (judul, penulis, dan tahun), lalu meminta data baru.
- Pengguna mengganti buku B002 menjadi judul `Bumi Manusia`, penulis `Pramoedya Ananta Toer`, tahun `1980`. Program menampilkan "Data buku berhasil diubah!".
- Setelah kembali ke menu admin, pengguna memilih menu **4** (Hapus Data Buku) dan memasukkan kode `B005`.
- Program menampilkan detail buku yang akan dihapus (kode, judul, penulis, tahun), lalu meminta **konfirmasi** `Yakin ingin menghapus? (y/n)`. Pengguna menjawab `y`. Konfirmasi ini mencegah data terhapus secara tidak sengaja.

---

### Output 4: Data Berhasil Dihapus

<img width="1366" height="768" alt="Screenshot (198)" src="https://github.com/user-attachments/assets/34010ebb-463f-4c79-90fa-835a8a314e51" />

```
Yakin ingin menghapus? (y/n): y
Data buku berhasil dihapus!

================================
    MENU ADMIN PERPUSTAKAAN
================================
1. Tambah Data Buku
2. Tampilkan Data Buku
3. Ubah Data Buku
4. Hapus Data Buku
5. Logout
Pilih menu (1-5):
```

**Penjelasan:**
- Karena pengguna menjawab `y`, program menghapus buku B005 dan menampilkan pesan "Data buku berhasil dihapus!".
- Program kembali menampilkan menu admin dan menunggu pilihan berikutnya. Ini menunjukkan menu berjalan dalam perulangan sampai pengguna memilih **5. Logout**.

---

### Output 5: Login Pengunjung

<img width="1366" height="768" alt="Screenshot (199)" src="https://github.com/user-attachments/assets/060ddeef-17f3-4e30-9fb4-6129c60218ea" />

```
================================
        LOGIN PERPUSTAKAAN
================================
Username : pengunjung
Password : *************

Login berhasil!
Selamat datang, pengunjung
Role : Pengunjung

================================
       MENU PENGUNJUNG
================================
1. Tampilkan Data Buku
2. Logout
Pilih menu (1-2): 1

================================
        DAFTAR DATA BUKU
================================
+------+-----------------+-----------------------+-------+
| Kode |      Judul      |        Penulis        | Tahun |
+------+-----------------+-----------------------+-------+
| B001 |       Bumi      |       Tere Liye       |  2014 |
| B002 |   Bumi Manusia  | Pramoedya Ananta Toer |  1980 |
| B003 | Sherlock Holmes |   Arthur Conan Doyle  |  1887 |
| B004 |  Norwegian Wood |     Haruki Murakami   |  1987 |
+------+-----------------+-----------------------+-------+

================================
       MENU PENGUNJUNG
================================
1. Tampilkan Data Buku
2. Logout
Pilih menu (1-2):
```

**Penjelasan:**
- Pengguna login dengan username `pengunjung`. Program mengenali role **Pengunjung** dan menampilkan menu yang berbeda dari admin.
- Menu Pengunjung hanya memiliki 2 pilihan: **Tampilkan Data Buku** dan **Logout**. Pengunjung tidak dapat menambah, mengubah, atau menghapus data (pembatasan hak akses berdasarkan role).
- Setelah memilih menu **1**, tabel buku ditampilkan dengan data terbaru: B002 sudah berubah menjadi *Bumi Manusia* karya Pramoedya Ananta Toer (1980), dan B005 sudah tidak ada karena telah dihapus oleh admin.
- Lebar kolom Penulis menyesuaikan otomatis dengan teks terpanjang, sehingga tabel tetap rapi.
- Setelah menampilkan data, program kembali ke menu pengunjung.
