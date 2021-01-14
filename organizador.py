import os
import shutil

# Aquí colocas tu ruta de descargas
# route_downloads = 'C:\\Users\\danie\\Downloads\\'
route_downloads = 'C:\\Users\\danie\\Desktop\\Organizala\\'

# Si quieres puedes agregar mas extensiones, como .bat, .ttf, .py, etx
text_extensions = ('.txt', '.doc', '.docx', 'pptx', '.odf', '.docm', '.pdf', 'xlsx')
video_extensions = ('.mov', '.mp4', '.avi', '.mkv', '.mkv', '.flv', '.wmv')
audio_extensions = ('.mp3', '.wma', '.wav', '.flac')
photo_extensions = ('.jpg', '.png', 'jpeg', '.gif', '.tiff', '.psd', '.bmp', '.ico', '.svg')
compressed_extensions = ('.zip', '.rar', '.rar5', '.7z', '.ace', '.gz')
executable_extensions = ('.exe', '.msi')

# Cree las carpetas antes de ejecutar, si no, puede usar el módulo mkdir(), de os
def order(file, extension):

    for etx in text_extensions:
        if os.path.isdir(route_downloads+'Documentos') == False:
            os.mkdir(route_downloads+'Documentos')
        if extension == etx:
            shutil.move(route_downloads + file, route_downloads + 'Documentos')
    # for etx in video_extensions:
    #     if extension == etx:
    #         shutil.move(route_downloads + file, route_downloads + 'Videos')
    # for etx in audio_extensions:
    #     if extension == etx:
    #         shutil.move(route_downloads + file, route_downloads + 'Audios')
    # for etx in photo_extensions:
    #     if extension == etx:
    #         shutil.move(route_downloads + file, route_downloads + 'Imagenes')
    # for etx in compressed_extensions:
    #     if extension == etx:
    #         shutil.move(route_downloads + file, route_downloads + '\Comprimidos')
    # for etx in executable_extensions:
    #     if extension == etx:
    #         shutil.move(route_downloads + file, route_downloads + 'Ejecutables')
    # if extension != '':
    #     try:
    #         shutil.move(route_downloads + file, route_downloads + 'Otros')
    #     except Exception as e:
    #         print(e)

    
def main():
    print('Iniciando\n')
    for file in os.listdir(route_downloads):
        try:
            etx = os.path.splitext(file)[1]
            order(file, etx)
        except Exception as e:
            print('No se puedo mover el archivo {}\n'.format(file))
            print(e)
    print('Proceso terminado')


if __name__ == '__main__':
    main()