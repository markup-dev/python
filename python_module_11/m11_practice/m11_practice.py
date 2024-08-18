from PIL import Image, ImageDraw, ImageFont


def new_photo(name, k):
	image = Image.open(name)
	width, height = image.size
	return image.resize((width // k, height // k))


im = new_photo('phoenix.jpg', 2)
im_2 = new_photo('gojo.jpg', 5)

w, h = im.size

im.paste(im_2, (w - 170, h - 170))

draw = ImageDraw.Draw(im)
font = ImageFont.truetype('monotypecorsiva.ttf', 50)
draw.text((190, 50), 'monolith', 'black', font=font)

im.show('MyPhoto')
