import yt_dlp

url = "https://www.youtube.com/watch?v=Iy4OAIqv_04&pp=ygUaYWwgZm9uZG8gaGF5IHNpdGlvIGNhcCA0NzE%3D"

ydl_opts = {
    'format': 'best',
    'outtmpl': '%(title)s.%(ext)s',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
