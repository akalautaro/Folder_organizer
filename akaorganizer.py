import os
import shutil

# Folder path to organize
path = 'C:\\Users\\danie\\Desktop\\Organizala\\'
print('Ingrese la carpeta a organizar con doble \ al final (alt + º)')
path = input()
if len(path) <= 1:
    path = 'C:\\Users\\danie\\Desktop\\Organizala\\'

# Extensions that works with the script (You can add whatever you want)
documents_ext = ['.docx', '.txt', 'doc', 'pptx', '.pdf', '.xls', 'xlsx']
videos_ext = ['.mov', '.mp4', '.avi', '.mkv', '.flv', '.wmv']
audios_ext = ['.mp3', '.wma', '.wav', '.flac']
photos_ext = ['.jpg', '.jpeg', '.ico', '.png', '.gif', '.psd', '.svg', '.tiff', '.bmp']
comp_ext = ['.zip', '.rar', '.rar5', '.7z', '.gz', '.ace']
exec_ext = ['.exe', '.msi']

# Functions
# Create folder before exec the script
def order(file, extension):
    # Check if the correspondent folder exists
    if os.path.isdir(path+'Documentos') == False:
        os.mkdir(path+'Documentos')
    for ext in documents_ext:
        if (extension == ext):
            shutil.move(path + file, path + 'Documentos')

    if os.path.isdir(path+'Videos') == False:
        os.mkdir(path+'Videos')
    for ext in videos_ext:
        if (extension == ext):
            shutil.move(path + file, path + 'Videos')

    if os.path.isdir(path+'Audio') == False:
        os.mkdir(path+'Audio')
    for ext in audios_ext:
        if (extension == ext):
            shutil.move(path + file, path + 'Audio')

    if os.path.isdir(path+'Fotos') == False:
        os.mkdir(path+'Fotos')
    for ext in photos_ext:
        if (extension == ext):
            shutil.move(path + file, path + 'Fotos')

    if os.path.isdir(path+'Comprimidos') == False:
        os.mkdir(path+'Comprimidos')
    for ext in comp_ext:
        if (extension == ext):
            shutil.move(path + file, path + 'Comprimidos')

    if os.path.isdir(path+'Ejecutables') == False:
        os.mkdir(path+'Ejecutables')
    for ext in exec_ext:
        if (extension == ext):
            shutil.move(path + file, path + 'Ejecutables')

    if (extension != ''):
        if os.path.isdir(path+'Otros') == False:
            os.mkdir(path+'Otros')
        try:
            shutil.move(path + file, path + 'Otros')
        except:
            pass

def main():
    print('Iniciando\n')

    if len(path) > 1:
        for file in os.listdir(path):
            try:
                ext = os.path.splitext(file)[1]
                order(file, ext)
            except Exception as e:
                print(f'No se pudo mover el archivo {file}')
                print(e)
        print('Proceso finalizado')

if __name__ == '__main__':
    main()