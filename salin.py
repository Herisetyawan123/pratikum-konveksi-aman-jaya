# kumpulan data
size = ["S" ,"M", "L", "XL", "XXL"]
memberShip = ['3028', '3029']
diskonMember = 10/100 
jenisBarang = {
    1 : "baju lengan panjang",
    2 : "baju lengan pendek",
    3 : "celana panjang",
    4 : "celana pendek",
}
biayaJahit = {
    1 : {
        "jasa" : 70000,
        "katun" : 60000,
        "polister" : 80000  
    },
    2 : {
        "jasa" : 60000,
        "katun" : 50000,
        "polister" : 60000
    },
    3 : {
        "jasa" : 60000,
        "katun" : 40000,
        "polister" : 50000
    },
    4 : {
        "jasa" : 50000,
        "katun" : 50000,
        "polister" : 60000
    },
}
while True:
    status = False
    tanyaMember = input("apakah anda member ? [y/n] ")
    if tanyaMember != "y" and tanyaMember != "n":
        print("masukan y dan n")
        continue
    elif tanyaMember == "n":
        break
    member = input("masukan kode member : ")
    for kode in memberShip:
        if kode == str(member):
            status = True
            break
    if status:
        break
   
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

    hargaTotal = biayaJahit[kodeBarang]["jasa"] + biayaJahit[kodeBarang][kain]
    ukuran = input("masukan size pakaian(S,M,L,XL,XXL): ").upper()
    while not(ukuran in size):
        if ukuran in size: break
        ukuran = input("masukan size pakaian(S,M,L,XL,XXL) lagi: ").upper()
    while True:
        try:
            jumlahBarang = int(input("Masukan jumlah barang yang akan di jahit : "))
            hargaPakaian = hargaTotal * jumlahBarang
            if jumlahBarang >= 12:
                diskon = 0
                dsm = 0
                if jumlahBarang >= 60:
                    diskon = hargaPakaian * 10/100
                    total = hargaPakaian - diskon
                    if tanyaMember == "y":
                        dsm = total * diskonMember
                else:
                    total = hargaPakaian - diskon
                    if tanyaMember == "y":
                        dsm = total * diskonMember
                total = total - dsm
                break
            else:
                print("\n(X) Jumlah yang anda masukan kurang, minimal 12 pcs")
        except ValueError:
                print("Inputan harus angka")
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
            -------------------------------------------------'''.format(jenisBarang[kodeBarang], ukuran, kain,jumlahBarang, biayaJahit[kodeBarang]["jasa"], biayaJahit[kodeBarang][kain], hargaPakaian,int(diskon), int(dsm), int(total)))
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
            -------------------------------------------------'''.format(jenisBarang[kodeBarang], ukuran, kain,jumlahBarang, biayaJahit[kodeBarang]["jasa"], biayaJahit[kodeBarang][kain], hargaPakaian, int(diskon), int(total)))