import os


def renameFiles(folderName):
  # (1) get all file names from a folder
  path = os.path.join(os.path.dirname(__file__), folderName)
  listDir = os.listdir(path)
  # (2) for each file, rename filename
  table = str.maketrans(dict.fromkeys('0123456789'))
  currentPath = os.getcwd()
  os.chdir(path)
  for fileName in listDir:
    print(fileName + " -> " + fileName.translate(table))
    os.rename(fileName, fileName.translate(table))
  os.chdir(currentPath)

renameFiles('prank')
