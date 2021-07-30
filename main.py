import cv2
import sys

from algorithm import walk_comp

run = True

def getInput():
    img_name = input('What is the name of the picture? ')

    work_with_txt = img_name.lower()
    if str('jpg') in work_with_txt and str('.') in work_with_txt:
        return img_name
    if work_with_txt == 'q' or work_with_txt == 'exit':
        return work_with_txt
    return ''

# for troubleshooting
def show_duplicated_pixels(list):
    counter = 0
    past_items = []
    for item in list:
        if item in past_items:
            counter += 1
        past_items.append(item)
    return counter

def collect_examined_pixels(valid_pixels):
    list = []

    for pos in valid_pixels:
        list.append(pos)

    return list

try:
    def on_click(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                examined_pixels = []
                valid_pixels = walk_comp(img, x, y, first = True)
                for item in valid_pixels:
                    last_return = walk_comp(img, item[1], item[0], first = False)
                    if examined_pixels:
                        for item_in in last_return:
                            if item_in not in examined_pixels:
                                valid_pixels.append(item_in)
                                examined_pixels.append(item_in)

                    else:
                        for item_in in last_return:
                            valid_pixels.append(item_in)
                            print('Original pixels ## ##')
                            print(valid_pixels)
                            examined_pixels.append(item_in)

                print('Output pixels ## ##')
                print(valid_pixels)
                print('TroubleShooting ## ##')
                print(f'Valid elements: {len(valid_pixels)}')
                print(f'There was/were: {show_duplicated_pixels(valid_pixels)} duplicants in the list.')

                print('Examined pixels ## ##')
                print(examined_pixels)

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