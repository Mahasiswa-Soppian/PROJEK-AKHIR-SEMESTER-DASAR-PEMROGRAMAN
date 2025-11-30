"""PROGRAM PEMESANAN TIKET PESAWAT"""

# data maskapai, rute, kelas, harga, dan stok tiket
data_maskapai = {
    "Garuda Indonesia": { # key nama maskapai
        "data": { # key data rute
            "jakarta-bali": {
                "Eksekutif": { # key jenis kelas
                    "harga": 1500000, # value harga tiket
                    "stok": 50 # value stok tiket
                },
                "Bisnis": {
                    "harga": 1000000,
                    "stok": 100
                },
                "Ekonomi": {
                    "harga": 500000,
                    "stok": 200
                }
            },
            "jakarta-surabaya": {
                "Eksekutif": {
                    "harga": 1400000,
                    "stok": 40
                },
                "Bisnis": {
                    "harga": 900000,
                    "stok": 80
                },
                "Ekonomi": {
                    "harga": 450000,
                    "stok": 150
                }
            },
            "jakarta-medan": {
                "Eksekutif": {
                    "harga": 1600000,
                    "stok": 30
                },
                "Bisnis": {
                    "harga": 1100000,
                    "stok": 70
                },
                "Ekonomi": {
                    "harga": 550000,
                    "stok": 120
                }
            }
        }
    },
    "Lion Air": {
        "data": {
            "jakarta-bali": {
                "Eksekutif": {
                    "harga": 1500000,
                    "stok": 50
                },
                "Bisnis": {
                    "harga": 1000000,
                    "stok": 100
                },
                "Ekonomi": {
                    "harga": 500000,
                    "stok": 200
                }
            },
            "jakarta-surabaya": {
                "Eksekutif": {
                    "harga": 1400000,
                    "stok": 40
                },
                "Bisnis": {
                    "harga": 900000,
                    "stok": 80
                },
                "Ekonomi": {
                    "harga": 450000,
                    "stok": 150
                }
            }
        }
    }
}

garis = "=" * 40

pesanan = []

# function untuk menampilkan halaman utama program
def tampilan_utama():
    print(garis)
    print("\tSELAMAT DATANG DI WFLIGHT")
    print(garis)
    print("Menu yang kami sediakan:")
    print("1. Tampilkan Daftar Maskapai")
    print("2. Pesan Tiket")
    print("3. Lihat Pesanan")
    print("4. Cek Stock Tiket")
    print("5. Keluar Program")
    print(garis)

# function untuk menampilkan daftar maskapai
def lihat_maskapai():
    print(garis)
    print("\tDaftar Maskapai Tersedia")
    print(garis)

    # perulangan untuk mengambil data nama maskapai di Dicrionary data_maskapai
    for maskapai in data_maskapai:
        # menampilkan nama maskapai
        print(f"- Maskapai: {maskapai}")
    print(garis)

    # inputan pilihan user untuk menentukan keinginann user
    pilih = input("Ingin melihat detail maskapai? (Y/N): ").upper()

    # eksekusi pilihan user
    if pilih == "Y":
        print(garis)
        print("\tDetail Maskapai")

        # perulangan untuk mengambil data maskapai(nama maskapai, tujuan maskapai) di Dicrionary data_maskapai
        for maskapai, tujuan in data_maskapai.items(): # method items() digunakan untuk mengambil key dan value dari dictionary yang diinginkan
            print(garis)
            print (f"Maskapai: {maskapai}")
            print(garis)

            # perulangan untuk mengambil data rute dan kelas di dalam tujuan
            for rute, kelas in tujuan["data"].items():
                print(f"Rute: {rute}")

                for jenis_kelas, data in kelas.items():
                    print(f"- {jenis_kelas}: Rp. {data['harga']}")
        print(garis)
    elif pilih == "N":
        print("Kembali ke menu utama.\n")
        return                  # <-- kembali ke main_program() secara otomatis
    else:
        print("Pilihan tidak valid!\n")
        return lihat_maskapai()
    
    pesan = input("Pesan Sekarang? (Y/N): ").upper()

    if pesan == "Y":
        return pesan_tiket()    # <-- PANGGIL FITUR PESAN TIKET
    else:
        return                  # <-- kembali ke main_program() secara otomatis

