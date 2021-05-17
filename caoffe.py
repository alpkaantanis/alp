import os 
def main():
    bulundu = False
    arama = input('Aranacak kahve tanımını giriniz: ')
    new_miktar = int(input('Yeni miktarı giriniz: '))
    coffee_file = open('coffee.txt', 'r')
    gecici_file = open('temp.txt', 'w')
    tanim = coffee_file.readline()
    while tanim != '':
        miktar = float(coffee_file.readline())
        tanim = tanim.rstrip('\n')
        if tanim == arama:
            gecici_file.write(tanim + '\n')
            gecici_file.write(str(new_miktar) + '\n')

            bulundu = True
        else:
            gecici_file.write(tanim + '\n')
            gecici_file.write(str(miktar) + '\n')
        tanim = coffee_file.readline()
    coffee_file.close()
    gecici_file.close()
    os.remove('coffee.txt')
    os.rename('temp.txt', 'coffee.txt')
    if bulundu:
        print('Dosya güncellendi.')
    else:
        print('Dosya bulunamadı.')
main()