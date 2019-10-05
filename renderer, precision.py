##################################################################
################### START FUNCTION DEFINITIONS ###################
##################################################################



def IterativeFunction(brot, ship, tri, buddha, real, imag, iters, length, height, power, pixelspacing, currentrealpos, currentimagpos, 
buddhaposx, buddhaposy, buddhacount, buddhay, buddhax, imgx, imgy, xpostable, ypostable, x):
	resultre, resultim, resultresqr, resultimsqr = mpf(0), mpf(0), mpf(0), mpf(0)
	global result
	global counter
	global repeatcount
	c = mpc(currentrealpos, currentimagpos) #complex number used
	counter = 0
	for a in range(0,round(iters)): #Loops for n amounts [iteration count]
		if brot:
			resultim = mpf(resultre) * mpf(resultim) * mpf(2.0) + mpf(c.imag)
			resultre = mpf(resultresqr) - mpf(resultimsqr) + mpf(c.real)
			resultimsqr = mpf(resultim) * mpf(resultim)
			resultresqr = mpf(resultre) * mpf(resultre) #Mandelbrot set
		if tri:
			resultim = mpf(resultre) * mpf(resultim) * mpf(-2.0) + mpf(c.imag)
			resultre = mpf(resultresqr) - mpf(resultimsqr) + mpf(c.real)
			resultimsqr = mpf(resultim) * mpf(resultim)
			resultresqr = mpf(resultre) * mpf(resultre) #tricorn formula
		if ship:
			resultim = mpf(abs(mpf(resultre) * mpf(resultim))) * mpf(2.0) + mpf(c.imag)
			resultre = mpf(resultresqr) - mpf(resultimsqr) + mpf(c.real)
			resultimsqr = mpf(resultim) * mpf(resultim)
			resultresqr = mpf(resultre) * mpf(resultre) #Burning ship formula
		if PerpBrot:
			resultim = mpf(abs(mpf(resultre))) * mpf(resultim) * mpf(-2.0) + mpf(c.imag)
			resultre = mpf(resultresqr) - mpf(resultimsqr) + mpf(c.real)
			resultimsqr = mpf(resultim) * mpf(resultim)
			resultresqr = mpf(resultre) * mpf(resultre) #Perpendicular mandelbrot set
		if HBrot:
			resultim = mpf(abs(mpf(resultre))) * mpf(resultim) * mpf(2.0) + mpf(c.imag)
			resultre = mpf(resultresqr) - mpf(resultimsqr) + mpf(c.real)
			resultimsqr = mpf(resultim) * mpf(resultim)
			resultresqr = mpf(resultre) * mpf(resultre) #Heart shaped mandelbrot set
		if PerpBS:
			resultim = mpf(resultre) * mpf(abs(mpf(resultim))) * mpf(-2.0) + mpf(c.imag)
			resultre = mpf(resultresqr) - mpf(resultimsqr) + mpf(c.real)
			resultimsqr = mpf(resultim) * mpf(resultim)
			resultresqr = mpf(resultre) * mpf(resultre) #Perpendicular Burning Ship
		if vlambda:
			resultim = mpf(resultre) * mpf(resultim) * mpf(2.0) *mpc(-c) + mpf(c.imag)
			resultre = (mpf(resultresqr) - mpf(resultimsqr)) *mpc(-c) + mpf(c.real)
			resultimsqr = mpf(resultim) * mpf(resultim)
			resultresqr = mpf(resultre) * mpf(resultre)
		#if testfract:
		(result) = mpc(resultre, resultim)
		(x) = mpc(result)
		(counter) = (counter) + 1
		(repeatcount) = (repeatcount) + 1 #Sets variables up and prepares for another iteration
		if buddha:
			while mpf(x.real) >= buddhaposx:
				buddhaposx = mpf(buddhaposx) + mpf(pixelspacing)
				buddhacount = buddhacount + 1
			xpostable[repeatcount - 1] = mpf(buddhacount)
			buddhacount = 0
			while mpf(x.imag) >= buddhaposy:
				buddhaposy = mpf(buddhaposy) + mpf(pixelspacing)
				buddhacount = buddhacount + 1
			ypostable[repeatcount - 1] = mpf(buddhacount)
			buddhacount, buddhaposx, buddhaposy = 0, mpf(0) - (mpf(pixelspacing) * (mpf(length[0]) / 2)), mpf(0) - (mpf(pixelspacing) * (mpf(height[0]) / 2)) #Prepares for buddhabrot array modification
		if mpf(abs(mpf(result.real)))*mpf(abs(mpf(result.real))) + mpf(abs(mpf(result.imag)))*mpf(abs(mpf(result.imag))) > 4:
			break # Determines escape values quicker