# function untuk menampilkan form pemesanan tiket
def pesan_tiket():
    print(garis)
    print("\tForm Pemesanan Tiket")
    print(garis)

    asal = input("Masukkan kota asal: ").lower()
    tujuan = input("Masukkan kota tujuan: ").lower()

    rute_yang_dicari = f"{asal}-{tujuan}"

    maskapai_tersedia = []
    for maskapai, info_maskapai in data_maskapai.items():
        if rute_yang_dicari in info_maskapai["data"]:
            maskapai_tersedia.append(maskapai)

    print(garis)
    print("\tMaskapai yang Melayani Rute Ini:")
    print(garis)

    if not maskapai_tersedia:
        print("❌ Tidak ada maskapai yang melayani rute tersebut.")
        return

    for i, m in enumerate(maskapai_tersedia, 1):
        print(f"{i}. {m}")
    print(garis)


    # USER PILIH MASKAPAI
    pilihan_maskapai = int(input("Pilih maskapai (nomor): "))
    maskapai_dipilih = maskapai_tersedia[pilihan_maskapai - 1]

    kelas_dict = data_maskapai[maskapai_dipilih]["data"][rute_yang_dicari]

    print(garis)
    print(f"Maskapai: {maskapai_dipilih}")
    print(f"Rute: {rute_yang_dicari}")
    print("Jenis Kelas:")
    for kelas, data in kelas_dict.items():
        print(f"- {kelas} | Harga: Rp {data['harga']} | Stok: {data['stok']}")

    # USER PILIH KELAS
    pilihan_kelas = input("Pilih kelas: ")
    if pilihan_kelas not in kelas_dict:
        print("❌ Kelas tidak ditemukan.")
        return

    stok = kelas_dict[pilihan_kelas]["stok"]
    harga = kelas_dict[pilihan_kelas]["harga"]

    if stok <= 0:
        print("❌ Stok tiket habis.")
        return

    # USER INPUT JUMLAH TIKET
    jumlah_tiket = int(input("Masukkan jumlah tiket: "))

    if jumlah_tiket > stok:
        print("❌ Stok tidak mencukupi.")
        return

    print(garis)
    print("\tInput Data Penumpang")
    print(garis)

    # LOOP INPUT DATA PENUMPANG (SESUAI JUMLAH TIKET YANG DIINPUT USER)
    data_penumpang = []
    sisa = jumlah_tiket

    while sisa > 0:
        print(f"Penumpang ke-{jumlah_tiket - sisa + 1}:")
        nama = input("Nama: ")
        nik = input("NIK: ")
        hp = input("No HP: ")

        data_penumpang.append({
            "nama": nama,
            "nik": nik,
            "hp": hp
        })

        sisa -= 1
        print(f"Sisa tiket yang harus diisi: {sisa}\n")

    # HITUNG TOTAL
    total_harga = harga * jumlah_tiket
    print(garis)
    print(f"Total Harga: Rp {total_harga}")
    konfirmasi = input("Konfirmasi pemesanan? (Y/N): ").upper()

    if konfirmasi != "Y":
        print("❌ Pemesanan dibatalkan.")
        return

    # UPDATE STOK DAN SIMPAN PESANAN
    kelas_dict[pilihan_kelas]["stok"] -= jumlah_tiket

    pesanan.append({
        "maskapai": maskapai_dipilih,
        "rute": rute_yang_dicari,
        "kelas": pilihan_kelas,
        "harga": harga,
        "jumlah_tiket": jumlah_tiket,
        "data_penumpang": data_penumpang,
        "total": total_harga
    })

    print("✅ Pemesanan berhasil!")
    print("Kembali ke menu utama...\n")

# function untuk menampilkan pesanan yang telah dibuat
def lihat_pesanan():
    print(garis)
    print("\tDaftar Pesanan Tiket")
    print(garis)

    if len(pesanan) == 0:
        print("Tidak ada pesanan yang tersimpan.")
        print("Silakan pesan tiket terlebih dahulu.\n")
        return

    # Menampilkan semua pesanan
    for i, p in enumerate(pesanan, 1):
        print(f"Pesanan #{i}")
        print(f"Maskapai       : {p['maskapai']}")
        print(f"Rute           : {p['rute']}")
        print(f"Kelas          : {p['kelas']}")
        print(f"Harga Per Tiket: Rp {p['harga']}")
        print(f"Jumlah Tiket   : {p['jumlah_tiket']}")
        print(f"Total Harga    : Rp {p['total']}")
        print("-" * 40)
        print("Data Penumpang:")

        # Loop daftar penumpang
        for j, penumpang in enumerate(p["data_penumpang"], 1):
            print(f"Penumpang {j}:")
            print(f"Nama : {penumpang['nama']}")
            print(f"NIK  : {penumpang['nik']}")
            print(f"HP   : {penumpang['hp']}")
            print()

        print(garis)

    input("Tekan Enter untuk kembali ke menu...")  # jeda agar tidak langsung kembali
    return

# function untuk menampilkan stock tiket maskapai
def stock_tiket():
    print(garis)
    print("\tCek Stock Tiket Maskapai")
    print(garis)

    for maskapai, info_maskapai in data_maskapai.items():
        print(f"Maskapai: {maskapai}")
        for rute, kelas in info_maskapai["data"].items():
            print(f" Rute: {rute}")
            for jenis_kelas, data in kelas.items():
                print(f"  - {jenis_kelas}: Stok {data['stok']}")
        print(garis)

    input("Tekan Enter untuk kembali ke menu...")  # jeda agar tidak langsung kembali
    return


# function untuk menjalankan program 
def main_program():
    while True: 
        tampilan_utama()
        pilihan = int(input("Pilih menu (1-5): "))
        if pilihan == 1:
            lihat_maskapai()
        elif pilihan == 2:
            pesan_tiket()
        elif pilihan == 3:
            lihat_pesanan()
        elif pilihan == 4:
            stock_tiket()
        elif pilihan == 5:
            print("Terima kasih telah menggunakan WFLIGHT. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

main_program()