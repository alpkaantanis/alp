import os 
def main():
    devammi='e'
    kahve_dosyasi=open('kahve2.txt','a')
    while devammi=='e' or devammi=='E':
        print('kahve detaylarını giriniz:')
        tanim=input('tanımı:')
        miktar=int(input('miktarı(ml):'))
        kahve_dosyasi.write(tanim+'\n')
        kahve_dosyasi.write(str(miktar)+'\n')
        print('Başka veri eklencek mi?')
        devammi=input('e/E: evet,diğer her şey :hayır')
    kahve_dosyasi.close()
    print('veriler kahve2.txt dosyasına eklendi.')
    bulundu=False
    arama=input('Aranacak kahve tanımını giriniz:')
    kahve_dosyasi=open('kahve.txt','r')
    if arama==kahve_dosyasi.readline():
        print('Dosya güncellendi')
        yeni_miktar=int(input('Yeni kahve miktarını giriniz'))
        kahve_dosyasi=open('kahve2.txt','r')
        gecici_dosya=open('temp.txt','w')
        tanim=kahve_dosyasi.readline()
        while tanim !='':
            miktar=float(kahve_dosyasi.readline())
            tanim=tanim.rstrip('\n')
            if tanim== arama:
               gecici_dosya.write(tanim+'\n')
               gecici_dosya.write(str(yeni_miktar)+'\n')
               bulundu=True
            else:
                gecici_dosya.write(tanim+'\n')
                gecici_dosya.write(str(miktar)+'\n')
            tanim=kahve_dosyasi.readline()
            kahve_dosyasi.close()
            gecici_dosya.close()
            os.remove('kahve2.txt')
            os.rename('temp.txt','kahve2.txt')
    else:
        print('dosya bulunamadı')
    

main()