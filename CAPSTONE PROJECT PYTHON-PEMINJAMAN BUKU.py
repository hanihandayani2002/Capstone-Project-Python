#!/usr/bin/env python
# coding: utf-8

# #Selamat datang di Perpustakaan Pintar!
# Program ini merupakan aplikasi berbasis Python yang dibuat untuk mengelola peminjaman buku di perpustakaan secara sederhana dan efisien. Sistem berjalan di terminal dengan antarmuka menu yang interaktif dan mudah digunakan.
# 
# Menu Utama:
# 📋 Data Anggota
# 
# 📄 Daftar Keanggotaan
# 
# ❌ Hapus Data Anggota
# 
# 📚 Daftar Buku
# 
# ✏️ Kelola/Edit Data Buku
# 
# 📥 Peminjaman Buku
# 
# 📤 Pengembalian Buku
# 
# 📑 Data Transaksi Peminjaman
# 
# ❎ Exit
# 
# Dengan fitur ini, pengguna dapat mengelola anggota, buku, serta mencatat proses peminjaman dan pengembalian dengan lebih praktis.

# In[1]:


import pandas as pd


# In[2]:


pip install emoji


# In[3]:


anggota_perpus = [
    {"ID Anggota": 101, "Nama": "Hani Handayani", "Telepon": 6282178899021},
    {"ID Anggota": 102, "Nama": "Nilam", "Telepon": 6282140899021},
    {"ID Anggota": 103, "Nama": "Sephia", "Telepon": 6282198894022},
    {"ID Anggota": 104, "Nama": "Raka Pratama", "Telepon": 6285798891123},
    {"ID Anggota": 105, "Nama": "Salsa Maharani", "Telepon": 6281387629812},
    {"ID Anggota": 106, "Nama": "Dimas Saputra", "Telepon": 6281223345566},
    {"ID Anggota": 107, "Nama": "Ayu Lestari", "Telepon": 6289876543210},
    {"ID Anggota": 108, "Nama": "Fajar Nugroho", "Telepon": 6281212345678},
    # {"ID Anggota": 109, "Nama": "Tari Amelia", "Telepon": 6281912341234},
    # {"ID Anggota": 110, "Nama": "Galih Ramadhan", "Telepon": 6282299988776},
    # {"ID Anggota": 111, "Nama": "Indah Permata", "Telepon": 6285647382910},
    # {"ID Anggota": 112, "Nama": "Yoga Wicaksono", "Telepon": 6281398765432},
    # {"ID Anggota": 113, "Nama": "Melati Sari", "Telepon": 6281122233445},
    # {"ID Anggota": 114, "Nama": "Andi Hermawan", "Telepon": 6281556677889},
    # {"ID Anggota": 115, "Nama": "Citra Dewi", "Telepon": 6281225566778}
]


daftar_buku = [
    {"ID Buku": 1001, "Judul": "Dunia Shopie", "ISBN": "978-623-00-0001-1", "Genre": "Fiksi", "Stok": 2},
    {"ID Buku": 1002, "Judul": "Laskar Pelangi", "ISBN": "978-623-00-0002-2", "Genre": "Fiksi", "Stok": 5},
    {"ID Buku": 1003, "Judul": "Bumi", "ISBN": "978-623-00-0003-3", "Genre": "Fiksi", "Stok": 4},
    {"ID Buku": 1004, "Judul": "Perahu Kertas", "ISBN": "978-623-00-0004-4", "Genre": "Fiksi", "Stok": 3},
    {"ID Buku": 1005, "Judul": "Negeri 5 Menara", "ISBN": "978-623-00-0005-5", "Genre": "Fiksi", "Stok": 6},
    # {"ID Buku": 1006, "Judul": "Hujan", "ISBN": "978-623-00-0006-6", "Genre": "Fiksi", "Stok": 4},
    # {"ID Buku": 1007, "Judul": "Pulang", "ISBN": "978-623-00-0007-7", "Genre": "Fiksi", "Stok": 3},
    # {"ID Buku": 1008, "Judul": "Rindu", "ISBN": "978-623-00-0008-8", "Genre": "Fiksi", "Stok": 5},
    # {"ID Buku": 1009, "Judul": "Bulan", "ISBN": "978-623-00-0009-9", "Genre": "Fiksi", "Stok": 2},
    # {"ID Buku": 1010, "Judul": "Selamat Tinggal", "ISBN": "978-623-00-0010-0", "Genre": "Fiksi", "Stok": 4},
    {"ID Buku": 1011, "Judul": "Filosofi Teras", "ISBN": "978-623-00-0011-1", "Genre": "Non Fiksi", "Stok": 6},
    {"ID Buku": 1012, "Judul": "Sapiens", "ISBN": "978-623-00-0012-2", "Genre": "Non Fiksi", "Stok": 3},
    {"ID Buku": 1013, "Judul": "Atomic Habits", "ISBN": "978-623-00-0013-3", "Genre": "Non Fiksi", "Stok": 5},
    {"ID Buku": 1014, "Judul": "The Psychology of Money", "ISBN": "978-623-00-0014-4", "Genre": "Non Fiksi", "Stok": 4},
    {"ID Buku": 1015, "Judul": "Rich Dad Poor Dad", "ISBN": "978-623-00-0015-5", "Genre": "Non Fiksi", "Stok": 5}
]

