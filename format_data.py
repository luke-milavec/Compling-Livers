import numpy as np
import cv2
import PIL
from PIL import Image
import os
import config

directory = 'Files for Capstone'
count = 1
for filename in os.listdir(directory):
    f1 = os.path.join(directory, filename,"Live","GATA6_Dox_20221225_Pos_"+filename[3:]+"_t_0096_470.tif")
    f2 = os.path.join(directory, filename,"Fixed","GATA6_Dox_20221225_IFImaging_ReImage_Pos_"+filename[3:]+"_625.tif")
    r1 = cv2.imread(f1)
    r2 = cv2.imread(f2)
    f1 = f1.split('.')[0] + '.png'
    f2 = f2.split('.')[0] + '.png'
    cv2.imwrite(f1,r1)
    cv2.imwrite(f2,r2)
    images = [Image.open(x) for x in [f1,f2]]
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for im in images:
        new_im.paste(im, (x_offset,0))
        x_offset += im.size[0]
    
    if count < 20:
        new_im.save(os.path.join(config.TRAIN_DIR, str(count)+".png"))
    else:
        new_im.save(os.path.join(config.VAL_DIR, str(count-19)+".png"))
    count+=1