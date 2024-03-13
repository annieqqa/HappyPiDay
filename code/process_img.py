from PIL import Image, ImageDraw
image = Image.open('img/pi_card_img_green.jpeg')
# image = Image.open('img/pi_card_img_blue.png')
# image = Image.open('img/pi_img.jpg') #online photo
m = 162
n = 89-4

width, height = image.size
pixels = image.getdata()

def getAvgColor(im,w,h):
    totalColor=[0,0,0]
    pixels = im.getdata()
    for pixel in pixels:
        totalColor[0]+=pixel[0]
        totalColor[1]+=pixel[1]
        totalColor[2]+=pixel[2]
    
    avgColor= tuple(x//len(pixels) for x in totalColor)
    ret = Image.new(mode = "RGB", size = (w, h), color = avgColor)
    return ret, avgColor

def splitToGrid(image,m,n):
    hsv_image = image.convert("HSV")
    h, s, v = hsv_image.split()
    s = s.point(lambda x: x * 2) 
    adjusted_hsv_image = Image.merge("HSV", (h, s, v))
    image = adjusted_hsv_image.convert("RGB")
    
    width, height = image.size
    colWidth =  width // m
    rowHeight = height // n
    newSize = (colWidth * m, rowHeight * n)
    image = image.resize(newSize)
    width, height = image.size
    print(newSize)
    colors=[]
    
    for j in range(0, height, rowHeight):
        for i in range(0, width, colWidth):
            box = (i, j, i+colWidth, j+rowHeight)
            region = image.crop(box)
            grid = getAvgColor(region, colWidth, rowHeight)[0]
            colors.append(getAvgColor(region, colWidth, rowHeight)[1])
            Image.Image.paste(image, grid, box)
    return image, colors

def process():
    print("processing...")
    result=splitToGrid(image, m, n)
    return result[1]