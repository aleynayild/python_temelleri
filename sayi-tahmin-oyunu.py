import random #random modülünü dahil ettik fakat modülleri daha öğrenmedik.

def sayi_tahmin_oyunu():
    print("1 ile 100 arasında bir sayı tuttum. 3 tahmin hakkın var!")
    
    gizli_sayi = random.randint(1, 100)  # Bilgisayar rastgele bir sayı seçiyoruz
    tahmin_sayisi = 0  # Kaç kez tahmin yaptığını takip ediyoruz
    tahmin_hakki = 3  # Kullanıcıya 3 tahmin hakkı veriyoruz
    
    while tahmin_sayisi < tahmin_hakki:
        tahmin = int(input("Tahmin ettiğin sayı: "))  # Kullanıcıdan tahmin alıyoruz
        tahmin_sayisi += 1
        
        if tahmin < gizli_sayi:
            print("Daha büyük bir sayı dene!")
        elif tahmin > gizli_sayi:
            print("Daha küçük bir sayı dene!")
        else:
            print(f"Tebrikler! {tahmin_sayisi}. denemede doğru sayıyı buldun: {gizli_sayi}")
            break
    else:
        print(f"Maalesef tahmin hakkın bitti! Doğru sayı: {gizli_sayi}")

sayi_tahmin_oyunu()
