import random

def tas_kagit_makas_Muhammed_Said_YILDIZ():
    # Oyunun başında oyuncuyu karşılama mesajı ve kuralların açıklaması
    giris_mesaji=( "Merhabalar, Taş, Kağıt, Makas oyununa hoşgeldin. Bu oyunu hayatında bir kere de olsa oynamışsındır. Yine de hatırlatmak amacıyla oyunun nasıl oynandığını anlatacağım." \
                  "İlk önce giriş ekranından taş kağıt veya makas girdilerinden birini girmen gerekiyor eğer ki oyundan çıkmak istiyorsan da çıkış yazman yeterli." \
                  "Seçeneklerin birbirine olan üstünlükleri şöyledir: Taş makasa karşı kazanır, makas kağıda karşı kazanır ve kağıt da taşa karşı kazanır. Kazanılan her tur 1 puan değerindedir ve 2 puana ulaşan taraf oyunu kazanır." \
                  "Eğer ki bilgisayara karşı tekrardan oynamak istersen ki onun da istemesi lazım oyun bitiminde ekrana yöneltilen soruya Evet veya Hayır yazman yeterli olur. İşte bu kadar basit " 
                  )
    print(giris_mesaji)

    # Başlangıç puanları
    pc_skor = 0         # Bilgisayarın skorunu tutan sayaç
    oyuncu_skor = 0     # Oyuncunu skorunu tutan sayaç
    oyun_sayisi = 1     # Oyun sayısını tutan sayaç
    tur_sayisi = 1      # Tur sayısını tutan sayaç    
   
    while True : 
        
        # Oyuncu veya bilgisayar 2 skora ulaşana kadar döngü devam eder
        while oyuncu_skor < 2 and pc_skor < 2:
            secenekler = ["Taş", "Kağıt", "Makas"]  # Oyuncu ve bilgisayar için geçerli seçenekler
            rastgele_sayi2 = random.randint(0,2)    # Bilgisayarın rastgele seçimi için 0 ve 2 arasında sayı üretir
            pc_secenek = secenekler[rastgele_sayi2] # Üretilen rastgele sayıya göre seçenekler listesinden eleman seçer            

            # Oyun ve tur sayısını ekrana bastırma
            print(f"*************** {oyun_sayisi}. Oyun - {tur_sayisi}. Tur ***************")

            # Oyuncudan girdi alma
            oyuncu_secenek = input("Taş, Kağıt, Makas veya çıkış : ")

            # Oyuncu girdi bölümüne 'çıkış' yazarsa oyun sona erer
            if oyuncu_secenek== "çıkış":
                print("Oyun bitti. Tekrardan görüşmek üzere")
                return  # Fonksiyondan çıkış yaparak programı sonlandırır

            # Seçenekler içinden bir seçim yapılmadıysa, kullanıcıdan tekrar seçim yapması istenir
            if oyuncu_secenek not in secenekler:
                print("Geçersiz seçim, lütfen yeniden seçim yapınız.")
                continue    
            
            # Oyuncu ve bilgisayar aynı seçimi yaparsa tur berabere sonuçlanır
            if pc_secenek == oyuncu_secenek :
                print("Berabare, bu turu kazanan çıkmadı!")
                tur_sayisi += 1
            
            # Oyuncunun kazandığı durumlar gerçekleşirse Oyuncu skoru 1 arttırılır ve uygun yazı ekrana yazılır
            elif (oyuncu_secenek == "Taş" and pc_secenek == "Makas") or \
                 (oyuncu_secenek == "Kağıt" and pc_secenek == "Taş") or \
                 (oyuncu_secenek == "Makas" and pc_secenek == "Kağıt"):
                print("Bu turu kazandınız!")
                oyuncu_skor += 1
                tur_sayisi += 1

            # Oyuncunun kazanamadığı yani bilgisayarın kazandığı diğer durumlarda ise bilgisayar skoru 1 arttrılrı ve uygu yazıyı ekrana yazılır    
            else:
                print("Bilgisayar bu turu kazandı!")
                pc_skor += 1  
                tur_sayisi += 1  
            
            # Bilgisayarın tur içinde ne seçtiğini ve skor tablosunu ekrana yazdırır
            print(f"PC  {pc_secenek}  seçti" )
            print(f"Computer: {pc_skor} , Player: {oyuncu_skor} ") 

    # Skor kontrolü: Oyuncu veya bilgisayar 2 skora ulaştığında sonuç değerlendirilir
        if oyuncu_skor == 2:
           print("Tebrikler, oyunu kazandınız!")
           oyun_devam = yeni_oyun() # Yeni oyun fonksiyonundaki dönen değere göre oyuna edvam edilir
           if oyun_devam == True:
            oyuncu_skor = 0
            pc_skor = 0
            oyun_sayisi += 1
            tur_sayisi = 1
            continue    # Oyuna devam edileceği için döngünün yeniden başlatır
           else :           
            break   # Oyuna devam edilmeyeceği için döngüyü sonlandırı ve oyunu bitirir
                   
        elif pc_skor == 2:
           print("Bilgisayar kazandı, üzgünüm!")
           oyun_devam = yeni_oyun() # Yeni oyun fonksiyonundaki dönen değere göre oyuna edvam edilir
           if oyun_devam == True:
            oyuncu_skor = 0
            pc_skor = 0
            oyun_sayisi += 1
            tur_sayisi = 1
            continue    # Oyuna devam edileceği için döngünün yeniden başlatır
           else :                           
            break   # Oyuna devam edilmeyeceği için döngüyü sonlandırı ve oyunu bitirir

