from PIL import Image

def imgdiff(img1, img2, img_name1, img_name2):
    N = 0
    new_image = Image.new("RGB", (img1.size[0], img1.size[1]), color=(255,255,255))

    for i in range(img1.size[0]):
        for j in range(img1.size[1]):
            if (img1.getpixel((i,j)) != img2.getpixel((i,j))):
                N += 1
                i1 = img1.getpixel((i,j))
                i2 = img2.getpixel((i,j))
                new_image.putpixel((i, j), tuple([i1[0]-i2[0],i1[1]-i2[1],i1[2]-i2[2]])) # for "RGB"
                # new_image.putpixel((i, j), tuple([i1-i2]))

    print("diff pixls = ", N) 
    print(f"{N*100/(img1.size[0]*img1.size[1]):.2f}%")

    new_image.show()
    new_image.save(f"for_{img_name1[:-4]}&{img_name2[:-4]}_diff={N*100/(img1.size[0]*img1.size[1]):.2f}%.png")


imageListwm = ['611wm-1.png', '611wm-2.png', '611wm-3.png', '611wm-4.png', '611wm-5.png']
imageList = ['611-1.png', '611-2.png', '611-3.png', '611-4.png', '611-5.png']

for i, im1 in enumerate(imageList):
    for j, im2 in enumerate(imageListwm):
        if i == j:
            img1 = Image.open(im1).convert("RGB")
            img2 = Image.open(im2).convert("RGB")
            imgdiff(img1, img2, im1, im2)