# Wadah buku yang sedang dipinjam
buku_dipilih = []


# In[ ]:


print("\033[1m=== Selamat Datang di Perpustakaan Pintar! ===\n\033[0m")

# Fungsi-1 untuk menampilkan data anggota
def data_anggota():
    print("\n=== Data Anggota ===")
    df_data_anggota = pd.DataFrame(anggota_perpus)
    print(df_data_anggota)

#fungsi-2 menambah anggota baru
def daftar_anggota():
    Nama_anggota = input("Masukan Nama anggota: ")
    #nomor_anggota = int(input("masukan ID Anggota: "))
    nomor_anggota_baru = anggota_perpus[-1]['ID Anggota']+1
    nomor_telepon = input("Masukan Nomor Telepon 62 (13 digit): ")
    if len(nomor_telepon) !=13 :
      print("\033[91mNomor telepon yang anda masukan salah, nomor Telepon harus 13 digit\033[0m")
      return
    data_anggota_baru ={
        "ID Anggota" : nomor_anggota_baru,
        "Nama" : Nama_anggota,
        "Telepon" : nomor_telepon
    }
    anggota_perpus.append(data_anggota_baru)
    print(f"\033[92mAnda Berhasil Terdaftar Sebagai Anggota, dengan nomor anggota : {data_anggota_baru['ID Anggota']}\033[0m")

#fungsi-3 edit/kelola anggota
def edit_anggota():
    df_data_anggota = pd.DataFrame(anggota_perpus)
    print(df_data_anggota)
    id_hapus = int(input("Masukkan ID anggota yang ingin dihapus: "))
    for i, anggota in enumerate(anggota_perpus):
        if anggota["ID Anggota"] == id_hapus:
            del anggota_perpus[i]
            print("\033[92mData berhasil dihapus!\033[0m")
            return
    print("\033[91mID tidak ditemukan.\033[0m")

#fungsi-4 menampilkan daftar buku
def data_buku():
  print("\n=== Daftar Buku ===")
  df_daftar_buku = pd.DataFrame(daftar_buku)
  print(df_daftar_buku)



# fungsi-5 kelola/edit data buku
def edit_buku():
    df_daftar_buku = pd.DataFrame(daftar_buku)
    print(df_daftar_buku)

    while True:
        opsi = input("pilih opsi yang kamu inginkan (ketik hapus/tambah/keluar) : ")

        if opsi == 'keluar':
            break

        if opsi == 'hapus':
            id_hapus_buku = int(input("Masukan ID buku yang ingin dihapus: "))

            for i, buku in enumerate(daftar_buku):
                if buku["ID Buku"] == id_hapus_buku:
                    del daftar_buku[i]
                    print("\033[92mData berhasil dihapus!\033[0m")
                    break
            else:
                print("\033[91mID tidak ditemukan.\033[0m")
            break

        elif opsi == 'tambah':
            id_edit = daftar_buku[-1]['ID Buku'] + 1
            judul_buku = input("Masukan Judul Buku Baru: ")
            isbn_buku = input("Masukan ISBN Buku Baru: ")
            genre_buku = input("Masukan Genre Buku Baru: ")
            stok_buku = int(input("Masukan Stok Buku Baru: "))

            buku_baru = {
                "ID Buku": id_edit,
                "Judul": judul_buku,
                "ISBN": isbn_buku,
                "Genre": genre_buku,
                "Stok": stok_buku
            }

            daftar_buku.append(buku_baru)
            print("\033[92mBuku berhasil ditambahkan!\033[0m")
            break


