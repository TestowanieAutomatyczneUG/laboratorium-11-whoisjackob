import os


class File:

    def open(self, path):
        plik = open(path, "r")
        content = plik.read()
        plik.close()

        return content

    def edit(self, path, text):
        plik = open(path, "w")
        plik.write(text)
        plik.close()

    def delete(self, path):
        if os.path.exists(path):
            os.remove(path)
        else:
            raise Exception("Nie znaleziono")
