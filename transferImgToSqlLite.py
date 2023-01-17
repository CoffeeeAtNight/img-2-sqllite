import base64
from PIL import Image
import os
import sqlite3

foundLanguages = []
imagesAsB64 = []

# List all languages that exsist as folders
try:
  for langName in os.listdir('.'):
    if '.' not in langName:
      foundLanguages.append(langName)
except Exception:
  print("Failed to add folder names to language array!")


# Get all images from Filesystem and store as Base64 in Array
try:
  for fileName in os.listdir('.'):
    if fileName.endswith('.jpg') or fileName.endswith('.png'):
      with open(fileName, "rb") as imgObj:
        encodedString = base64.b64encode(imgObj.read()).decode('utf-8')
        imagesAsB64.append(encodedString)
except Exception:
  print("Failed to decode/add - img/base64 to image array!")


# Create table and add b64 string + languages to db instance
try:
  conn = sqlite3.connect('animeBookImages.db')
  cursor = conn.cursor()

  for lang in foundLanguages:
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {lang} (id INTEGER PRIMARY KEY, image TEXT)''')
    print(f"Created db table for language: {lang}")


  # TODO BUILD A OBJECT WITH LANG : IMAGES[] TO BETTER EXECUTE THE DB CURSORS!
  #for images in imagesAsB64:
  #  cursor.execute('''INSERT INTO imagesByLanguages(image) VALUES(?)''', (string_value,))
except Exception:
  print("Failed to commit languages and images to database instance!")

# Commit to and close db instance
conn.commit()
conn.close()


# Decode b64
#firstElem = imagesAsB64[0]
#decodedString = base64.b64decode(firstElem)
#with open("image.jpg", "wb") as image_file:
    #image_file.write(decodedString)