# Fungsi untuk meminjam buku
def pinjam():
    id_peminjam = int(input("masukan ID Peminjam: "))
    for anggota in anggota_perpus:
        if anggota["ID Anggota"] == id_peminjam:
            print(f"ID Peminjam Ditemukan : {anggota['Nama']}")
            id_buku = int(input("masukan ID Buku yang kamu inginkan : "))
            for buku in daftar_buku:
                if buku["ID Buku"] == id_buku:
                    if buku["Stok"] > 0:
                        buku["Stok"] -= 1
                        buku_dipilih.append({
                            "ID Buku": id_buku,
                            "ID Peminjam": id_peminjam,
                            "Judul": buku["Judul"]
                        })
                        print(f"\033[92mBuku '{buku['Judul']}' berhasil dipinjam!\033[0m")
                        return
                    else:
                        print("\033[91m❌ Stok buku habis!\033[0m")
                        return
            print("\033[91m❌ ID Buku tidak ditemukan!\033[0m")
            return
    print("\033[91m❌ ID peminjam tidak ditemukan!\033[0m")



# Fungsi-7 untuk mengembalikan buku
def kembalikan_buku():
    id_peminjam = int(input("Masukkan ID Peminjam: "))
    for anggota in anggota_perpus:
        if anggota["ID Anggota"] == id_peminjam:
            print(f"\033[92mID peminjam ditemukan : {anggota['Nama']}\033[0m")
            break
    else:
        print("\033[91m❌ ID peminjam tidak ditemukan!\033[0m")
        return
    id_buku = int(input("Masukkan ID Buku yang ingin dikembalikan: "))
    for i, buku in enumerate(buku_dipilih):
        if buku["ID Buku"] == id_buku and buku["ID Peminjam"] == id_peminjam:
            print(f"\033[92m✅ Buku '{buku['Judul']}' berhasil dikembalikan!\033[0m")
            for item in daftar_buku:
                if item["ID Buku"] == id_buku:
                    item["Stok"] += 1
                    break
            buku_dipilih.pop(i)
            return
    else:
        print("\033[91m❌ ID peminjam tidak ditemukan!\033[0m")
        return
    print("\033[91m❌ Anda tidak pernah meminjam buku dengan ID tersebut!\033[0m")

def riwayat_peminjaman():
 print("\n=== Daftar Transaksi Peminjaman ===")
 df_buku_dipilih = pd.DataFrame(buku_dipilih)
 print(df_buku_dipilih)





while True:
  print(''' === Menu Utama ===
   1. 👥 Data Anggota
   2. 📝 Daftar Keanggotaan
   3. ✏️ Hapus Data Anggota
   4. 📖 Daftar Buku
   5. ✏️ Kelola/ Edit Data Buku
   6. 📦 Peminjaman Buku
   7. 🔁Pengembalian Buku
   8. 📦Data Transaksi Peminjaman
   9. ❌Exit ''')
  pilihan = input("Masukkan pilihan (1-9): ")

  if pilihan == '1':
     data_anggota()
  elif pilihan == '2' :
     daftar_anggota()
  elif pilihan == '3' :
     edit_anggota()
  elif pilihan == '4' :
     data_buku()
  elif pilihan == '5' :
     edit_buku()
  elif pilihan == '6' :
    pinjam()
  elif pilihan == '7' :
     kembalikan_buku()
  elif pilihan == '8' :
    riwayat_peminjaman()
  elif pilihan == '9':
       print("\033[94mTerima kasih sudah menggunakan Perpustakaan Pintar!\033[94m")
       break
  else:
      print("\033[91mAngka yang anda masukkan tidak sesuai, program yang anda jalankan salah!\033[0m")
      break


# In[ ]:




