def menu():
    print ('Pilih Bentuk 2D')
    print ()
    print ('1. Persegi Panjang')
    print ('2. Lingkaran')
    print ('3. Segitiga')
    print ('4. Keluar')
    choice = int(input('Masukkan Nomer Pilihan: '))
    if choice == 1:
        from luas import luas_persegi
        luas_persegi.persegi()
    elif choice == 2:
        from luas import luas_lingkaran
        luas_lingkaran.lingkaran()
    elif choice == 3:
        from luas import luas_segitiga
        luas_segitiga.segitiga()
    else:
        exit()

def segitiga():
    print ('Menghitung Luas Segitiga')
    a = int(input('Masukkan Alas : '))
    t = int(input('Masukkan Tinggi : '))
    luas = (a*t)/2
    print ('Luas Segitiga adalah ',luas)
    print
    print ('Coba lagi [Y/N]? ')
    choice = input()
    back = choice.upper()
    if back == 'Y':
        menu()
    else:
        exit()
