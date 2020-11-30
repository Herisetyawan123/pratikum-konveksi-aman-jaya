# kumpulan data
size = ["S" ,"M", "L", "XL", "XXL"]
memberShip = ['3028', '3029']
diskonMember = 10/100 
tanyaMember = input("apakah anda member ? [y/n] ")
while tanyaMember != "y" and tanyaMember != "n":
    if tanyaMember == "y" or tanyaMember == "n":break
    tanyaMember = input("apakah anda member ? [y/n] ")
    


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
while not(kodeBarang <= 4 and kodeBarang >= 1):
    if kodeBarang <= 4 and kodeBarang >= 1: break
    kodeBarang = int(input("inputan salah, Masukan nomor barang yang ingin di jahit lagi : "))


if kodeBarang <= 4:
    print('''\n---------Jenis Kain YANG DI INGINKAN--------        
    
    1. Katun
    2. Poliester
    ''')
    jenisKain = int(input("Masukan Nomor jenis kain :  "))
    while not(jenisKain <= 2 and jenisKain >= 1):
        if jenisKain <= 2 and jenisKain >=1: break
        jenisKain = int(input("inputan salah, Masukan Nomor jenis kain lagi :  "))
        
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
        ukuran = input("masukan size pakaian(S,M,L,XL,XXL): ").upper()
        while not(ukuran in size):
            if ukuran in size: break
            ukuran = input("masukan size pakaian(S,M,L,XL,XXL) lagi: ").upper()

        while True:
            try:
                jumlahBarang = int(input("Masukan jumlah barang yang akan di jahit : "))
                hargaPakaian = (jasa + hargaKain) * jumlahBarang

                if jumlahBarang >= 12:
                    if jumlahBarang >= 60:
                        diskon = hargaPakaian * 10/100
                        harga = hargaPakaian - diskon
                        if tanyaMember == "y":
                            dsm = harga * diskonMember
                            harga = harga - dsm
                    else:
                        diskon = 0
                        harga = hargaPakaian - diskon
                        if tanyaMember == "y":
                            dsm = harga * diskonMember
                            harga = harga - dsm
                    break
                else:
                    print("\n(X) Jumlah yang anda masukan kurang, minimal 12 pcs")
            except ValueError:
                    print("Inputan harus angka")
    else:
        print("\n(X) Jenis kain tidak tersedia")  
else:
    print("\n(X) Maaf Barang belum tersedia")


if tanyaMember == "y":
    print('''-------------------------------------------------
                        KONVEKSI AMAN JAYA
                        Jl. Mastrip, Jember
                -------------------------------------------------

                    Jenis Pakaian       : {}
                    Size                : {}
                    Jenis Kain          : {}
                    Total Barang        : {} pcs
                    Biaya jasa jahit    : Rp. {:,}
                    Biaya kain          : Rp. {:,}
                    Biaya Pakaian       : Rp. {:,}
                    Diskon              : Rp. {:,}
                    Diskon Membership   : Rp. {:,}
                    Total Pembayaran    : Rp. {:,}
            -------------------------------------------------
            TERIMA KASIH TELAH MENJAHIT DI KONVEKSI AMAN JAYA
            -------------------------------------------------'''.format(jenisBarang, ukuran, kain,jumlahBarang, jasa, hargaKain, hargaPakaian,int(dsm), int(diskon), int(harga)))
else:
    print('''-------------------------------------------------
                        KONVEKSI AMAN JAYA
                        Jl. Mastrip, Jember
                -------------------------------------------------

                    Jenis Pakaian       : {}
                    Size                : {}
                    Jenis Kain          : {}
                    Total Barang        : {} pcs
                    Biaya jasa jahit    : Rp. {:,}
                    Biaya kain          : Rp. {:,}
                    Biaya Pakaian       : Rp. {:,}
                    Diskon              : Rp. {:,}
                Total Pembayaran    : Rp. {:,}
            -------------------------------------------------
            TERIMA KASIH TELAH MENJAHIT DI KONVEKSI AMAN JAYA
            -------------------------------------------------'''.format(jenisBarang, ukuran, kain,jumlahBarang, jasa, hargaKain, hargaPakaian, int(diskon), int(harga)))