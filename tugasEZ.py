#soal 1 usia dewasa
umur_andi = 16
if umur_andi < 18 :
    print("jeh bayekk")
else :
    print("bayi tuwoo")

#soal 2 nilai lulus
nilai_dina = 85
if nilai_dina >= 70 :
    print("cie lulus")
else :
    print("wakwokawka gagal")

#soal 3 uang cukup
uang_ani = 45000
harga_buku = 50000
kurang_uang = harga_buku - uang_ani

if uang_ani >= harga_buku :
    print(f"gass tumbas bukune rego {harga_buku}")
else :
    print(f"johhh kadung exited jebul kurang {kurang_uang}")

#soal 4 juara kelas
avg_fajar = 92
if avg_fajar >= 90 :
    print("wikike juara kelas")
else :
    print("nt masbroo belajar maneh")

#soal 5 kecepatan aman
vcar = 85
if vcar > 80 :
    print("cah kae pengen dijemput yang mahakuasa ketoke")
else :
    print("cekelen aku pak polisii, aku tanpamu ngisingku abot")


# umur = int(input("Masukkan umur Anda: "))
# if umur < 10:
#     print("Anak-anak")
# elif umur <= 19:
#     print("Remaja")
# else:
#     print("Dewasa")









#1 Program Penentuan Kategori Usia dan Status Pelajar 
# nama = str(input("Masukkan nama Anda: "))
# umur = int(input("Masukkan umur Anda: "))
# status_pelajar = str(input("Pelajar/ bukan Pelajar ?"))

# if umur < 18 :
#    if status_pelajar.lower() == "pelajar":
#         print(f"{nama}, Anda Pelajar di bawah umur.")
#    else:
#         print(f"{nama}, Anda Bukan Pelajar di bawah umur.")
# elif umur >= 18 :
#     if status_pelajar.lower() == "pelajar":
#         print(f"{nama}, Anda Pelajar Dewasa.")
#     else:
#         print(f"{nama}, Anda Bukan Pelajar Dewasa.")
# else:
#     print("Input status pelajar tidak valid.")

# #2 toko online memberi diskon 
# nama_pelanggan = str(input("Masukkan nama pelanggan: "))
# jenis_pelanggan = str(input("Masukkan jenis pelanggan (reguler/silver/gold): "))
# total_belanja = float(input("Masukkan total belanja: "))

# if jenis_pelanggan.lower() == "reguler":
#     if total_belanja < 500000:
#         total_bayar = total_belanja
#         print(f"Halo {nama_pelanggan}, Anda adalah jenis pelanggan {jenis_pelanggan}, Total belanja awal Rp{total_belanja:.2f}, Anda tidak mendapatkan diskon, Total yang harus dibayar Rp{total_bayar:.2f}")
#     elif total_belanja >= 500000:
#         diskon = total_belanja * 0.05
#         total_bayar = total_belanja - diskon
#         print(f"Halo {nama_pelanggan}, Anda adalah jenis pelanggan {jenis_pelanggan}, Total belanja awal Rp{total_belanja:.2f}, Anda mendapatkan diskon 5%, Total yang harus dibayar Rp{total_bayar:.2f}")

# elif jenis_pelanggan.lower() == "silver":
#     if total_belanja < 500000:
#         diskon = total_belanja * 0.05
#         total_bayar = total_belanja - diskon
#         print(f"Halo {nama_pelanggan}, Anda adalah jenis pelanggan {jenis_pelanggan}, Total belanja awal Rp{total_belanja:.2f}, Anda mendapatkan diskon 5%, Total yang harus dibayar Rp{total_bayar:.2f}")
#     elif total_belanja >= 500000:
#         diskon = total_belanja * 0.1
#         total_bayar = total_belanja - diskon
#         print(f"Halo {nama_pelanggan}, Anda adalah jenis pelanggan {jenis_pelanggan}, Total belanja awal Rp{total_belanja:.2f}, Anda mendapatkan diskon 10%, Total yang harus dibayar Rp{total_bayar:.2f}")

# elif jenis_pelanggan.lower() == "gold":
#     if total_belanja < 500000:
#         diskon = total_belanja * 0.1
#         total_bayar = total_belanja - diskon
#         print(f"Halo {nama_pelanggan}, Anda adalah jenis pelanggan {jenis_pelanggan}, Total belanja awal Rp{total_belanja:.2f}, Anda mendapatkan diskon 10%, Total yang harus dibayar Rp{total_bayar:.2f}")
#     elif total_belanja >= 500000:
#         diskon = total_belanja * 0.15
#         total_bayar = total_belanja - diskon
#         print(f"Halo {nama_pelanggan}, Anda adalah jenis pelanggan {jenis_pelanggan}, Total belanja awal Rp{total_belanja:.2f}, Anda mendapatkan diskon 15%, Total yang harus dibayar Rp{total_bayar:.2f}")

# else:
#     print("Jenis pelanggan tidak valid.")

# # .2f berfungsi untuk membatasi angka dibelakang koma menjadi 2 angka saja


# #warahi juned yang penilaian
# nilai = int(input("masukkan nilai anda: "))

# if nilai >= 90 :
#     print("A")
# elif nilai >= 80 :
#     print("B")
# elif nilai >= 70 :
#     print("C")
# else: 
#     print("D")


