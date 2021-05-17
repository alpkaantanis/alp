def main():
    calisan_dosyasi=open('calisanlar.txt','r')
    isim=calisan_dosyasi.readline()
    while isim !='':
        sicil=calisan_dosyasi.readline()
        bolum=calisan_dosyasi.readline()
        isim=isim.rstrip('\n')
        sicil=sicil.rstrip('\n')
        bolum=bolum.rstrip('\n')
        print('isim:',isim)
        print('sicil:',sicil)
        print('bolum:',bolum)
        print()
        isim=calisan_dosyasi.readline()
    calisan_dosyasi.close()
main()

