#라이브러리 참조
from pytube import YouTube

#특정 영상 다운로드
# YouTube('https://www.youtube.com/watch?v=54EjMLjxuhQ&list=PL5L3Lhdx2zrOeitGY8Y0-717WbjWBl3Kq').streams.first().download()
YouTube('https://www.youtube.com/watch?v=54EjMLjxuhQ&list=PL5L3Lhdx2zrOeitGY8Y0-717WbjWBl3Kq').streams.first().download('./video') #위치지정, ./은 현재위치를 의미
