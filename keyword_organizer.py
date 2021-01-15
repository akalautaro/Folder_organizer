import os
import shutil

print('Iniciando...\n')

# Folder path to organize
path = ''
while len(path) <= 1:
    print('Ingresa la ruta de la carpeta en que vamos a trabajar:\n')
    path = input()
    path = path + '\\'

def main():
    # Keyword to search
    keyword = ''
    while (len(keyword) <= 1):
        print('Ingresa la palabra clave para ordenar: ')
        keyword = input()
        keyword = (str(keyword))
        keyword = keyword.lower()

    # Create a folder if you want. If you skip, this creates a folder with the name of the keyword
    if len(path) > 1:
        folder_keyword = input('Ingresa el nombre de la carpeta a crear (Presiona Enter para skip este paso):\n')
        folder_keyword_flag = False
        if len(folder_keyword) > 0:
            # Check if the folder exist
            if os.path.isdir(path+folder_keyword) == False:
                # Create the folder it it doesnt exist
                os.mkdir(path+folder_keyword)
                folder_keyword_flag = True
            else:
                folder_keyword_flag = True
        elif len(folder_keyword) == 0:
            os.mkdir(path+keyword)
            folder_keyword_flag = False
        for file in os.listdir(path):
            try:
                name_file = (os.path.splitext(file)[0]).lower()
                ext_file = (os.path.splitext(file)[1]).lower()
                if (keyword in name_file) and len(ext_file) > 0:
                    if folder_keyword_flag == True:
                        shutil.move(path + file, path + folder_keyword)
                    else:
                        shutil.move(path + file, path + keyword)
            except Exception as e:
                print(f'Error :( / {e}')
        print(f'Ordenamiento con {keyword} finalizado')

if __name__ == '__main__':
    main()