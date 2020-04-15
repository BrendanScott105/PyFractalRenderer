##################################################################
################### START FUNCTION DEFINITIONS ###################
##################################################################



def IterativeFunction(brot, ship, tri, julia, buddha, real, imag, iters, length, height, power, pixelspacing, currentrealpos, currentimagpos, 
buddhaposx, buddhaposy, buddhacount, buddhay, buddhax, imgx, imgy, xpostable, ypostable, x):
	global result
	global counter
	global repeatcount
	global c
	counter = 0
	if julia == False:
		c = complex(currentrealpos, currentimagpos) #complex number used when --julia arg not present
	if julia:
		x = complex(currentrealpos, 0-currentimagpos)
		c = complex(real[0], imag[0]) #Sets complex numbers if julia set is rendered
	for a in range(0,round(iters[0])): #Loops for n amounts [iteration count]
		if brot or julia:
			(result) = pow((x),power[0])+(c) #Mandelbrot set formula
		if tri:
			(result) = ((pow((x),power[0])).conjugate())+(c) #Tricorn formula
		if ship:
			(result) = pow(abs(x.real) + 1j*(abs(x.imag)),power[0]) + (c) #Burning ship formula
		if vlambda:
			(result) = ((pow((x),power[0]))*-c)+c
		if PerpBrot:
			(result) = pow(abs(x.real)-(1j*x.imag), power[0])+c
		(x) = (result)
		(counter) = (counter) + 1
		(real2) = x.imag
		(repeatcount) = (repeatcount) + 1 #Sets variables up and prepares for another iteration
		if buddha:
			while x.real >= buddhaposx:
				buddhaposx = buddhaposx + pixelspacing
				buddhacount = buddhacount + 1
			xpostable[repeatcount - 1] = buddhacount
			buddhacount = 0
			while x.imag >= buddhaposy:
				buddhaposy = buddhaposy + pixelspacing
				buddhacount = buddhacount + 1
			ypostable[repeatcount - 1] = buddhacount
			buddhacount, buddhaposx, buddhaposy = 0, 0 - (pixelspacing * (length[0] / 2)), 0 - (pixelspacing * (height[0] / 2)) #Prepares for buddhabrot array modification
		if pow(x.real, 2) + pow(real2, 2) > 4: break # Determines escape values quicker

def Coloring(decolorize, edge, buddha, iters, length, height, arraytransfercount, xpostable, ypostable, incamount, c):
	global result
	global counter
	global color
	global repeatcount
	global counterval
	if buddha and counter != iters[0]:
		for a in range(0, repeatcount):
			if xpostable[round(arraytransfercount)] < length[0] and xpostable[round(arraytransfercount)] > 0 and ypostable[round(arraytransfercount)] < height[0] and ypostable[round(arraytransfercount)] > 0:
				r = colorarray[round(xpostable[round(arraytransfercount)] + (length[0] * ypostable[round(arraytransfercount)]))]
				if r < 255:
					r = r + incamount
				else:
					r = 0
				colorarray[round(xpostable[round(arraytransfercount)] + (length[0] * ypostable[round(arraytransfercount)]))] = colorarray[round(xpostable[round(arraytransfercount)] + (length[0] * ypostable[round(arraytransfercount)]))] + r
			arraytransfercount = arraytransfercount + 1 #Adds values to buddhabrot and dynamically changes incrementation amounts across different iter values
	arraytransfercount, repeatcount = 0, 0
	if buddha == False:
		if abs(result) <= 2 and grayscale == False: #Colors the set black when needed
			color = "black"
		else:
			if abs(result) <=2 and (grayscale or invedge):
				color = "white"
			else:
				if decolorize:
					(color) = "white" #In case of decolorize argument, the exterior colors will be set to white
				else:
					if counterval != counter and edge and smooth == False: #Detects if a change in the iteration values exists, and if so, a white color will be displayed
						color = "white" 
						counterval = counter
					if counterval != counter and invedge and smooth == False: #Detects if a change in the iteration values exists, and if so, a black color will be displayed
						color = "black" 
						counterval = counter
					if edge == False and invedge == False and smooth == False: #Determines point color with table
						(modulus) = (counter) % 8
						colorlookup = ["Black", "Red", "Orange", "Yellow", "Green", "Blue", "Violet", "Gray"]
						(color) = colorlookup[modulus]
					if edge and counterval == counter and color == 0 and smooth == False: #Chooses black if no iter change is present
						color = "black"
						counterval = counter
					if invedge and counterval == counter and color == 0 and smooth == False: #Chooses white if no iter change is present
						color = "white"
						counterval = counter
					if invgrayscale and smooth == False:
						color = (math.floor(255 - counter * (255/iters[0])), math.floor(255 - counter * (255/iters[0])), math.floor(255 - counter * (255/iters[0])))
					if grayscale and smooth == False:
						color = (math.floor(counter * (255/iters[0])), math.floor(counter * (255/iters[0])), math.floor(counter * (255/iters[0])))
					if smooth:
						colorlookupsmooth = ["#0000FF", "#0500F9", "#0A00F4", "#0F00EF", "#1400EA", "#1900E5", "#1E00E0", "#2300DB", "#2800D6", "#2D00D1", "#3300CC", "#3800C6", "#3D00C1", "#4200BC", "#4700B7", "#4C00B2", "#5100AD", "#5600A8", "#5B00A3", "#60009E", "#660099", "#6B0093", "#70008E", "#750089", "#7A0084", "#7F007F", "#84007A", "#890075", "#8E0070", "#93006B", "#990066", "#9E0060", "#A3005B", "#A80056", "#AD0051", "#B2004C", "#B70047", "#BC0042", "#C1003D", "#C60038", "#CC0032", "#D1002D", "#D60028", "#DB0023", "#E0001E", "#E50019", "#EA0014", "#EF000F", "#F4000A", "#F90005"]
						color = colorlookupsmooth[math.floor((((counter+1)-math.log(abs((math.log(abs(c.real + c.imag))/power[0]))/(math.log(power[0])))/(math.log(power[0])))*1)%50)]
						
