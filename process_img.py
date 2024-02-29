from PIL import Image, ImageDraw
image = Image.open('pi_img.jpg') #size 817*980
m = 147
n = 83

width, height = image.size
pixels = image.getdata()
print(width,height)

#just realised that i did this for nothing :D

def getAvgColor(im,w,h):
    totalColor=[0,0,0]
    pixels = im.getdata()
    for pixel in pixels:
        totalColor[0]+=pixel[0]
        totalColor[1]+=pixel[1]
        totalColor[2]+=pixel[2]
    avgColor= tuple(x//len(pixels) for x in totalColor)
    ret = Image.new(mode = "RGB", size = (w, h), color = avgColor)
    # print(ret.size)
    return ret, avgColor

def splitToGrid(image,m,n):
    width, height = image.size
    colWidth =  width // m
    rowHeight = height // n
    colors=[]
    
    for j in range(0, height, rowHeight):
        for i in range(0, width, colWidth):
            box = (i, j, i+colWidth, j+rowHeight)
            # print(i,j)
            region = image.crop(box)
            # print(region.size)
            grid = getAvgColor(region, colWidth, rowHeight)[0]
            colors.append(getAvgColor(region, colWidth, rowHeight)[1])
            Image.Image.paste(image, grid, box)
    # region.show()
    return image, colors

def process():
    result=splitToGrid(image, m, n)
    return result[1]

#test: construct processed image
# newImg=
# newImg.show()