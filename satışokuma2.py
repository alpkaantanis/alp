def main():
    satis_dosyasi=open('satislar.txt','r')

    for satir in satis_dosyasi:
        miktar=float(satir)
        print(format(miktar,'.2f'))
    satis_dosyasi.close()
main()