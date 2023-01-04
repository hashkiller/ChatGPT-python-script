import pyi_importers
import pyi_archive
import pyi_carchive

def decompile(exe_path: str, dst_dir: str):
    # Ouvrir l'exécutable PyInstaller
    with open(exe_path, 'rb') as f:
        exe = f.read()

    # Extraire l'archive Python à partir de l'exécutable
    importer = pyi_importers.Importer(exe)
    if not importer.is_package():
        # L'exécutable n'est pas un package, donc il s'agit d'une archive C
        carchive = pyi_carchive.CArchive(importer)
        pyi_archive.extract_pyz(carchive, dst_dir)
    else:
        # L'exécutable est un package, donc il s'agit d'une archive Python
        pyz = pyi_archive.ZlibArchive(importer)
        pyi_archive.extract_pyz(pyz, dst_dir)

# Utilisation de la fonction de décompilation
decompile("mon_programme.exe", "dossier_de_sortie")