def MainRenderer(brot, ship, julia, buddha, length, height, power, pixelspacing, currentrealpos, currentimagpos, leftside, buddhay, buddhax, imgx, imgy, x, counter, draw, realminusfourth, secondbulb, grayscale):
	global color
	for a in range(0, round(height[0])):
		for a in range(0, round(length[0])): #loops for entire image size
			if power[0] == 2 and brot and julia == False:
				realminusfourth = math.sqrt((pow((currentrealpos - 1/4),2))+pow(currentimagpos,2)) #cardioid check
				secondbulb = pow((currentrealpos+1),2)+pow(currentimagpos,2)
			if ship == False and power[0] == 2 and ((currentrealpos < realminusfourth - (2*pow(realminusfourth,2)) + .25) or secondbulb < 1/16) and julia == False and brot == True and vlambda == False and PerpBrot == False:
				color = "black" #Sets color to black if cardioid check returns true
				if grayscale or invedge:
					color = "white"
				draw.point((imgx, imgy), color)
			else:
				IterativeFunction(brot, ship, tri, julia, buddha, real, imag, iters, length, height, power, pixelspacing, currentrealpos, currentimagpos, 
				buddhaposx, buddhaposy, buddhacount, buddhay, buddhax, imgx, imgy, xpostable, ypostable, x)
				Coloring(decolorize, edge, buddha, iters, length, height, arraytransfercount, xpostable, ypostable, incamount, c)
				global colortransfer
				if buddha == False: #Colors the image in absence of buddhabrot variable
					draw.point((imgx, imgy), color)
					if mirror == True:
						draw.point((imgx, height[0]-imgy), color)
						if imgy==((math.ceil(height[0]))/2+1):return
			imgx = imgx + 1
			currentrealpos, buddhax = currentrealpos + pixelspacing, buddhax + 1 #sets variables for next pixel on x axis
			result, real2, y, x, counter, modulus, color = 0, 0, 0, 0, 0, 0, 0
		imgx, imgy, currentrealpos, currentimagpos, buddhay, buddhax = 0, imgy + 1, leftside, currentimagpos + pixelspacing, buddhay + 1, 0 #Sets variables for new row
		if buddha == False: #Colors the image in absence of buddhabrot variable
			printbuffery = ' '
			printbuffery = printbuffery*(len(str(height)) - len(str(imgy)))
			print('y :',imgy,printbuffery,end='\r')
		else: #Colors image differently when buddhabrot is present
			printbuffery = ' '
			printbuffery = printbuffery*(len(str(height)) - len(str(buddhay)))
			print('y :',buddhay,printbuffery,end='\r')

################################################################
################### END FUNCTION DEFINITIONS ###################
################################################################

