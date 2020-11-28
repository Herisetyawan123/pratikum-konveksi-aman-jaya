# jenis barang
jenisBarang = ["Baju lengan panjang", "Baju lengan pendek", "Celana panjang", "Celana Pendek"]
# harga
hargaOutfit = [70000, 60000, 60000, 50000]
# jenis kain
jenisKain = ["kain", "polister"]
# ukuran baju
size = ["S", "M", "L", "XL", "XXL"]


print('''
-------------------------------------
SELAMAT DATANG DI KONVEKSI AMAN JAYA
-------------------------------------''')
no = 0
for i in range(len(jenisBarang)):
    no += 1
    print("     {}. {} = Rp. {:,}".format(no, jenisBarang[i], hargaOutfit[i]))


kodeBarang = int(input("Masukan nomor barang yang ingin di jahit : "))
while not(kodeBarang <= 4 and kodeBarang > 0):
    if kodeBarang == 1 or kodeBarang == 2:
        break
    kodeBarang = int(input("(X) Jenis Barang tidak tersedia, mohon masukan Nomor jenis barang :  "))

print("\n---------Jenis Kain YANG DI INGINKAN--------")
no = 0
for kain in jenisKain:
    no += 1
    print("     {}. {}".format(no,kain))

jenisKain = int(input("Masukan Nomor jenis kain :  "))
while jenisKain != 2 and jenisKain != 1:
    if jenisKain == 1 or jenisKain == 2:
        break
    jenisKain = int(input("(X) Jenis kain tidak tersedia, mohon masukan Nomor jenis kain :  "))


ukuran = input("masukan size pakaian(S,M,L,XL,XXL): ").upper()
while not(ukuran in size):
    if ukuran in size:
        break
    ukuran = input("(X) Ukuran yang anda masukan salah, masukan size pakaian(S,M,L,XL,XXL): ").upper()

# if jenisKain == 1 or jenisKain == 2:
#      if kodeBarang == 1 or kodeBarang == 2:
#          jenisBarang = "baju"
#          if kodeBarang == 1:
#              jenisBarang = jenisBarang + " lengan " + "panjang"
#              jasa = 70000
#              if kain == "katun":
#                  hargaKain = 60000
#              else:
#                  hargaKain = 80000
#          else:
#              jenisBarang = jenisBarang + " lengan " + "pendek"
#              jasa = 60000
#              if kain == "katun":
#                  hargaKain = 50000
#              else:
#                  hargaKain = 60000
#      else:
#          jenisBarang = "celana"
#          if kodeBarang == 3:
#              jenisBarang = jenisBarang + " " + "panjang"
#              jasa = 60000
#              if kain == "katun":
#                  hargaKain = 50000
#              else:
#                  hargaKain = 60000
#          else:
#              jenisBarang = jenisBarang + " " + "pendek"
#              jasa = 50000
#              if kain == "katun":
#                  hargaKain = 40000
#              else:
#                  hargaKain = 50000


#      ukuran = input("masukan size pakaian(S,M,L,XL,XXL): ")
#      if ukuran.upper() in size:
#          jumlahBarang = int(input("Masukan jumlah barang yang akan di jahit : "))
#          hargaPakaian = (jasa + hargaKain) * jumlahBarang
#          if jumlahBarang >= 12:
#              if jumlahBarang >= 60:
#                  diskon = hargaPakaian * 10/100
#              else:
#                  diskon = 0
#              harga = hargaPakaian - diskon
#              print('''\n\n-------------------------------------------------
#          KONVEKSI AMAN JAYA
#          Jl. Mastrip, Jember
#  -------------------------------------------------

#      Jenis Pakaian       : {}
#      Size                : {}
#      Jenis Kain          : {}
#      Total Barang        : {} pcs
#      Biaya jasa jahit    : Rp. {}
#      Biaya kain          : Rp. {}
#      Biaya Pakaian       : Rp. {}
#      Diskon              : Rp. {}
#      Total Pembayaran    : Rp. {}
#  -------------------------------------------------
#  TERIMA KASIH TELAH MENJAHIT DI KONVEKSI AMAN JAYA
#  -------------------------------------------------'''.format(jenisBarang, ukuran.upper(), kain,jumlahBarang, jasa, hargaKain, hargaPakaian, int(diskon), int(harga)))
#          else:
#              print("\n(X) Jumlah yang anda masukan kurang, minimal 12 pcs")
#      else:
#          print("\n(X) Masukan ukuran sesuai format / ukuran tidak tersedia")
# else:
#      print("\n(X) Jenis kain tidak tersedia")  
