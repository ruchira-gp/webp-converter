import os
from PIL import Image
for filename in os.listdir("images"):
    img=Image.open("images/"+filename)
    img.save("Converted_Files/"+os.path.splitext(filename)[0]+".webp","webp")

print("conversion completed")
