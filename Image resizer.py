# Image Resizing using Pillow library 

from PIL import Image

def resize_image(length, breath):
    image = Image.open("#IMAGENAME") 
    resized_image = image.resize((length, breath))
    resized_image.save(newname + ".jpg")

newname = input("Enter new name of file: ")
length = int(input("Enter length: "))
breath = int(input("Enter breath: "))
resize_image(length, breath)
print(f'A new file by the name {newname} is saved, Thank you using me.')
