import os
from pytube import YouTube
from colorama import Fore, Style, init
from tqdm import tqdm
from datetime import datetime

init()

def print_large_yt_downloader():
    if os.name == 'nt':
        print("YT Downloader")
    else:
        print(Fore.GREEN + "┌───────────────────────────────────────────────┐" + Style.RESET_ALL)
        print("\t" + Fore.YELLOW + "Y" + Fore.BLUE + "T_" + Fore.GREEN + "Downloader" + "\t\tby_white" + Style.RESET_ALL)

def print_colored(message, color):
    print(color + message + Style.RESET_ALL)

def download_video(video_url):
    try:
        yt = YouTube(video_url)
        video_stream = yt.streams.get_highest_resolution()
        video_filename = f"video_{datetime.now().strftime('%Y%m%d%H%M%S')}.mp4"

        print_colored("Descargando video...", Fore.CYAN)
        video_stream.download(filename=video_filename)
        print_colored("Descarga de video completada.", Fore.GREEN)
        print_colored("Descarga completada.", Fore.GREEN)
        input("Presione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception as e:
        print_colored("Ocurrio un error: " + str(e), Fore.RED)

def download_audio(video_url):
    try:
        yt = YouTube(video_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_filename = f"audio_{datetime.now().strftime('%Y%m%d%H%M%S')}.mp3"

        print_colored("Descargando audio...", Fore.CYAN)
        audio_stream.download(filename=audio_filename)
        print_colored("Descarga de audio completada.", Fore.GREEN)
        print_colored("Descarga completada.", Fore.GREEN)
        input("Presione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception as e:
        print_colored("Ocurrio un error: " + str(e), Fore.RED)

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print_large_yt_downloader()

    while True:
        print_colored("Seleccione una opcion:", Fore.YELLOW)
        print("1 - Descargar video")
        print("2 - Descargar audio del video")
        print("3 - Salir")
        option = input(Fore.RED + "Ingresa el numero de la opcion: " + Style.RESET_ALL)
        if option == "1":
            video_url = input(Fore.RED + "Introduce el enlace del video de YouTube: " + Style.RESET_ALL)
            download_video(video_url)
        elif option == "2":
            video_url = input(Fore.RED + "Introduce el enlace del video de YouTube: " + Style.RESET_ALL)
            download_audio(video_url)
        elif option == "3":
            break
        else:
            print_colored("Opcion no valida, por favor seleccione una opcion valida.", Fore.RED)
