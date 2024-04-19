import os
import shutil
import subprocess
from pytube import Playlist, YouTube

def download_playlist(pl, hedef_klasor):
    
    # çalma listesindeki her bağlantıyı alır
    videolar = pl.video_urls
    
    # her bir öğeyi indirir
    for video in videolar:
        os.system("cls")
        
        # bağlantıyı YouTube nesnesine dönüştürür
        yt = YouTube(video)
        
        # en iyi ses kalitesini seçer
        ses = yt.streams.filter(only_audio=True).first()
        
        # varsayılan dosya adını alır
        varsayilan_dosyaadi = ses.default_filename
        print(varsayilan_dosyaadi)
        print(varsayilan_dosyaadi + " indiriliyor...")
        
        # sesi indirir ve yeniden adlandırır
        ses.download(output_path=hedef_klasor)
        varsayilan_dosyaadi_boslukssiz = varsayilan_dosyaadi.replace(" ", "")
        try:
            # zaten adlandırılmışsa, geç
            os.rename(os.path.join(hedef_klasor, varsayilan_dosyaadi), os.path.join(hedef_klasor, varsayilan_dosyaadi_boslukssiz))
        except:
            pass
            
        # çıktıyı MP3 formatına dönüştürür
        yeni_dosyaadi = varsayilan_dosyaadi.replace("mp4", "mp3")
        yeni_dosyaadi_boslukssiz = yeni_dosyaadi.replace(" ", "")
        print("MP3'e dönüştürülüyor....")
        
        # MP4 videosunu MP3 sesine dönüştürür ve sesi hedef klasöre taşır
        subprocess.call(f"ffmpeg -i {os.path.join(hedef_klasor, varsayilan_dosyaadi_boslukssiz)} {os.path.join(hedef_klasor, yeni_dosyaadi_boslukssiz)}", shell=True)
        os.remove(os.path.join(hedef_klasor, varsayilan_dosyaadi_boslukssiz))
        
    print("İndirme tamamlandı.")


def download_singell(video_link, hedef_klasor):
    yt = YouTube(video_link)
    video = yt.streams.filter(only_audio=True).first()
    default_filename = video.default_filename
    print(default_filename)
    print(default_filename + " indiriliyor...")
    video.download(output_path=hedef_klasor)
    yeni_dosyaadi = default_filename.replace("mp4", "mp3")
    yeni_dosya_yolu = os.path.join(hedef_klasor, yeni_dosyaadi)
    os.rename(os.path.join(hedef_klasor, default_filename), yeni_dosya_yolu)
    print("İndirme tamamlandı.")

if __name__ == "__main__":
    hedef_klasor = "./Downloads"
    secim = input("Lütfen indirme yöntemi seçin:\n0: Tekli\n1: Çalma Listesi\nSeçiminiz: ")
    
    if secim == "0":
        video_link = input("Lütfen indirmek istediğiniz video URL'sini girin: ")
        download_singell(video_link, hedef_klasor)
    elif secim == "1":
        playlist_url = input("Lütfen indirmek istediğiniz çalma listesinin URL'sini girin: ")
        download_playlist(playlist_url, hedef_klasor)
    else:
        print("Geçersiz seçim! Lütfen 0 veya 1 girin.")