def Coloring(decolorize, edge, buddha, iters, length, height, arraytransfercount, xpostable, ypostable, incamount):
	global result
	global counter
	global color
	global repeatcount
	global counterval
	if buddha and counter != iters:
		for a in range(0, repeatcount):
			if mpf(xpostable[round(arraytransfercount)]) < length[0] and mpf(xpostable[round(arraytransfercount)]) > 0 and mpf(ypostable[round(arraytransfercount)]) < height[0] and mpf(ypostable[round(arraytransfercount)]) > 0:
				r = mpf(colorarray[round(mpf(xpostable[round(arraytransfercount)])) + (mpf(length[0]) * mpf(ypostable[round(arraytransfercount)]))])
				if r < 255:
					r = mpf(r) + mpf(incamount)
				else:
					r = 0
				colorarray[round(xpostable[round(arraytransfercount)] + (length[0] * ypostable[round(arraytransfercount)]))] = colorarray[round(xpostable[round(arraytransfercount)] + (length[0] * ypostable[round(arraytransfercount)]))] + r
			arraytransfercount = arraytransfercount + 1 #Adds values to buddhabrot and dynamically changes incrementation amounts across different iter values
	arraytransfercount, repeatcount = 0, 0
	if buddha == False:
		if abs(result) <= 2 and grayscale == False and invedge == False: #Colors the set black when needed
			color = "black"
		else:
			if abs(result) <=2 and (grayscale or invedge):
				color = "white"
			else:
				if decolorize:
					(color) = "white" #In case of decolorize argument, the exterior colors will be set to white
				else:
					if counterval != counter and edge: #Detects if a change in the iteration values exists, and if so, a white color will be displayed
						color = "white" 
						counterval = counter
					if counterval != counter and invedge: #Detects if a change in the iteration values exists, and if so, a black color will be displayed
						color = "black" 
						counterval = counter
					if edge == False and invedge == False: #Determines point color with table
						(modulus) = (counter) % 8 
						colorlookup = ["Black", "Red", "Orange", "Yellow", "Green", "Blue", "Violet", "Gray"]
						(color) = colorlookup[modulus]
					if edge and counterval == counter and color == 0: #Chooses black if no iter change is present
						color = "black"
						counterval = counter
					if invedge and counterval == counter and color == 0: #Chooses white if no iter change is present
						color = "white"
						counterval = counter
					if invgrayscale:
						color = (math.floor(mpf(255) - mpf(counter) * (mpf(255)/iters)), math.floor(mpf(255) - mpf(counter) * (mpf(255)/iters)), math.floor(mpf(255) - mpf(counter) * (mpf(255)/iters)))
					if grayscale:
						color = (math.floor(mpf(counter) * (mpf(255)/iters)), math.floor(mpf(counter) * (mpf(255)/iters)), math.floor(mpf(counter) * (mpf(255)/iters)))
						
