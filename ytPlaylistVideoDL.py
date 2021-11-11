from pytube import Playlist
import sys

if len(sys.argv) == 1:
    print('Passe pelo terminal a URL de alguma playlist ou de algum vídeo dentro da playlist.')
else:
    try:
        count = 1
        playlist = Playlist(sys.argv[1])
        for video in playlist.videos:
            print('Baixando Vídeo #'+str(count)+' de '+str(len(playlist.video_urls)))
            video.streams.get_highest_resolution().download()
            count+=1
    except:
        print("Passe pelo terminal uma URL de uma playlist válida.")