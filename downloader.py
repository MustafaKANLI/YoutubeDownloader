import os
import yt_dlp

def download_audio(url, hedef_klasor, is_playlist=False):
    # Hedef klasör yoksa oluştur
    if not os.path.exists(hedef_klasor):
        os.makedirs(hedef_klasor)
        print(f"📁 '{hedef_klasor}' klasörü oluşturuldu.")

    # yt-dlp ayarları
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(hedef_klasor, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        # Eğer çalma listesiyse hatalı videoları atla ve devam et
        'ignoreerrors': True if is_playlist else False,
        'quiet': False, # İndirme detaylarını konsolda görmek için
    }

    mesaj = "Çalma listesi" if is_playlist else "Video"
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"\n⏳ {mesaj} indiriliyor: {url}")
        try:
            ydl.download([url])
            print("\n✅ İndirme ve MP3'e dönüştürme işlemi tamamlandı!")
        except Exception as e:
            print(f"\n❌ Bir hata oluştu: {e}")

if __name__ == "__main__":
    hedef_klasor = "./Downloads"
    
    print("🎵 YouTube MP3 İndiriciye Hoş Geldin 🎵")
    print("-" * 40)
    secim = input("Lütfen indirme yöntemi seç:\n[0] Tekli Video\n[1] Çalma Listesi\nSeçiminiz: ")
    
    if secim == "0":
        video_link = input("🔗 İndirmek istediğin video URL'sini gir: ")
        download_audio(video_link, hedef_klasor, is_playlist=False)
    elif secim == "1":
        playlist_url = input("🔗 İndirmek istediğin çalma listesinin URL'sini gir: ")
        download_audio(playlist_url, hedef_klasor, is_playlist=True)
    else:
        print("⚠️ Geçersiz seçim! Lütfen sadece 0 veya 1 gir.")