import argparse
import math
import time
from PIL import ImageDraw
from PIL import Image as image
import PIL #Imports modules
parser = argparse.ArgumentParser(description='A short program that creates fractal imagery.')
parser.add_argument('real', metavar='real', type=float, nargs=1 ,help='Real portion of the image center.')
parser.add_argument('imag', metavar='imag', type=float, nargs=1 ,help='Imaginary portion of the image center.')
parser.add_argument('iters', metavar='iters', type=float, nargs=1 ,help='Number of times to iterate function.')
parser.add_argument('zoom', metavar='zoom', type=float, nargs=1 ,help='Image depth.')
parser.add_argument('length', metavar='length', type=float, nargs=1 ,help='Image length.')
parser.add_argument('height', metavar='height', type=float, nargs=1 ,help='Image height.')
parser.add_argument('pow', metavar='pow', type=float, nargs=1 ,help='Number to raise z by.')
parser.add_argument('filename', type=str ,help='Name of file, excluding ".png"')
parser.add_argument('--brot' ,help='Renders the Mandelbrot set.', action='store_true')
parser.add_argument('--ship' ,help='Renders the Burning ship.', action='store_true')
parser.add_argument('--tri' ,help='Renders the Tricorn.', action='store_true')
parser.add_argument('--vlambda' ,help='Renders a mix between a julia and mandelbrot set.', action='store_true')
parser.add_argument('--perpbrot' ,help='Renders the Perpendicular Mandelbrot.', action='store_true')
parser.add_argument('--julia' ,help='Renders a julia with the given real, imag, and fractal type.', action='store_true')
parser.add_argument('--decolorize' ,help='Sets exterior color to white.', action='store_true')
parser.add_argument('--edge', help='Enables edge detection.', action='store_true')
parser.add_argument('--invedge', help='Black on white edge detection, oppsite of white on black.', action='store_true')
parser.add_argument('--grayscale', help='Replaces colors with a dynamic grayscale.', action='store_true')
parser.add_argument('--invgrayscale', help='Inverse of a black to white grayscale, white to black.', action='store_true')
parser.add_argument('--smooth', help='--EXPERIMENTAL-- Uses normalized iteration count coloring.', action='store_true')
parser.add_argument('--mirror', help='Horizontal mirroring, useful on symmetrical Fractals.', action='store_true')
parser.add_argument('--buddha', help='Renders using the buddhabrot method.', action='store_true')
parser.add_argument('--nebula', help='Renders a color variant of the buddhabrot.', action='store_true')
args = parser.parse_args() #Initializes cmd interface and defines arguments
global colorarray
real, imag, iters, zoom, length, height, power, timestart, filename = args.real, args.imag, args.iters, args.zoom, args.length, args.height, args.pow, time.process_time(), args.filename + '.png'
brot, ship, tri, julia, decolorize, edge, buddha, nebula, grayscale, invgrayscale, invedge, vlambda, PerpBrot, smooth, mirror = args.brot, args.ship, args.tri, args.julia, args.decolorize, args.edge, args.buddha, args.nebula, args.grayscale, args.invgrayscale, args.invedge, args.vlambda, args.perpbrot, args.smooth, args.mirror
refrence, dividedtwo, explevel, pixelspacing, currentrealpos, currentimagpos, leftside, counter2 = 2, 2, 2, 0, 0, 0, 0, 0 #sets variables
while zoom[0] >= explevel and zoom[0] >= 2:
	(explevel) = (explevel) * 2
	(refrence) = (refrence) / 2
while zoom[0] <= explevel:
	(explevel) = (explevel) / 2
	(refrence) = (refrence) * 2
pixelspacing = ((real[0] + refrence) - real[0]) / (length[0] / 2) #Sets difference in pixel values
if args.julia == False: #prepares for image drawing
	currentimagpos = imag[0] - (pixelspacing * (height[0] / 2)) 
	currentrealpos = real[0] - (pixelspacing * (length[0] / 2))
	boxupperleftreal = real[0] - (pixelspacing * (length[0] / 2))
	boxupperleftimag = imag[0] - (pixelspacing * (height[0] / 2))
if args.julia: #sets image location to 0 if the julia arg is present
	currentimagpos = 0 - (pixelspacing * (height[0] / 2))
	currentrealpos = 0 - (pixelspacing * (length[0] / 2))
