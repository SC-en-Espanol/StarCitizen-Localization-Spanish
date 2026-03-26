import os
import zipfile
import shutil

####
# Crear un release de la versión actual
#
# Pasos:
# 1. Crear un zip llamado "SC_Spanish.zip" con:
#   - El archivo de configuración, "user.cfg"
#   - El archivo de traducción,
#     incluida su estructura de carpetas, "data/Localization/spanish_(spain)/global.ini"
# 2. Copiar el "data/Localization/spanish_(spain)/global.ini" a "Tools/scripts/release/" como "global.ini.es_ES"

fileUser = "user.cfg"
toolsPath = "Tools\\scripts\\release"

fileSpanish = "data/Localization/spanish_(spain)/global.ini"
zipName = "SC_Spanish.zip"
zipPath = os.path.join(os.getcwd(), f"{toolsPath}\\{zipName}")
zipFiles = [fileUser, fileSpanish]

fileSpanishASCII = "data/Localization/spanish_(spain)/global.ascii.ini"
zipNameASCII = "SC_Spanish_ASCII.zip"
zipPathASCII = os.path.join(os.getcwd(), f"{toolsPath}\\{zipNameASCII}")
zipFilesASCII = [fileUser, fileSpanishASCII]



print(zipPath)

# 1. Crear un zip llamado "SC_Spanish.zip" en "Tools/scripts/release/"
print("Creating normal zip file...")
with zipfile.ZipFile(zipPath, "w", zipfile.ZIP_DEFLATED) as zip:
    for file in zipFiles:
        zip.write(file)
print("Normal Zip file created!")
print("Creating ASCII zip file...")
with zipfile.ZipFile(zipPathASCII, "w", zipfile.ZIP_DEFLATED) as zip:
    for file in zipFilesASCII:
        zip.write(file)
print("ASCII ip file created!")


# # 2. Copiar el "data/Localization/spanish_(spain)/global.ini" a "Tools/scripts/release/" como "global.ini.es_ES"
# print("Copying normal global.ini...")
# shutil.copyfile(fileSpanish, f"{toolsPath}\\global.es_ES.ini")
# print("normal global.ini copied!")
# print("Copying normal global.ini...")
# shutil.copyfile(fileSpanish, f"{toolsPath}\\global.es_ES.ascii.ini")
# print("normal global.ini copied!")
