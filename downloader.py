import os
import yt_dlp

def download_audio(url, hedef_klasor, is_playlist=False, tekrar_indir=False):
    # Hedef klasör yoksa oluştur
    if not os.path.exists(hedef_klasor):
        os.makedirs(hedef_klasor)
        print(f"📁 '{hedef_klasor}' klasörü oluşturuldu.")

    # yt-dlp temel ayarları
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(hedef_klasor, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ignoreerrors': True, # Telifli/Gizli videoları çökmeksizin atlar
        'quiet': False, 
    }

    # Eğer kullanıcı "Hayır" (H) dediyse arşiv sistemini devreye sok
    if not tekrar_indir:
        arsiv_dosyasi = os.path.join(hedef_klasor, 'indirilenler_arsivi.txt')
        ydl_opts['download_archive'] = arsiv_dosyasi
        print("📌 Arşiv sistemi devrede: Önceden indirilenler anında atlanacak.")
    else:
        # Eğer "Evet" dendiyse üzerine yazmaya izin ver
        ydl_opts['overwrites'] = True

    mesaj = "Çalma listesi" if is_playlist else "Video"
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"\n⏳ {mesaj} işlem görüyor: {url}")
        try:
            ydl.download([url])
            print("\n✅ İşlem tamamlandı!")
        except Exception as e:
            print(f"\n❌ Beklenmeyen bir hata oluştu: {e}")

if __name__ == "__main__":
    hedef_klasor = "./Downloads"
    
    print("🎵 YouTube MP3 İndiriciye Hoş Geldin 🎵")
    print("-" * 40)
    
    secim = input("Lütfen indirme yöntemi seç:\n[0] Tekli Video\n[1] Çalma Listesi\nSeçiminiz: ")
    
    if secim in ["0", "1"]:
        ustune_yaz_secim = input("Klasörde var olan şarkılar tekrar indirilsin mi? (E/H): ").lower()
        tekrar_indir = True if ustune_yaz_secim == 'e' else False
        
        is_playlist = (secim == "1")
        mesaj_link = "çalma listesi" if is_playlist else "video"
        
        link = input(f"🔗 İndirmek istediğin {mesaj_link} URL'sini gir: ")
        
        download_audio(link, hedef_klasor, is_playlist=is_playlist, tekrar_indir=tekrar_indir)
    else:
        print("⚠️ Geçersiz seçim! Lütfen sadece 0 veya 1 gir.")