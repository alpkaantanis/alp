def main():
    num_videos=int(input('oynatma videounuzda kaç video var?'))
    video_dosyası=open('video_süreleri.txt','w')

    print('Her videonun süresini giriniz:')
    for count in range(1,num_videos +1):
        run_time=float(input('video #'+str(count)+':'))
        video_dosyası.write(str(run_time)+'\n')

    video_dosyası.close
    print('video oynatma süreleri video_süreleri.txt dosyasına yazıldı')
main()