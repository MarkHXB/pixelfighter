import math

MAX_TOLARENCE = 40.0

def difference_between_two_pixel(color1, color2):
    r1 = color1[0]
    g1 = color1[1]
    b1 = color1[2]

    r2 = color2[0]
    g2 = color2[1]
    b2 = color2[2]
    try:
        d = math.sqrt( int(pow(r2 - r1, 2)) + int(pow(g2 - g1, 2)) + int(pow(b2 - b1, 2)) )
        p = d / math.sqrt( pow(255, 2) * 3 )
    except:
        print(color1, color2)

    return ( (p * 100) )

def compute_rgb(img, pos_y, pos_x, original_color):
    # 1.: szimpla max tolerenszes check az originalhoz képest
    # 2.: tolarenszes check + az elozohoz kepest check
    # 3.: még intelligensebb

    r = img[pos_y, pos_x, 0]
    g = img[pos_y, pos_x, 1]
    b = img[pos_y, pos_x, 2]
    rgb = (r, g, b)

    result = difference_between_two_pixel(color1=original_color, color2=rgb)

    return result

    #print(rgb)

def walk_examination(img, x, y,first):
    valid_pixels = []
    max_width = img.shape[1]
    max_height = img.shape[0]
    pos_x = x
    pos_y = y

    run = True

    checked_pixel = 0

    while run is True:
        if checked_pixel >= 8:
            run = False

        # center | starting pos
        if checked_pixel == 0 and first is True:
            valid_pixels.append((pos_y, pos_x))

        # 1 up | center top
        elif checked_pixel == 1:
            pos_y -= 1
            if pos_y - 1 >= -1:
                valid_pixels.append((pos_y, pos_x))

        # 1 left | left top corner
        elif checked_pixel == 2:
            pos_x -= 1
            if pos_x -1 >= -1:
                valid_pixels.append((pos_y, pos_x))

        # 1 down | left middle
        elif checked_pixel == 3:
            pos_y += 1
            if pos_y + 1 <= max_height:
                valid_pixels.append((pos_y, pos_x))

        # 1 down | left bottom corner
        elif checked_pixel == 4:
            pos_y += 1
            if pos_x >= -1 and pos_y <= max_height:
                valid_pixels.append((pos_y, pos_x))

        # 1 right | center bottom
        elif checked_pixel == 5:
            pos_x += 1
            if pos_x <= max_width and pos_y <= max_height:
                valid_pixels.append((pos_y, pos_x))

        # 1 right | right bottom corner
        elif checked_pixel == 6:
            pos_x += 1
            if pos_x <= max_width:
                valid_pixels.append((pos_y, pos_x))

        # 1 up | right middle
        elif checked_pixel == 7:
            pos_y -= 1
            if pos_x <= max_width:
                valid_pixels.append((pos_y, pos_x))

        # 1 up | right top corner
        elif checked_pixel == 8:
            pos_y -= 1
            if pos_y <= max_height and pos_x <= max_width:
                valid_pixels.append((pos_y, pos_x))

        checked_pixel += 1

    return valid_pixels


def walk_comp(img, x, y, first = True):
    valid_pixels = []

    # 1.: menj körbe és csekkold a színeket     COMPLETE
    # 2.: menj körbe és amelyik szín megfelel a tolerencnek az ok
    # 3.: menj körbe és - == - majd ahol megfelel a tolerensznek az abbol nyilo pixeleket szedd ki es nezd meg
    # 4.: ugyan ez csak itt mar addig menjen amig megfelel majd a vegen gyujtse ki mik voltak ezek

    """
    Part ..: 4 :..
    Két lépcsős lenne
    Végig menne az algoritmus a pixel szomszédjain és amik vizsgálhatóak
                                -> Vizsgálható: [  ]
    majd végig menne egy másik algoritmus a vizsgálhatókon, hogy abból kinyerje a tolerancia szabály szerint az adatokat, majd
    rekurzívan ezt az egészet, amíg el nem fogynak a vizsgálható területek
    """
    # Side step.: írd meg rekurzívra a walk algoritmust

    og_color = (img[y,x,0], img[y,x,1], img[y,x,2])
    examined = walk_examination(img,x,y,first)

    for pos in examined:
        pos_y = pos[0]
        pos_x = pos[1]
        df = compute_rgb(img,pos_y,pos_x,og_color)
        if df <= MAX_TOLARENCE:
            valid_pixels.append((pos_y,pos_x))

    return valid_pixels


