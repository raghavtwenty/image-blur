'''
Application Name: Image blurring
Author : Raghav, Kendriya Vidyalaya, Coimbatore. [2021]
Github ID : @raghavtwenty
Created On: July 25, 2021 | Last Modified On: July 25, 2021
Version Info: 1.0
'''


# Importing required libraries
from PIL import Image, ImageFilter


# image location from user input
loc = str(input("\nEnter the image(.jpg) location : "))
pix_blur = int(input("Enter the blur pixel size (integer) : "))

# open the image 
op_img = Image.open(loc,'r')

# processing
blurred = op_img.filter(ImageFilter.BoxBlur(pix_blur))

# save the new image to same location
loc = loc.split(".")
print(loc[0])
blurred.save(loc[0]+"-EDITED.jpg")

print("\nPROCESS COMPLETE\n")
print(f"Image saved in the location : {loc[0]}-EDITED.jpg")