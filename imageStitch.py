import cv2
from imageToGray import convert
from PIL import Image
import numpy as np
def offsetFix(r):
    return 1535 + (r * 1800)

def saveImage(name, image, cropped_images):
    print(cropped_images)
    image_list = []
    for i in range(len(cropped_images)):
        start_col, end_col, start_row, end_row = cropped_images[i]
        cropped_image = image[start_col:end_col, start_row:end_row]
        img = f'./combine/image{i}.png'
        #cv2.imwrite(img, cropped_image)
        processed = convert(cropped_image)
        cv2.imwrite(img, processed)
        image_list.append(img)
        #cv2.namedWindow("cropped-image", cv2.WINDOW_NORMAL)
        #cv2.resizeWindow('cropped-image', 800,800)
        #cv2.imshow('cropped-image', cropped_image)
        #cv2.waitKey(2000)
    return image_list

def combine(images):
    imgs = [Image.open(i) for i in images]
    min_shape = sorted([(np.sum(i.size), i.size) for i in imgs])[0][1]
    imgs_combine = np.hstack((np.asarray(i.resize(min_shape))) for i in imgs)
    imgs_combine = Image.fromarray(imgs_combine)
    imgs_combine.save("continuousECG.png")

def stitch(file):
    image = cv2.imread(file)
    print(image.shape)
    start_row, start_col = int(238), int(1535)
    end_row, end_col = int(6238), int(2135)
    cropped_images = []
    for i in range(0,4):
        y = offsetFix(i)
        start_row, start_col = 238, y
        end_row, end_col = 238 + 6000, y + 600
        cropped_images.append((start_col, end_col, start_row, end_row))
    imgs = saveImage('s',image,cropped_images)
    combine(imgs)
stitch("ecg2.png")