def my_sekull(name_sch):
    return f"Welkam to di {name_sch}!"

print(my_sekull("SMA negeri 1 Kudus"))

def luwas_persegay_panjang(p, l):
    hasil = p * l
    return f"{hasil} cm2"

print(luwas_persegay_panjang(10, 5))

def filter_penonton(umur, ktp):
    if umur >= 17 and ktp == True:
        return "Boleh nonton"
    else:
        return "Tidak boleh nonton"
    
print(filter_penonton(18, True))

'''Aktivitas 1: Kuis Kilat & Code Tracing (Individu)

Perintah:
Kerjakan soal-soal penelusuran logika berikut secara mandiri.

Soal 1 (Tracing Output)
Amatilah potongan kode berikut, lalu tentukan output yang dicetak jika nilai a = 15 dan b = 20!
'''
a = 15
b = 20

if a > 10:
    if b < 15:
        print("Kondisi A")
    else:
        print("Kondisi B")
else:
    print("Kondisi C")

#jawaban = Kondisi B, karena pada if statement pertama variabel a (15 > 10 = true) memenuhi syarat, lanjut ke if statement kedua, b (20 < 15 = false) tidak memebuhi syarat if statment, langsung dialihkan ke else statement.

'''Soal 2 (Tracing Output SIM)
Seseorang berusia 17 tahun tetapi belum memiliki SIM (punya_sim = False). Apa output dari kode di bawah?
'''
umur = 17
punya_sim = False

if umur >= 17:
    if punya_sim:
        print("Boleh Mengemudi")
    else:
        print("Harus Buat SIM Terlebih Dahulu")
else:
    print("Belum Cukup Umur")

#jawaban = Harus Buat SIM Terlebih Dahulu, karena umur memenuhi syarat (17 >= 17 = true), lanjut ke if kedua, punya_sim tidak memenuhi syarat (false), langsung lanjut ke else statement

'''Proyek Kelompok (Pair Programming)
Judul Proyek:
Build-a-Bot Eligibility System (Validator Diskon Kantin CLI)
'''

input_total_belanja = int(input("Total belanja anda: "))

def buat_nota(besaran_diskon, total_awal, total_akhir):
    print("\n===== NOTA =====")
    print(f"Total Awal      : Rp{total_awal}")
    print(f"Besaran Diskon  : Rp{besaran_diskon}")
    print(f"Total Akhir     : Rp{total_akhir}")

def validator_diskon(total_belanja):
    persen_diskon = 0
    besaran_diskon = 0
    harga_akhir = total_belanja

    if total_belanja >= 50000:
        member = input("Apakah anda mempunyai kartu member? (y/n): ").lower()

        if member == "y":
            persen_diskon = 0.2
            besaran_diskon = total_belanja * persen_diskon
            harga_akhir = total_belanja - besaran_diskon

            print("Kami memberi anda diskon 20%.")

        else:
            punya_kupon = input("Apakah anda membawa kupon? (y/n): ").lower()

            if punya_kupon == "y":
                persen_diskon = 0.1
                besaran_diskon = total_belanja * persen_diskon
                harga_akhir = total_belanja - besaran_diskon

                print("Kami memberi anda diskon 10%.")
            else:
                print("Maaf, tidak ada diskon untuk anda.")

    else:
        print("Maaf, tidak ada diskon untuk anda.")

    buat_nota(besaran_diskon, total_belanja, harga_akhir)

validator_diskon(input_total_belanja)


'''Aktivitas 3: Tes Praktik Mandiri (Unjuk Kerja)
Judul Kasus:
Validator Kelayakan Pinjaman Modal Usaha Kecil
'''

usia_pemohon = int(input("umur pemohon? : "))
penghasilan_perbulan = int(input("penghasilan per bulan?(Rp) : Rp"))
skor_kredit = int(input("skor kredit? : "))

def validator_kelayakan_pinjaman(usia, penghasilan, skor) :
    if usia >= 21 :
        if penghasilan >= 5000000 :
            if skor >= 75 :
                return "pinjaman disetujui, bunga 5%"
            else :
                return "Pinjaman Disetujui dengan Syarat Penjamin, Bunga 7%"
        else :
            return "pinjaman ditolak, penghasilan kurang"
       
    else :
        return "Usia Belum Memenuhi Syarat"

cek = validator_kelayakan_pinjaman(usia_pemohon, penghasilan_perbulan, skor_kredit)
print(cek)

'''
1. Mengapa indentation penting? Apa bedanya IndentationError dan Logical Error?
Indentation menentukan blok eksekusi pada Python. Tanpa indentation yang benar, program bisa gagal dijalankan (IndentationError) atau berjalan tetapi menghasilkan logika yang salah (Logical Error).

2. Kapan menggunakan Nested If dan kapan Single If dengan AND/OR?
Gunakan Nested If jika setiap kondisi memiliki proses atau hasil yang berbeda. Gunakan AND/OR jika hanya ingin mengecek beberapa syarat sekaligus untuk satu hasil. Nested If lebih cocok untuk logika bertingkat, sedangkan AND/OR lebih ringkas untuk kondisi sederhana.'''