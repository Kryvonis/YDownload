import sys
import os
from pytube import YouTube

def startDownload(link: str):
    if link:
        video_name = ''
        try:
            ytObj = YouTube(link)
            video = ytObj.streams.filter(file_extension='mp4').get_highest_resolution()
            video_name = f'{video.title}.mp4'
            video.download()
        except Exception as error:
            print('Error')
            print(error)
            return
        print(f'File dowloaded')
        print(f'{os.getcwd()}/{video_name}')
    else:
        print('No link')
    
def main(link: str):
    print('let`s download')
    startDownload(link)
    print('Done')

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        print(f'Link --- ${sys.argv[1]}')
        main(sys.argv[1])
    else:
        print('No link')