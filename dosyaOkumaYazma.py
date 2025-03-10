#Dosya Okuma ve Yazma => read, write, append

# Kullanıcının girdiği tek bir metni dosyaya yazma
with open("metin_dosyasi.txt", "w", encoding="utf-8") as dosya:
    metin = input("Bir metin girin: ")
    dosya.write(metin +"\n" )

# Dosyayı okuma ve ekrana yazdırma
with open("metin_dosyasi.txt", "r", encoding="utf-8") as dosya:
    icerik = dosya.read()
    print("\nDosya içeriği:")
    print(icerik)

# Kullanıcıdan 5 farklı satır alıp dosyaya yazma
with open("metin_dosyasi.txt", "a", encoding="utf-8") as dosya:
    print("\n5 farklı satır girin:")
    satirlar = []
    for i in range(5):
        satir = input(f"Satır {i+1}: ")
        satirlar.append(satir + "\n")  # Satır sonuna \n ekleniyor
    dosya.writelines(satirlar)  # Tüm satırları bir defada yazdır

print("\nDosya başarıyla yazıldı.")

# Dosyayı satır satır okuyarak ekrana yazdırma
with open("metin_dosyasi.txt", "r", encoding="utf-8") as dosya:
    print("\nDosyadaki satırlar:")
    for satir in dosya:
        print(satir.strip())  # Satır sonundaki boşlukları temizle

