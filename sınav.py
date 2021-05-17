def main():
    ogrenci_no=input('Ogrenci Numaranızı Giriniz')
    ogrenci_no=int(ogrenci_no)
    arkadaslar_dosyasi=open('arkadaslar.txt','w')
    ogno=ogrenci_no%10
    for sayac in range(1,ogno+1):
        isim=input('İsim Giriniz: ')
        telefon=input('Telefon giriniz: ')
        arkadaslar_dosyasi.write('İsim: '+isim+'\n')
        arkadaslar_dosyasi.write('Telefon: '+telefon+'\n')
    arkadaslar_dosyasi.close()
    print("arkadaslar.txt dosyasına yazılan veriler asagıda")
    arkadaslar_dosyasi=open('arkadaslar.txt','r')
    while isim !='':
        isim=arkadaslar_dosyasi.readline()
        numara=arkadaslar_dosyasi.readline()
        isim=isim.rstrip('\n')
        print(isim)
        numara=numara.rstrip('\n')
        print(numara)
    arkadaslar_dosyasi.close()
main()