# Yeni oyun başlatma fonksiyonu
def yeni_oyun():
    # Bilgisayarın devam etme kararını rastgele oluşturan kod dizileri
    devam_secenekler1 = [True, False]
    rastgele_sayi1 = random.randint(0,1)
    pc_devam_secenek = devam_secenekler1[rastgele_sayi1] # Rastgele oluşturulan sayıdan rsatgele seçenek tanımalama 

    # Oyuncudan yeni oyun isteyip istemedğine dair girdi alınan döngü
    while  True:  
        oyuncu_devam_secenek = input("Bilgisayar da oynamak isterse bir oyun daha oynamak ister misin? (Evet \ Hayır):  ")

        # Oyuncu "Evet" girdisini girerse bu girdiyi True olarak tanımla
        if oyuncu_devam_secenek == "Evet":
            oyuncu_devam_secenek = True
            break
        # Oyuncu "Hayır" girdisini girerse bu girdiyi False olarak tanımla
        elif oyuncu_devam_secenek == "Hayır":
            oyuncu_devam_secenek = False
            break
        # Oyuncu "Evet" veya "Hayır" dışında girdi girerse uyarı mesajı ver ve döngüyü tekrarla
        else:
            print("Geçersiz giriş. Lütfen 'Evet' veya 'Hayır' yazın.")
               
    # Mantık operatörleri kullanarak oyuncunun ve bilgisayarın devam etme kararına göre kararını True ve False değerleri ile döndürme
    if pc_devam_secenek and oyuncu_devam_secenek == True:
        print("Bilgisayar da sizinle bir oyun daha oynamak istiyor")
        return True
    elif pc_devam_secenek == False and oyuncu_devam_secenek == True: 
        print("Bilgisayar sizinle bir oyun daha oynamak istemiyor")
        return False
    elif pc_devam_secenek == True and oyuncu_devam_secenek == False:
        print("Siz oynamak istemiyorsunuz ama bilgisayar oynamak istiyor.")
        return  False
    else:
        print("İkiniz de oynamak istemiyorsunuz.")
        return False
    
# Ana program, oyun fonksiyonunu başlatır
if __name__ == "__main__":
    tas_kagit_makas_Muhammed_Said_YILDIZ()
     