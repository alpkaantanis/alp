def main():
     calisan_sayisi=int(input('kaç adet çalışan girilecek?:'))
     calisan_dosyasi=open('calisanlar.txt','w')

     for sayac in range(1,calisan_sayisi+1):
         print('verileri giriniz çalışan #',sayac,sep='')
         isim=input('isim')
         sicil=input('sicil no :')
         bolum=input('Bölüm :')
         calisan_dosyasi.write(isim+'\n')
         calisan_dosyasi.write(sicil+'\n')
         calisan_dosyasi.write(bolum+'\n')
         print()
     calisan_dosyasi.close()
     print('Veriler calisanlar.txt. dosyasına yazıldı')
main()


