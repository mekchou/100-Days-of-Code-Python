import colorgram as cg


def rbg_list(color_obj):
    rgb = []
    # length = len(color_obj)
    
    for color in color_obj:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb.append(new_color)
    
    # for num in range(length):
        # rgb.append(color_obj[num].rgb)
    
    # rgblist = [None for _ in range(len(rgb))]
    
    # for num in range(len(rgb)):
        # for ind in range(3):
        # rgblist[num] = (rgb[num][0], rgb[num][1], rgb[num][2])
        
    
    return rgb

colors = cg.extract(r"V:\100-Days-of-Code-Python\data\HirstSpot.jpg",40)

print(rbg_list(colors))


# print(colors)