from pytube import YouTube

url = input("Digite a url do YouTube: ")

video = YouTube(url)

video.streams.get_highest_resolution().download(
    output_path = r"C:\Users\Kurumí\Downloads",
    filename = video.title
)

video.streams.filter(only_audio=True).first().download(
    output_path = r"C:\Users\Kurumí\Downloads",
    filename = video.title + ".mp3"
)