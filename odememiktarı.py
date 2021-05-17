def main():
    try:
        saat=int(input('kaç saat çalıştın'))
        saatlik_ucret=float(input('Saatlik ücretinizi giriniz'))
        toplam_odeme=saat*saatlik_ucret
        print('Toplam Ödeme:',format(toplam_odeme,',.2f'),sep='')
    except ValueError:
        print('HATA:Çalışılan saatler ve kaç saat çalıştığınız')
        print('rakamlarla girilmelidir')
main()