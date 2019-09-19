import os
import glob
import shutil

# shutil.move(premier argument un fichier , deuxieme arguments un dossier)
# mp3, wav : Musique
# mp4, mov : Videos
# jpg, jpeg, png : Images
# pdf : Documents


chemin = "/Users/jodo/Documents/pythonCourse/exo/exo4/tri_fichiers_sources/**"
chemin2 = "/Users/jodo/Documents/pythonCourse/exo/exo4/tri_fichiers_sources"
files = glob.glob(chemin, recursive=True)
print(files)
for f in files:
    if f.endswith("jpg") or f.endswith("jpeg") or f.endswith("png"):
        ds= os.path.join(chemin2,"ImagesDs")
        if not os.path.exists(ds):
            os.makedirs(ds)
            shutil.move(f,ds)
        else:
            shutil.move(f,ds)
    elif f.endswith("pdf") :
        ds= os.path.join(chemin2,"PdfDs")
        if not os.path.exists(ds):
            os.makedirs(ds)
            shutil.move(f,ds)
        else:
            shutil.move(f,ds)
    elif f.endswith("mp3") or f.endswith("wav"):
        ds= os.path.join(chemin2,"MusiquesDs")
        if not os.path.exists(ds):
            os.makedirs(ds)
            shutil.move(f,ds)
        else:
            shutil.move(f,ds)
    elif f.endswith("mp4") :
        ds= os.path.join(chemin2,"VideoDs")
        if not os.path.exists(ds):
            os.makedirs(ds)
            shutil.move(f,ds)
        else:
            shutil.move(f,ds)
    elif f.endswith("json") :
        ds= os.path.join(chemin2,"JsonDs")
        if not os.path.exists(ds):
            os.makedirs(ds)
            shutil.move(f,ds)
        else:
            shutil.move(f,ds)   




import os
from glob import glob
import shutil

chemin = "/Users/thibh/trier_fichiers/sources"

extensions = {".mp3": "Musique",
              ".wav": "Musique",
              ".mp4": "Videos",
              ".mov": "Videos",
              ".jpeg": "Images",
              ".jpg": "Images",
              ".png": "Images",
              ".pdf": "Documents"}

fichiers = glob(os.path.join(chemin, "*"))
for fichier in fichiers:
    extension = os.path.splitext(fichier)[-1]
    dossier = extensions.get(extension)
    if dossier:
        chemin_dossier = os.path.join(chemin, dossier)
        os.makedirs(chemin_dossier, exist_ok=True)
        shutil.move(fichier, chemin_dossier)
