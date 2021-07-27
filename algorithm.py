import math

MAX_TOLARENCE = 20.0

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

def walk(img,x,y):
    valid_pixels = []
    pixel_pos = (x,y)
    max_width = img.shape[1]
    max_height = img.shape[0]
    pos_x = x
    pos_y = y

    run = True

    checked_pixel = 0
    # 1.: menj körbe és csekkold a színeket     COMPLETE
    # 2.: menj körbe és amelyik szín megfelel a tolerencnek az ok
    # 3.: menj körbe és - == - majd ahol megfelel a tolerensznek az abbol nyilo pixeleket szedd ki es nezd meg
    # 4.: ugyan ez csak itt mar addig menjen amig megfelel majd a vegen gyujtse ki mik voltak ezek
    og_color = (img[y,x,0], img[y,x,1], img[y,x,2])
    while run is True:
        if checked_pixel >= 8:
            run = False

        # center | starting pos
        if checked_pixel == 0:
            df = compute_rgb(img,pos_y,pos_x,og_color)
            if df <= MAX_TOLARENCE:
                valid_pixels.append((pos_y,pos_x))

        elif checked_pixel == 1:
            pos_y -= 1
            if pos_y - 1 <= -1:
                pos_y = 0

            df = compute_rgb(img, pos_y, pos_x, og_color)
            if df <= MAX_TOLARENCE:

                valid_pixels.append((pos_y, pos_x))

        elif checked_pixel == 2:
            pos_x -= 1
            if pos_x -1 <= -1:
                pos_x = 0

            df = compute_rgb(img, pos_y, pos_x, og_color)
            if df <= MAX_TOLARENCE:
                valid_pixels.append((pos_y, pos_x))

        elif checked_pixel == 3:
            pos_y += 1
            if pos_y + 1 >= max_height:
                pos_y = max_height

            df = compute_rgb(img, pos_y, pos_x, og_color)
            if df <= MAX_TOLARENCE:
                valid_pixels.append((pos_y, pos_x))

        elif checked_pixel == 4:
            pos_y +=1
            df = compute_rgb(img, pos_y, pos_x, og_color)
            if df <= MAX_TOLARENCE:
                valid_pixels.append((pos_y, pos_x))

        elif checked_pixel == 5:
            pos_x += 1
            if pos_y >= max_height:
                pos_y = max_height
            df = compute_rgb(img, pos_y, pos_x, og_color)
            if df <= MAX_TOLARENCE:
                valid_pixels.append((pos_y, pos_x))

        elif checked_pixel == 6:
            pos_x += 1
            if pos_x >= max_width:
                pos_x = max_width
            df = compute_rgb(img, pos_y, pos_x, og_color)
            if df <= MAX_TOLARENCE:
                valid_pixels.append((pos_y, pos_x))

        elif checked_pixel == 7:
            pos_y -= 1
            df = compute_rgb(img, pos_y, pos_x, og_color)
            if df <= MAX_TOLARENCE:
                valid_pixels.append((pos_y, pos_x))

        elif checked_pixel == 8:
            pos_y -= 1
            if pos_y <= -1:
                pos_y = 0

            df = compute_rgb(img, pos_y, pos_x, og_color)
            if df <= MAX_TOLARENCE:
                valid_pixels.append((pos_y, pos_x))


        checked_pixel += 1

    return valid_pixels


