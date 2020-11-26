'''
HERI SETYAWAN	(202410103028)
DIKI DWI AJI	(202410103029)

“KONVEKSI AMAN JAYA”

sebuah perusahaan konveksi bernama aman jaya ingin membuat struk pembayaran kasir yang berisi, ·        
1.pilihan pakaian berupa (baju lengan panjang/pendek, celana panjang/pendek),
2.pilihan ukuran pakaian(S,M,L,XL,XXL),
3.ongkos jahit pakaian
1.      baju lengan panjang = Rp. 70.000
2.      baju lengan pendek = Rp.60.000
3.      celana panjang = Rp.60.000
4.      celana pendek = Rp.50.000
4.banyaknya pesanan (harus grosir, minimal 1 lusin(12 pcs))
5.pilihan kain,
1.      baju pendek katun Rp.50.000
2.      baju pendek polyester Rp.60.000
3.      baju panjang katun Rp.60.000
4.      baju Panjang polyester Rp.80.000
5.      celana pendek katun Rp. 40.000
6.      celana pendek polyester Rp.50.000
7.      celana panjang katun Rp.50.00
8.      celana Panjang polyester Rp.60.000 
6.diskon 10% bila membeli lebih dari 5 lusin(60 pcs)
'''

print('''
-------------------------------------
SELAMAT DATANG DI KONVEKSI AMAN JAYA
-------------------------------------

    1. baju lengan panjang = Rp. 70.000
    2. baju lengan pendek = Rp. 60.000
    3. celana panjang =  Rp. 60.000
    4. celana pendek = Rp. 50.000
''')
kodeBarang = int(input("Masukan nomor barang yang ingin di jahit : "))

# ukuran baju
size = "S, M, L, XL, XXL"


if kodeBarang <= 4:
    print('''\n---------Jenis Kain YANG DI INGINKAN--------        
    
    1. Katun
    2. Poliester
    ''')
    jenisKain = int(input("Masukan Nomor jenis kain :  "))
    if jenisKain == 1:
        kain = "katun"
    elif jenisKain == 2:
        kain = "polister"
    if jenisKain == 1 or jenisKain == 2:
        if kodeBarang == 1 or kodeBarang == 2:
            jenisBarang = "baju"
            if kodeBarang == 1:
                jenisBarang = jenisBarang + " lengan " + "panjang"
                jasa = 70000
                if kain == "katun":
                    hargaKain = 60000
                else:
                    hargaKain = 80000
            else:
                jenisBarang = jenisBarang + " lengan " + "pendek"
                jasa = 60000
                if kain == "katun":
                    hargaKain = 50000
                else:
                    hargaKain = 60000
        else:
            jenisBarang = "celana"
            if kodeBarang == 3:
                jenisBarang = jenisBarang + " " + "panjang"
                jasa = 60000
                if kain == "katun":
                    hargaKain = 50000
                else:
                    hargaKain = 60000
            else:
                jenisBarang = jenisBarang + " " + "pendek"
                jasa = 50000
                if kain == "katun":
                    hargaKain = 40000
                else:
                    hargaKain = 50000
        ukuran = input("masukan size pakaian(S,M,L,XL,XXL): ")
        if ukuran.upper() in size:
            jumlahBarang = int(input("Masukan jumlah barang yang akan di jahit : "))
            hargaPakaian = (jasa + hargaKain) * jumlahBarang
            if jumlahBarang >= 12:
                if jumlahBarang >= 60:
                    diskon = hargaPakaian * 10/100
                else:
                    diskon = 0
                harga = hargaPakaian - diskon
                print('''\n\n-------------------------------------------------
            KONVEKSI AMAN JAYA
            Jl. Mastrip, Jember
    -------------------------------------------------

        Jenis Pakaian       : {}
        Size                : {}
        Jenis Kain          : {}
        Total Barang        : {} pcs
        Biaya jasa jahit    : Rp. {}
        Biaya kain          : Rp. {}
        Biaya Pakaian       : Rp. {}
        Diskon              : Rp. {}
        Total Pembayaran    : Rp. {}
    -------------------------------------------------
    TERIMA KASIH TELAH MENJAHIT DI KONVEKSI AMAN JAYA
    -------------------------------------------------'''.format(jenisBarang, ukuran.upper(), kain,jumlahBarang, jasa, hargaKain, hargaPakaian, int(diskon), int(harga)))
            else:
                print("\n(X) Jumlah yang anda masukan kurang, minimal 12 pcs")
        else:
            print("\n(X) Masukan ukuran sesuai format / ukuran tidak tersedia")
    else:
        print("\n(X) Jenis kain tidak tersedia")  
else:
    print("\n(X) Maaf Barang belum tersedia")