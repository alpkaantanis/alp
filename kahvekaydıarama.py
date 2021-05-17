def main():
    bulundu=False
    arama=input('Aranacak kahve tanımını giriniz:')
    kahve_dosyasi=open('kahve.txt','r')
    tanim=kahve_dosyasi.readline()
    while tanim !='':
        miktar=float(kahve_dosyasi.readline())
        tanim=tanim.rstrip('\n')
        if tanim== arama:
            print('Tanım:',tanim)
            print('Miktar',miktar)
            print()
            bulundu=True
        tanim=kahve_dosyasi.readline()   
    kahve_dosyasi.close()
    if not bulundu:
        print('Dosya içinde bulunamadı')   
main()
