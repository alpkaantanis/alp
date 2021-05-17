def main():
     satis_dosyasi= open('satislar.txt','r')
     satir= satis_dosyasi.readline()
     while satir != '':
         miktar = float(satir)
         print(format(miktar,'2f'))
         satir=satis_dosyasi.readline()
     satis_dosyasi.close()
main()