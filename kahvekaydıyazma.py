def main():
    devammi='e'
    kahve_dosyasi=open('kahve.txt','a')
    while devammi=='e' or devammi=='E':
        print('kahve detaylarını giriniz:')
        tanim=input('tanımı:')
        miktar=int(input('miktarı(ml):'))
        kahve_dosyasi.write(tanim+'\n')
        kahve_dosyasi.write(str(miktar)+'\n')
        print('Başka veri eklencek mi?')
        devammi=input('e/E: evet,diğer her şey :hayır')
    kahve_dosyasi.close()
    print('veriler kahve.txt dosyasına eklendi.')
main()