leftside, buddhaposx, buddhaposy, buddhacount = currentrealpos, 0 - (pixelspacing * (length[0] / 2)), 0 - (pixelspacing * (height[0] / 2)), 0
imagelength, imageheight, im, buddhay, buddhax, arraytransfercount, repeatcount = length[0], height[0], image.open, 0, 0, 0, 0 #Sets variables
im = image.new('RGB', (round(imagelength), round(imageheight)), color = "black") #creates image
imgx, imgy, px, xpostable, ypostable = 0, 0, im.load(), [0] * round(iters[0]), [0] * round(iters[0])
x, counter, color, draw, mathvar, realminusfourth, counterval, pxspaceinc, incamount, colorarray = 0, 0, 0, ImageDraw.Draw(im), 0, 0, -1, 0, 255 / iters[0], [0] * round((length[0] * height[0]))
secondbulb, timeend, printbufferx, printbuffery, result = 0, 0, " ", " ", 0 #sets more variables

if nebula == False: #Giant mess that calls the main renderer function
	MainRenderer(brot, ship, julia, buddha, length, height, power, pixelspacing, currentrealpos, currentimagpos, 
	leftside, buddhay, buddhax, imgx, imgy, x, counter, draw, realminusfourth, secondbulb, grayscale)

if buddha and nebula == False: #Reconstructs image data from arrays used within image
	print('Reconstructing image data from array')
	imgx, imgy, arraycounter = 0, 0, 0
	for a in range(0, round(height[0])):
		for a in range(0, round(length[0])):
			draw.point((imgx, imgy), (round(colorarray[arraycounter]), round(colorarray[arraycounter]), round(colorarray[arraycounter])))
			arraycounter, imgx = arraycounter + 1, imgx + 1
		imgx, imgy = 0, imgy + 1
if nebula: #Runs the above code three times with minor changes so that color images can be created
	args.buddha, incamount = True, 255 / iters[0]
	MainRenderer(args.brot, args.ship, args.julia, args.buddha, length, height, power, pixelspacing, currentrealpos, currentimagpos, 
	leftside, buddhay, buddhax, imgx, imgy, x, counter, draw, realminusfourth, secondbulb, grayscale)
	imgx, imgy, arraycounter = 0, 0, 0
	for a in range(0, round(height[0])):
		for a in range(0, round(length[0])):
			r, g, b = im.getpixel((imgx, imgy))
			draw.point((imgx, imgy), (round(colorarray[arraycounter]), g, b))
			arraycounter, imgx = arraycounter + 1, imgx + 1
		imgx, imgy = 0, imgy + 1
	iters[0] = math.floor(iters[0]/10)
	print("Finished red color channel, 1/3                                    ")
	colorarray.clear()
	colorarray, incamount = [0] * round((length[0] * height[0])), 255 / iters[0]
	MainRenderer(args.brot, args.ship, args.julia, args.buddha, length, height, power, pixelspacing, currentrealpos, currentimagpos, 
	leftside, buddhay, buddhax, imgx, imgy, x, counter, draw, realminusfourth, secondbulb, grayscale)
	imgx, imgy, arraycounter = 0, 0, 0
	for a in range(0, round(height[0])):
		for a in range(0, round(length[0])):
			r, g, b = im.getpixel((imgx, imgy))
			draw.point((imgx, imgy), (r, round(colorarray[arraycounter]), b))
			arraycounter, imgx = arraycounter + 1, imgx + 1
		imgx, imgy = 0, imgy + 1
	iters[0] = math.floor(iters[0]/10)
	print("Finished green color channel, 2/3                                  ")
	colorarray.clear()
	colorarray, incamount = [0] * round((length[0] * height[0])), 255 / iters[0]
	MainRenderer(args.brot, args.ship, args.julia, args.buddha, length, height, power, pixelspacing, currentrealpos, currentimagpos, 
	leftside, buddhay, buddhax, imgx, imgy, x, counter, draw, realminusfourth, secondbulb, grayscale)
	imgx, imgy, arraycounter = 0, 0, 0
	for a in range(0, round(height[0])):
		for a in range(0, round(length[0])):
			r, g, b = im.getpixel((imgx, imgy))
			draw.point((imgx, imgy), (r, g, round(colorarray[arraycounter])))
			arraycounter, imgx = arraycounter + 1, imgx + 1
		imgx, imgy = 0, imgy + 1
	print("Finished blue color channel, 3/3                                   ")
im.save(filename) #Saves image
print('Render complete.                                                                  ')
print('time elapsed :', time.process_time() - timestart, 'seconds') #Prints time taken
