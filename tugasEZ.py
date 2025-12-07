#soal 1 usia dewasa
umur_andi = 16
if umur_andi < 18 :
    print("jeh bayekk")
else :
    print("bayi tuwoo")

#soal 2 nilai lulus
nilai_dina = 85
if nilai_dina >= 70 :
    print("cie lulus🙄")
else :
    print("wakwokawka gagal😜😂")

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


umur = int(input("Masukkan umur Anda: "))
if umur < 10:
    print("Anak-anak")
elif umur <= 19:
    print("Remaja")
else:
    print("Dewasa")









#1 Program Penentuan Kategori Usia dan Status Pelajar 
nama = str(input("Masukkan nama Anda: "))
umur = int(input("Masukkan umur Anda: "))
status_pelajar = str(input("Pelajar/ bukan Pelajar ?"))

if umur < 18 :
   if status_pelajar.lower() == "pelajar":
        print(f"{nama}, Anda Pelajar di bawah umur.")
   else:
        print(f"{nama}, Anda Bukan Pelajar di bawah umur.")
elif umur >= 18 :
    if status_pelajar.lower() == "pelajar":
        print(f"{nama}, Anda Pelajar Dewasa.")
    else:
        print(f"{nama}, Anda Bukan Pelajar Dewasa.")
else:
    print("Input status pelajar tidak valid.")

#2 toko online memberi diskon 
nama_pelanggan = str(input("Masukkan nama pelanggan: "))
jenis_pelanggan = str(input("Masukkan jenis pelanggan (reguler/silver/gold): "))
total_belanja = float(input("Masukkan total belanja: "))

if jenis_pelanggan.lower() == "reguler":
    if total_belanja < 500000:
        total_bayar = total_belanja
        print(f"Halo {nama_pelanggan}, Anda adalah jenis pelanggan {jenis_pelanggan}, Total belanja awal Rp{total_belanja:.2f}, Anda tidak mendapatkan diskon, Total yang harus dibayar Rp{total_bayar:.2f}")
    elif total_belanja >= 500000:
        diskon = total_belanja * 0.05
        total_bayar = total_belanja - diskon
        print(f"Halo {nama_pelanggan}, Anda adalah jenis pelanggan {jenis_pelanggan}, Total belanja awal Rp{total_belanja:.2f}, Anda mendapatkan diskon 5%, Total yang harus dibayar Rp{total_bayar:.2f}")

elif jenis_pelanggan.lower() == "silver":
    if total_belanja < 500000:
        diskon = total_belanja * 0.05
        total_bayar = total_belanja - diskon
        print(f"Halo {nama_pelanggan}, Anda adalah jenis pelanggan {jenis_pelanggan}, Total belanja awal Rp{total_belanja:.2f}, Anda mendapatkan diskon 5%, Total yang harus dibayar Rp{total_bayar:.2f}")
    elif total_belanja >= 500000:
        diskon = total_belanja * 0.1
        total_bayar = total_belanja - diskon
        print(f"Halo {nama_pelanggan}, Anda adalah jenis pelanggan {jenis_pelanggan}, Total belanja awal Rp{total_belanja:.2f}, Anda mendapatkan diskon 10%, Total yang harus dibayar Rp{total_bayar:.2f}")

elif jenis_pelanggan.lower() == "gold":
    if total_belanja < 500000:
        diskon = total_belanja * 0.1
        total_bayar = total_belanja - diskon
        print(f"Halo {nama_pelanggan}, Anda adalah jenis pelanggan {jenis_pelanggan}, Total belanja awal Rp{total_belanja:.2f}, Anda mendapatkan diskon 10%, Total yang harus dibayar Rp{total_bayar:.2f}")
    elif total_belanja >= 500000:
        diskon = total_belanja * 0.15
        total_bayar = total_belanja - diskon
        print(f"Halo {nama_pelanggan}, Anda adalah jenis pelanggan {jenis_pelanggan}, Total belanja awal Rp{total_belanja:.2f}, Anda mendapatkan diskon 15%, Total yang harus dibayar Rp{total_bayar:.2f}")

else:
    print("Jenis pelanggan tidak valid.")

# .2f berfungsi untuk membatasi angka dibelakang koma menjadi 2 angka saja


#warahi juned yang penilaian
nilai = int(input("masukkan nilai anda: "))

if nilai >= 90 :
    print("A")
elif nilai >= 80 :
    print("B")
elif nilai >= 70 :
    print("C")
else: 
    print("D")