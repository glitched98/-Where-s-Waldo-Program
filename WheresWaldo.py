# Omar Syed
# Student Number: 500809837

scene = makePicture('C:\\Users\\Omar Syed\\Downloads\\tinyscene.jpg')
waldo = makePicture('C:\\Users\\Omar Syed\\Downloads\\tinywaldo.jpg')

#Function 1
# Function that takes the template and searchImage and determines the luminance of the pixel in template and takes the luminance
# .. of the relative pixel on the searchImage, and then finds the difference between the luminance values
# .. template luminance - searchImage luminance 
def compareOne(template, searchImage, x1, y1): 
  w = getWidth(template) 
  h = getHeight(template)
  sum = 0 
  for x in range(w): 
    for y in range(h):
      pixel1 = getPixel(template, x, y) 
      L1 = getRed(pixel1) 
      pixel2 = getPixel(searchImage, x1 + x, y1 + y)
      L2 = getRed(pixel2) 
      difflum = abs(L1 - L2) 
      sum = sum + difflum # difference in the Red values from template and searchImage
  return sum 
 
#Function 2
def compareAll(template, searchImage): 
  w = getWidth(searchImage) 
  h = getHeight(searchImage)
  grayscale(template) # GreyScale Template
  grayscale(searchImage) # GreScale SearchImage
  matrix = [[1000000000 for i in range(w)] for j in range(h)] #Building the 2D array
  for x in range(w - (getWidth(template))): 
    for y in range(h - (getHeight(template))):
      matrix [x][y] = compareOne(template, searchImage, x, y) # Calls upon the first compareOne function to compare 
      # .. red values from these x and y values
  return matrix

#Function 3
# Function to locate the minimum values in the generated 2D matrix
def find2Dmin(matrix):
  mincol, minrow = 0, 0 
  min = 10000000 
  for j in range(len(matrix)): 
    for i in range(len(matrix[j])): 
      if matrix[j][i] < min: 
        mincol = i 
        minrow = j 
        min = matrix[j][i]
  return (minrow, mincol) 
      
#Function 4
# Builds a Rectangle around the found SearchImage in the Template
def displayMatch(searchImage, x1, y1, w1, h1, color):
  print(x1 , y1)
  addRect(searchImage, x1, y1, w1, h1, color) 
    
#Function 5
# GreyScales images to allow luminance difference to be caluclated accurately
def grayscale(picture): # Function Grey Scales the whole image
  for pixel in getPixels(picture):
    L = (getRed(pixel) + getGreen(pixel) + getBlue(pixel)) / 3 
    setColor(pixel, makeColor(L, L, L)) 
    
#Function 6
# The Parent Function to call upon all other classes required to find Location of Waldo in the Scene image and
# .. after greyscaling the image, builds a rectangle around the Waldo in the searchImage[Scene] to indicate its location
def findWaldo(targetJPG, searchJPG):
  matrix = compareAll(targetJPG, searchJPG)
  x, y = find2Dmin(matrix) 
  displayMatch(searchJPG, x, y, getWidth(targetJPG), getHeight(targetJPG), red) 
  show(scene)
  
  
