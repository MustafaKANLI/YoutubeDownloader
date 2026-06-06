import os
import yt_dlp

def eski_dosyalari_arsive_ekle():
    klasor = "./Downloads"
    arsiv_dosyasi = os.path.join(klasor, "indirilenler_arsivi.txt")

    # Klasör yoksa işlemi iptal et
    if not os.path.exists(klasor):
        print(f"❌ '{klasor}' klasörü bulunamadı.")
        return

    # Sadece .mp3 dosyalarını listele
    mp3_dosyalari = [f for f in os.listdir(klasor) if f.endswith('.mp3')]
    
    if not mp3_dosyalari:
        print("⚠️ Klasörde hiç MP3 dosyası bulunamadı.")
        return

    print(f"📁 Toplam {len(mp3_dosyalari)} eski şarkı bulundu. Kimlikleri (ID) bulunup arşive ekleniyor...\n")

    # yt-dlp'yi sadece arama yapıp ID çekecek şekilde ayarla (İndirme yapmaz)
    ydl_opts = {
        'extract_flat': True, 
        'quiet': True,
    }

    # Arşiv dosyasını ekleme modunda ('a') aç
    with open(arsiv_dosyasi, "a", encoding="utf-8") as f:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            for dosya in mp3_dosyalari:
                # Dosya adından .mp3 uzantısını temizle
                sarki_adi = dosya.replace(".mp3", "")
                print(f"🔍 Aranıyor: {sarki_adi}")
                
                try:
                    # YouTube'da şarkı adıyla arama yap ('ytsearch1:' sadece ilk sonucu getirir)
                    info = ydl.extract_info(f"ytsearch1:{sarki_adi}", download=False)
                    if 'entries' in info and len(info['entries']) > 0:
                        video_id = info['entries'][0]['id']
                        
                        # ID'yi arşiv formatına uygun şekilde dosyaya yaz
                        f.write(f"youtube {video_id}\n")
                        print(f"  ✅ Eklendi: youtube {video_id}")
                    else:
                        print(f"  ⚠️ Sonuç bulunamadı.")
                except Exception as e:
                    print(f"  ❌ Hata oluştu: {e}")
                    
    print("\n🎉 İşlem tamam! Eski dosyaların artık arşivde güvende ve tekrar indirilmeyecek.")

if __name__ == "__main__":
    eski_dosyalari_arsive_ekle()