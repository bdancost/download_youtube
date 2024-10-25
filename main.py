from pytubefix import YouTube

# Solicitar a URL do vídeo
url = input('Cole aqui sua url: ')
yt = YouTube(url)

# Exibir título e thumbnail do vídeo
print("Título:", yt.title)
print("Thumbnail URL:", yt.thumbnail_url)

# Obter streams disponíveis
streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()

# Exibir opções de resolução
print("Resuloções disponíveis:")
for stream in streams:
    print(stream.resolution)

# Selecionar a melhor resolução
best_stream = streams.first() # Pega o primeiro stream da lista, que é o de melhor resolução
print(f"Baixando: {best_stream.resolution}")

# Fazer o download do vídeo
best_stream.download()
print("Download completo!")