from pytube import YouTube
import os

# inserire indirizzo video youtube
yt = YouTube(
    str(input("Enter the URL of the video you want to download: \n>> ")))

# extract only audio
video = yt.streams.filter(only_audio=True).first()

# scelta dove salvare il file
print("Dove vuoi salvarlo? (lasciare in bianco per directory corrente)")
destination = str(input(">> ")) or '.'

# download del file nella destinazione scelta
out_file = video.download(output_path=destination)

# salva il file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
