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
    imgPath = r'这里放图片文件夹路径'
    width = 180 #需要转换的像素
    height = 240  #需要转换的像素
    movePath = r'图片转换完成后自动移动到此文件夹'

    grey(imgPath, width, height, movePath)
