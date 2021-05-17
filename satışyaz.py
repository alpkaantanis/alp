def main():
     gunler=int(input('Kaç gün satış yaptınız?:'))
     satis_dosyasi=open('satislar.txt', 'w')
     for sayac in range(1,gunler+1):
         satis= float(input('Satışları giriniz gün'+str(sayac)+':'))
         satis_dosyasi.write(str(satis)+'\n')
         print('veriler satislar.txt dosyasına yazıldı')
     satis_dosyasi.close()
main()

