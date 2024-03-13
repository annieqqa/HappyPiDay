from PIL import Image, ImageDraw
image = Image.open('img/pi_card_img.png')
hsv_image = image.convert("HSV")
h, s, v = hsv_image.split()
s = s.point(lambda x: x * 2)
adjusted_hsv_image = Image.merge("HSV", (h, s, v))
image = adjusted_hsv_image.convert("RGB")

image.show()