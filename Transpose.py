from PIL import Image
import os
import shutil

class grey:
    def __init__(self,imgPath , width, height, movePath):
        self.imgPath = imgPath
        self.width = width
        self.height = height
        self.movePath = movePath

        self.transpose()

    def transpose(self):
        if not os.path.exists(self.movePath):
            os.makedirs(self.movePath)

        img_list = os.listdir(self.imgPath)

        for img in img_list:
            img_path = os.path.join(self.imgPath, img)
            move_path = os.path.join(self.movePath, img)

            image = Image.open(img_path)
            resized_image = image.resize((width, height), Image.ANTIALIAS)
            resized_image.save(move_path)


if __name__ == '__main__':
    imgPath = r'F:\learnproject\信管2班'
    width = 180
    height = 240
    movePath = r'F:\learnproject\tow\wanc'

    grey(imgPath, width, height, movePath)
