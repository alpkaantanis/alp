def main():
    kahve_dosyasi=open('kahve.txt','r')
    tanim=kahve_dosyasi.readline()
    while tanim !='':
       miktar=float(kahve_dosyasi.readline())
       tanim =tanim.rstrip('\n')
       print('Tanım',tanim)
       print('miktar',miktar)
       tanim=kahve_dosyasi.readline()
    kahve_dosyasi.close()
main()