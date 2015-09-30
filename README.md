# YoutubeChannelDownloader

These classes allow you to create a program in ~15 lines (see main.py) that will download and convert an entire
youtube channel to mp3 files. 

This was created to download entire EDM music channels on Youtube for example: MrSuicideSheep, Proximity, Liquicity, etc.


DEPENDENCIES:

- requests  (pip install requests OR easy_install requests)
- pytube (download zip at: https://github.com/NFicano/pytube then "sudo python setup.py install" OR pip install pytube
- python-video-converter (download zip at: https://github.com/Bullzeyes/python-video-converter then "sudo python setup.py install"

FOR LINUX:
- ffmpeg (  1) sudo add-apt-repository ppa:djcj/vlc-stable
            2) sudo apt-get update
            3) sudo apt-get upgrade
            4) sudo apt-get install ffmpeg  )

- ffmpeg libmp3lame library needed to convert to mp3 ( "sudo apt-get install ffmpeg libavcodec-extra-53" OR "sudo apt-get install ffmpeg libavcodec-extra-52")

FOR WINDOWS:
- Chocolatey Gallery (for ffmpeg) ( in admin command window: @powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin )
- ffmpeg ( choco install ffmpeg )
- openssl and https for requests ( pip install pyopenssl ndg-httpsclient pyasn1 )

