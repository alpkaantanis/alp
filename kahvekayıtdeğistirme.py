import os 
def main():
    bulundu=False
    arama=input('Aranacak kahve tanımını giriniz:')
    yeni_miktar=int(input('Yeni kahve miktarını giriniz'))
    kahve_dosyasi=open('kahve.txt','r')
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
    os.remove('kahve.txt')
    os.rename('temp.txt','kahve.txt')
    if bulundu:
        print('Dosya güncellendi')
    else:
        print('dosya bulunamadı')
main()