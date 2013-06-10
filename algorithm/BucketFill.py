class Pix(object):
	def __init__(self, x, y, color=0):
		self.x = x
		self.y = y
		self.color = color
	def toString(self):
		return self.color

def bucketFill(img, x, y, color, orig=None):
	if x < 0 or y < 0 or x >= len(img) or y >= len(img[0]):
		return
	if orig is None:
		orig = img[x][y]
	if img[x][y] == orig:
		img[x][y] = color
		bucketFill(img, x-1, y, color, orig)
		bucketFill(img, x+1, y, color, orig)
		bucketFill(img, x, y-1, color, orig)
		bucketFill(img, x, y+1, color, orig)

def printImg(img):
	print '---'
	for x in xrange(0, len(img)):
		for y in xrange(0, len(img[x])):
			print img[x][y],
		print

if __name__ == '__main__':
	img = [
			[0,0,0,0],
			[0,0,0,0],
			[0,0,0,0],
			[0,0,0,0],
			[0,0,0,0],
			]
	printImg(img)
	bucketFill(img, 2, 3, 1)
	printImg(img)

	img = [
			[2,2,0,2,2,2,0,2],
			[2,0,2,0,0,0,2,0],
			[0,0,2,0,2,0,2,0],
			[2,0,2,0,2,0,2,0],
			[0,0,0,0,2,0,0,0],
			]
	printImg(img)
	bucketFill(img, 1, 1, 1)
	printImg(img)
