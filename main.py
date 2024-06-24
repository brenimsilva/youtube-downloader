from pytube import YouTube
from pydub import AudioSegment
import os

def download_youtube_video(url, download_path, as_mp3=False):
    try:
        yt = YouTube(url)

        stream = yt.streams.get_highest_resolution()

        print("Baixando o vídeo...")
        video_path = stream.download(download_path)
        print(f"Vídeo baixado com sucesso: {video_path}")

        if as_mp3:
            print("Convertendo vídeo para MP3...")
            audio_path = os.path.splitext(video_path)[0] + '.mp3'
            AudioSegment.from_file(video_path).export(audio_path, format='mp3')
            print(f"Áudio MP3 criado com sucesso: {audio_path}")

            os.remove(video_path)
            print("Arquivo de vídeo original excluído.")

            return audio_path
        else:
            return video_path
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return None


url = input("Digite a URL do vídeo do YouTube: ")
download_path = "./downloads"
as_mp3 = input("Deseja baixar como MP3? (s/n): ").lower() == 's'

download_youtube_video(url, download_path, as_mp3)
