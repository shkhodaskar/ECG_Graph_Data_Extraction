import cv2

def convert(file):
    img = file
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 15, cv2.THRESH_BINARY)
    img[thresh > 1] = 255
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
    erosion = cv2.erode(img, kernel, iterations = 1)
    return erosion
    '''
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow("image", erosion)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    imageName = 'gray_{}.png'.format(file.split('.')[0])
    #print(imageName)
    cv2.imwrite(imageName, gray)
    #cv2.imshow('Gray Image', gray)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
'''