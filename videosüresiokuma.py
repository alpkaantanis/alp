def main():
    video_dosyasi=open('video_süreleri.txt','r')
    total=0.0
    count=0
    print('Dosya içindeki videoların her birinin süreleri:')
    for line in video_dosyasi:
        run_time=float(line)
        count+=1
        print('video #',count,':',run_time)
        total +=run_time
    video_dosyasi.close()
    print('toplam oynatma süresi',total,'dakika saniyedir')
main()



