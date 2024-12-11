# SAYI TAHMİNİ OYUNU
import random
import os
from colorama import Fore, Style

# Skor tablosunu okuma
def skor_tablosu_oku():
    if os.path.exists("skor_tablosu.txt"):
        with open("skor_tablosu.txt", "r") as file:
            return file.read()
    return "Henüz oynanan bir oyun yok!"

# Skor tablosunu güncelleme
def skor_tablosu_guncelle(isim, puan):
    with open("skor_tablosu.txt", "a") as file:
        file.write(f"{isim}: {puan} puan\n")

# Zorluk seviyesi seçimi
def zorluk_seviyesi_secin():
    print("\nZorluk seviyeleri:")
    print("1 - Kolay (1-50 arası)")
    print("2 - Orta (1-70 arası)")
    print("3 - Zor (1-100 arası)")
    while True:
        try:
            secim = int(input("Bir zorluk seviyesi seçin (1/2/3): "))
            if secim == 1:
                return (1, 50)
            elif secim == 2:
                return (1, 70)
            elif secim == 3:
                return (1, 100)
            else:
                print(Fore.RED + "Hata: Geçerli bir zorluk seviyesi seçin!" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Hata: Lütfen 1-2-3 arasında bir sayı giriniz!" + Style.RESET_ALL)

# Tahmin oyunu
def tahmin_oyunu(aralik_min, aralik_max, isim):
    secilen_sayi = random.randint(aralik_min, aralik_max)
    deneme_sayi = 0
    tahminler = []

    print(f"\n{aralik_min} ile {aralik_max} arasında bir sayı tuttum!")
    print("Oyundan çıkmak için 'q' tuşuna basabilirsiniz.")

    while True:
        tahmin = input("Bir sayı tahmin ediniz: ")

        if tahmin.lower() == "q":
            print("Çıkış yapılıyor...")
            print(f"Tahminleriniz: {tahminler}")
            return None

        try:
            tahmin = int(tahmin)
            deneme_sayi += 1
            tahminler.append(tahmin)

            if tahmin < aralik_min or tahmin > aralik_max:
                print(Fore.RED + f"Hata: Lütfen {aralik_min} ile {aralik_max} arasında bir sayı giriniz!" + Style.RESET_ALL)
            elif tahmin < secilen_sayi:
                print(Fore.BLUE + "Tahmininizde biraz daha yukarı çıkmalısınız! :)" + Style.RESET_ALL)
            elif tahmin > secilen_sayi:
                print(Fore.BLUE + "Tahmininizde biraz daha aşağı inmelisiniz! :)" + Style.RESET_ALL)
            else:
                puan = max(0, 100 - deneme_sayi * 10)
                print(Fore.GREEN + f"Tebrikler doğru bildiniz! Tuttuğum sayı {secilen_sayi}." + Style.RESET_ALL)
                print(Fore.YELLOW + f"Oyunu başarılı bir şekilde tamamladınız! Toplam {deneme_sayi} tahminde bildiniz." + Style.RESET_ALL)
                print(Fore.CYAN + f"Puanınız: {puan}" + Style.RESET_ALL)
                skor_tablosu_guncelle(isim, puan)
                return puan
        except ValueError:
            print(Fore.RED + "Hata: Lütfen geçerli bir sayı giriniz!" + Style.RESET_ALL)

# Ana program
def ana_program():
    print("Hoş Geldiniz! Bu bir sayı tahmini oyunudur.")
    isim = input("Lütfen isminizi giriniz: ")

    print("\nÖnceki Skor Tablosu: ")
    print(skor_tablosu_oku())

    while True:
        aralik_min, aralik_max = zorluk_seviyesi_secin()
        tahmin_oyunu(aralik_min, aralik_max, isim)

        tekrar = input("Tekrar oynamak ister misiniz? (e/h): ").lower()
        if tekrar != "e":
            print("Görüşmek üzere...")
            break

ana_program()