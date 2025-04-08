import sys
import tarfile
import gzip


class Compresseur_tar_gz:


    @staticmethod
    def compresser_tar_gz(nom_archive, fichiers):
        # Compresse les fichiers dans un fichier tar.gz
        # le w:gz indique que le fichier sera compressé avec gzip
        with tarfile.open("./output/" + nom_archive, "w:gz") as tar:
            for fichier in fichiers:
                tar.add(fichier)
                print(f"Ajouté {fichier} au fichier compressé {nom_archive}")

    @staticmethod
    def compresser_deux_etapes(nom_archive, fichiers):
        # Compresse les fichiers dans un fichier tar
        with tarfile.open("./output/" + nom_archive, "w") as tar:
            for fichier in fichiers:
                tar.add(fichier)
                print(f"Ajouté {fichier} au fichier compressé {nom_archive}")

        # Compresse le fichier tar avec gzip
        with open("./output/" + nom_archive, "rb") as f_in:
            with gzip.open("./output/" + nom_archive + ".gz", "wb") as f_out:
                f_out.writelines(f_in)
                print(f"Compressé {nom_archive} en {nom_archive}.gz")

    @staticmethod
    def decompresser(nom_archive):
        with tarfile.open("./output/" + nom_archive, "r:gz") as tar:
            tar.extractall(path= "./output", filter="data")
            print(f"Décompressé {nom_archive}")

    @staticmethod
    def decompresser_deux_etapes(nom_archive):
        # Décompresse le fichier tar.gz
        with gzip.open("./output/" + nom_archive, "rb") as f_in:
            with open("./output/" + nom_archive[:-3], "wb") as f_out:
                f_out.writelines(f_in)
                print(f"Décompressé {nom_archive} en {nom_archive[:-3]}")

        # Décompresse le fichier tar
        with tarfile.open("./output/" + nom_archive[:-3], "r") as tar:
            tar.extractall(path="./output", filter="data")
            print(f"Décompressé {nom_archive[:-3]}")


if __name__ == "__main__":
    fichiers_a_compresser = ["hachage.py", "tas_operations.py", "compression.py"]

    Compresseur_tar_gz.compresser_tar_gz("test.tar.gz", fichiers_a_compresser)
    Compresseur_tar_gz.compresser_deux_etapes("test_deux_etape.tar", fichiers_a_compresser)
    Compresseur_tar_gz.decompresser("test.tar.gz")
    Compresseur_tar_gz.decompresser_deux_etapes("test_deux_etape.tar.gz")