def MainRenderer(brot, ship, buddha, length, height, power, pixelspacing, currentrealpos, currentimagpos, leftside, buddhay, buddhax, imgx, imgy, x, counter, draw, realminusfourth, secondbulb, grayscale):
	global color
	for a in range(0, round(height[0])):
		for a in range(0, round(length[0])): #loops for entire image size
			if power[0] == 2 and brot:
				realminusfourth = mpf(math.sqrt(mpf((pow(mpf((mpf(currentrealpos) - 1/4)),2))+pow(mpf(currentimagpos),2)))) #cardioid check
				secondbulb = mpf(pow((mpf(currentrealpos)+1),2))+mpf(pow(mpf(currentimagpos),2))
			if ship == False and power[0] == 2 and ((currentrealpos < mpf(realminusfourth) - (mpf(2*mpf(pow(mpf(realminusfourth),2)))) + .25) or secondbulb < 1/16) and brot == True and vlambda == False and PerpBrot == False and HBrot == False and PerpBS == False:
				color = "black" #Sets color to black if cardioid check returns true
				if grayscale or invedge:
					color = "white"
				draw.point((imgx, imgy), color)
			else:
				IterativeFunction(brot, ship, tri, buddha, real, imag, iters, length, height, power, pixelspacing, currentrealpos, currentimagpos, 
				buddhaposx, buddhaposy, buddhacount, buddhay, buddhax, imgx, imgy, xpostable, ypostable, x)
				Coloring(decolorize, edge, buddha, iters, length, height, arraytransfercount, xpostable, ypostable, incamount)
				global colortransfer
				if buddha == False: #Colors the image in absence of buddhabrot variable
					draw.point((imgx, imgy), color)
			imgx = imgx + 1
			currentrealpos, buddhax = mpf(currentrealpos) + mpf(pixelspacing), buddhax + 1 #sets variables for next pixel on x axis
			result, real2, y, x, counter, modulus, color = 0, 0, 0, 0, 0, 0, 0
		imgx, imgy, currentrealpos, currentimagpos, buddhay, buddhax = 0, imgy + 1, leftside, mpf(currentimagpos) + mpf(pixelspacing), buddhay + 1, 0 #Sets variables for new row
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
from mpmath import *
from PIL import ImageDraw
from PIL import Image as image
import PIL #Imports modules
parser = argparse.ArgumentParser(description='A short program that creates fractal imagery.')
parser.add_argument('real', metavar='real', type=str, nargs=1 ,help='Real portion of the image center.')
parser.add_argument('imag', metavar='imag', type=str, nargs=1 ,help='Imaginary portion of the image center.')
parser.add_argument('iters', metavar='iters', type=str, nargs=1 ,help='Number of times to iterate function.')
parser.add_argument('zoom', metavar='zoom', type=str, nargs=1 ,help='Image depth.')
parser.add_argument('length', metavar='length', type=float, nargs=1 ,help='Image length.')
parser.add_argument('height', metavar='height', type=float, nargs=1 ,help='Image height.')
parser.add_argument('pow', metavar='pow', type=float, nargs=1 ,help='Number to raise z by.')
parser.add_argument('precision', metavar='prec', type=float, nargs=1 ,help='Number of decimal places to use, 17 is 64 bit.')
parser.add_argument('filename', type=str ,help='Name of file, excluding ".png"')
parser.add_argument('--brot' ,help='Renders the Mandelbrot set.', action='store_true')
parser.add_argument('--ship' ,help='Renders the Burning ship.', action='store_true')
parser.add_argument('--tri' ,help='Renders the Tricorn.', action='store_true')
parser.add_argument('--vlambda' ,help='Renders a mix between a Julia and Mandelbrot set.', action='store_true')
parser.add_argument('--perpbrot' ,help='Renders the Perpendicular Mandelbrot.', action='store_true')
parser.add_argument('--hbrot' ,help='Renders a heart shaped Mandelbrot set.', action='store_true')
parser.add_argument('--perpbs' ,help='Renders the Perpendicular Burning Ship.', action='store_true')
parser.add_argument('--testfract' ,help='Test.', action='store_true')
parser.add_argument('--decolorize' ,help='Sets exterior color to white.', action='store_true')
parser.add_argument('--edge', help='Enables edge detection.', action='store_true')
parser.add_argument('--invedge', help='Black on white edge detection, oppsite of white on black.', action='store_true')
parser.add_argument('--grayscale', help='Replaces colors with a dynamic grayscale.', action='store_true')
parser.add_argument('--invgrayscale', help='Inverse of a black to white grayscale, white to black.', action='store_true')
parser.add_argument('--buddha', help='Renders using the Buddhabrot method.', action='store_true')
parser.add_argument('--nebula', help='Renders a color variant of the Buddhabrot.', action='store_true')
args = parser.parse_args() #Initializes cmd interface and defines arguments
mp.dps = (args.precision[0])
global colorarray
real, imag, iters, zoom, length, height, power, timestart, filename = args.real, args.imag, args.iters, args.zoom, args.length, args.height, args.pow, time.process_time(), args.filename + '.png'
real, imag, iters, zoom = mpmathify(real[0]), mpmathify(imag[0]), mpmathify(iters[0]), mpmathify(zoom[0])
brot, ship, tri, decolorize, edge, buddha, nebula = args.brot, args.ship, args.tri, args.decolorize, args.edge, args.buddha, args.nebula
grayscale, invgrayscale, invedge, vlambda, PerpBrot, HBrot, PerpBS, testfract = args.grayscale, args.invgrayscale, args.invedge, args.vlambda, args.perpbrot, args.hbrot, args.perpbs, args.testfract
refrence, dividedtwo, explevel, pixelspacing, currentrealpos, currentimagpos, leftside, counter2 = 2, 2, 2, 0, 0, 0, 0, 0 #sets variables
while zoom >= explevel and zoom >= 2:
	(explevel) = (explevel) * 2
	(refrence) = mpf(refrence) / 2
