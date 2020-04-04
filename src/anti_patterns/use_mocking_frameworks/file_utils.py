import os


class FileUtils():

    def delete_file(self, path: str):
        os.remove(path)
