<h1 align="center">YT_Downloader</h1>
<p align="center"> descargador de videos y musicas de youtube en alta calidad</p>
<p align="center"><img src="https://cdn.computerhoy.com/sites/navi.axelspringer.es/public/media/image/2021/09/youtube-ya-permite-usar-opcion-demandada-usuarios-toda-historia-2479961.jpg?tf=600x"/></p> 

## primero actualizamos los paquetes
    apt update && apt upgrade -y

## instalamos git
    pkg install git  
## instalamos python3
    pkg install python3
## instalamos libexpat
    pkg install libexpat
## instalamos openssl
    pkg install openssl
## instalamos pytube
    pip install pytube
## instalamos colorama
    pip install colorama
## instalamos tqdm
    pip install tqdm
## instalamos moviepy
    pip install moviepy
## repositorio
    git clone https://github.com/whit3moonlight/YT_Downloader.git

## Navega al directorio:
    cd YT_Downloader
    
## Establecer permisos:
    chmod +x yt_Downloader.py
    
## Ejecutar el script:
    python yt_Downloader.py


