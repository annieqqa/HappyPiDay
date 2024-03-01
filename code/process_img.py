from PIL import Image, ImageDraw
image = Image.open('img/pi_img.jpg') #size 817*980
m = 162
n = 89-4

width, height = image.size
pixels = image.getdata()
print(width,height)

def getAvgColor(im,w,h):
    totalColor=[0,0,0]
    pixels = im.getdata()
    for pixel in pixels:
        totalColor[0]+=pixel[0]
        totalColor[1]+=pixel[1]
        totalColor[2]+=pixel[2]
    avgColor= tuple(x//len(pixels) for x in totalColor)
    # h, s, v = colorsys.rgb_to_hsv
    # newAvgColor = tuple()
    ret = Image.new(mode = "RGB", size = (w, h), color = avgColor)
    # print(ret.size)
    return ret, avgColor

def splitToGrid(image,m,n):
    width, height = image.size
    colWidth =  width // m
    rowHeight = height // n
    newSize = (colWidth * m, rowHeight * n)
    image = image.resize(newSize)
    width, height = image.size
    print(newSize)
    colors=[]
    
    for j in range(0, height, rowHeight):
        # gridColors=[]
        for i in range(0, width, colWidth):
            box = (i, j, i+colWidth, j+rowHeight)
            # print(i,j)
            region = image.crop(box)
            # print(region.size)
            grid = getAvgColor(region, colWidth, rowHeight)[0]
            colors.append(getAvgColor(region, colWidth, rowHeight)[1])
            Image.Image.paste(image, grid, box)
        # colors.append(gridColors)
    # region.show()
    return image, colors

def process():
    result=splitToGrid(image, m, n)
    return result[1]

result = process()
# print(len(result[1]), len(result)) #164 * 90 (wrong) VS 162* 89 (right)
#test: construct processed image
# newImg=result[0]
# newImg.show()