while zoom <= explevel:
	(explevel) = mpf(explevel) / 2
	(refrence) = (refrence) * 2
pixelspacing = mpf(mpf(real + refrence) - real) / (mpf(length[0]) / 2) #Sets difference in pixel values
currentimagpos = mpf(imag) - (mpf(pixelspacing) * (mpf(height[0]) / 2)) 
currentrealpos = mpf(real) - (mpf(pixelspacing) * (mpf(length[0]) / 2))
boxupperleftreal = mpf(real) - (mpf(pixelspacing) * (mpf(length[0]) / 2))
boxupperleftimag = mpf(imag) - (mpf(pixelspacing) * (mpf(height[0]) / 2))
leftside, buddhaposx, buddhaposy, buddhacount = currentrealpos, mpf(0) - (mpf(pixelspacing) * (mpf(length[0] / 2))), mpf(0) - (mpf(pixelspacing) * (mpf(height[0]) / 2)), 0
imagelength, imageheight, im, buddhay, buddhax, arraytransfercount, repeatcount = length[0], height[0], image.open, 0, 0, 0, 0 #Sets variables
im = image.new('RGB', (round(imagelength), round(imageheight)), color = "black") #creates image
imgx, imgy, px, xpostable, ypostable = 0, 0, im.load(), [0] * round(iters), [0] * round(iters)
x, counter, color, draw, mathvar, realminusfourth, counterval, pxspaceinc, incamount, colorarray = 0, 0, 0, ImageDraw.Draw(im), 0, 0, -1, 0, mpf(255) / iters, [0] * round((length[0] * height[0]))
secondbulb, timeend, printbufferx, printbuffery, result = 0, 0, " ", " ", 0 #sets more variables

if nebula == False: #Giant mess that calls the main renderer function
	MainRenderer(brot, ship, buddha, length, height, power, pixelspacing, currentrealpos, currentimagpos, 
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
	args.buddha, incamount = True, mpf(255) / iters
	MainRenderer(args.brot, args.ship, args.buddha, length, height, power, pixelspacing, currentrealpos, currentimagpos, 
	leftside, buddhay, buddhax, imgx, imgy, x, counter, draw, realminusfourth, secondbulb, grayscale)
	imgx, imgy, arraycounter = 0, 0, 0
	for a in range(0, round(height[0])):
		for a in range(0, round(length[0])):
			r, g, b = im.getpixel((imgx, imgy))
			draw.point((imgx, imgy), (round(colorarray[arraycounter]), g, b))
			arraycounter, imgx = arraycounter + 1, imgx + 1
		imgx, imgy = 0, imgy + 1
	iters = math.floor(mpf(iters)/10)
	print("Finished red color channel, 1/3                                    ")
	colorarray.clear()
	colorarray, incamount = [0] * round((length[0] * height[0])), mpf(255) / iters
	MainRenderer(args.brot, args.ship, args.buddha, length, height, power, pixelspacing, currentrealpos, currentimagpos, 
	leftside, buddhay, buddhax, imgx, imgy, x, counter, draw, realminusfourth, secondbulb, grayscale)
	imgx, imgy, arraycounter = 0, 0, 0
	for a in range(0, round(height[0])):
		for a in range(0, round(length[0])):
			r, g, b = im.getpixel((imgx, imgy))
			draw.point((imgx, imgy), (r, round(colorarray[arraycounter]), b))
			arraycounter, imgx = arraycounter + 1, imgx + 1
		imgx, imgy = 0, imgy + 1
	iters = math.floor(mpf(iters)/10)
	print("Finished green color channel, 2/3                                  ")
	colorarray.clear()
	colorarray, incamount = [0] * round((length[0] * height[0])), mpf(255) / iters
	MainRenderer(args.brot, args.ship, args.buddha, length, height, power, pixelspacing, currentrealpos, currentimagpos, 
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