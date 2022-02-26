from PIL import Image, ImageDraw, ImageFont

image = Image.open('./test_image/001.png')
font_type = ImageFont.truetype(r'./front/ArialCE.ttf',18)
font_type_2 = ImageFont.truetype(r'./front/ArialCEBold.ttf',20)
font_type_3 = ImageFont.truetype(r'./front/ArialCEBoldItalic.ttf', 24)
# drawing text size
draw = ImageDraw.Draw(image)
draw.text(xy=(50,50), text="Your mark is 16 on 20", fill=(255,69,0), font=font_type, align ="right")
draw.text(xy=(0,0), text="Your wrong reponse is at the line ", fill=(255, 69,0), font=font_type_2)
draw.text(xy=(100, 100), text="From the rest is cool", fill=(255,69,0), font=font_type_3)
image.show()
