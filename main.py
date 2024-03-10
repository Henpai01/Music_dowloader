from pytube import YouTube
import os

print('\nPara descargar musica en YT\n')

URL = input("Coloca la URL:")
yt = YouTube(URL)

try:
    print("\nDescargando...")
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download()
    base, ext = os.path.splitext(out_file)
    new_file = base + ".mp3"
    os.rename(out_file, new_file)
    print("\nSe ha descargado, Correctamente.\n")

except:
    print("\nAlgo salió mal, intenta nuevamente!.....\n")