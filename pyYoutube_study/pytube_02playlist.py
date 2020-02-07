

from pytube import Playlist

#재생목록 지정
pl = Playlist('https://www.youtube.com/playlist?list=PL5L3Lhdx2zrNu2PuVUyb-4UdheDcUN3K7')
 #유튜브 재생목록 링크

#재생 목록 다운
pl.download_all('C:\\Dev\\workspace\\crawling\\source\\PythonYoutube\\video') #위치지정
