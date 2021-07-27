import cv2
import sys

from algorithm import walk

run = True

def getInput():
    img_name = input('What is the name of the picture? ')

    work_with_txt = img_name.lower()
    if str('jpg') in work_with_txt and str('.') in work_with_txt:
        return img_name
    if work_with_txt == 'q' or work_with_txt == 'exit':
        return work_with_txt
    return ''

try:
    def on_click(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            valid_pixels = walk(img,x ,y)
            print(valid_pixels)

    while run is True:
        #img_name = getInput() real one

        img_name = 't.jpg' # test
        if img_name != '':
            img = cv2.imread(f'{img_name}', cv2.IMREAD_UNCHANGED)

            scale_percent = 60 # percent of the original size
            dim = (600, 600)
            resized = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)

            cv2.imshow('image', resized)
            cv2.namedWindow('image')
            cv2.setMouseCallback('image',on_click)

            cv2.waitKey(0)
            cv2.destroyAllWindows()

            run = False


        elif img_name == 'exit' or img_name == 'q':
            run = False

        else:
            continue


except ValueError:
    print("Could not convert data to the expected value.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    sys.exit(1)
    raise