beach = makePicture('C:\\Users\\Omar Syed\\Desktop\\Computer Science\\Sem 1\\CPS 109\\Program FIles\\MediaSources\\mediasources-4ed\\beach.jpg')
butterfly = makePicture('C:\\Users\\Omar Syed\\Desktop\\Computer Science\\Sem 1\\CPS 109\\Program FIles\\MediaSources\\mediasources-4ed\\butterfly.jpg')
bug = makePicture('C:\\Users\\Omar Syed\\Desktop\\Computer Science\\Sem 1\\CPS 109\\Program FIles\\MediaSources\\mediasources-4ed\\caterpillar.jpg')
#1
def border(picture):
  w = getWidth(picture)
  h = getHeight(picture)   
  for pixel in getPixels(picture):
    x = getX(pixel)
    y = getY(pixel)
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)
    if x < 5 or x > w-5 :
      r = 244
      g = 164
      b = 96
      setColor(pixel, makeColor(r, g, b))
    if y < 5 or y > h-5:
      r = 244
      g = 164
      b = 96
      setColor(pixel, makeColor(r, g, b))
    if x < 10 and x > 4 or x > w -10 and x < w - 4:
      r = 0
      g = 0
      b = 0
      setColor(pixel, makeColor(r, g, b))
    if y < 10 and y > 4 or y > h -10 and y < h - 4:
      r = 0
      g = 0
      b = 0     
      setColor(pixel, makeColor(r, g, b)) 
  show(picture)
#2
def whitescreen(backgroundpic, picture):
  for pixel in getPixels(picture):
    x = getX(pixel)
    y = getY(pixel)
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)
    if r > 200 and g > 200 and b > 200:
      br = getRed(getPixel(backgroundpic, x+50, y+50))
      bg = getGreen(getPixel(backgroundpic, x+50, y+50))
      bb = getBlue(getPixel(backgroundpic, x+50, y+50))
      setColor(pixel,makeColor(br, bg, bb))
  show(picture)
#3
def transparent(backgroundpic, picture):
  for pixel in getPixels(picture):
    x = getX(pixel)
    y = getY(pixel)
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)
    if r > 200 and g > 200 and b > 200:
      r = 0
      g = 0
      b = 0
    br = getRed(getPixel(backgroundpic, x+200, y+150)) + r
    bg = getGreen(getPixel(backgroundpic, x+200, y+150)) + g
    bb = getBlue(getPixel(backgroundpic, x+200, y+150)) + b
    setColor(pixel,makeColor(br, bg, bb)) 
  show(picture)
#4
def GreyBlueGrid(picture):
  w = getWidth(picture)
  h = getHeight(picture)
  for pixel in getPixels(picture):
    x = getX(pixel)
    y = getY(pixel)
    if w/4 < x < w/2 or w*.75 < x < w:
      r = getRed(pixel)
      g = getGreen(pixel)
      b = getBlue(pixel)
      lum = r * 0.3 + g * 0.6 + b * 0.1
      setColor(pixel, makeColor(lum, lum, lum))
    if h/4 < y < h/2 or h*.75 < y < h:
      r = getRed(pixel)
      g = getGreen(pixel)
      b = getBlue(pixel)
      setColor(pixel, makeColor(r - 20, g - 20, b + 50))
  show(picture)
#5  
def greenscreen(backgroundpic, picture):
  for pixel in getPixels(picture):
    x = getX(pixel)
    y = getY(pixel)
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)
    if r < 70 and g > 200 and b < 70:
      br = getRed(getPixel(backgroundpic, x+50, y+50))
      bg = getGreen(getPixel(backgroundpic, x+50, y+50))
      bb = getBlue(getPixel(backgroundpic, x+50, y+50))
      setColor(pixel,makeColor(br, bg, bb))
  show(picture)
#6 
def blackandwhite(picture):
  for pixel in getPixels(picture):
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)
    if r > 120 and g > 120 and b > 120:
      setColor(pixel, makeColor(r + 255, g + 255, b + 255))
    else:
      setColor(pixel, makeColor(r - 255, g - 255, b - 255))
  show(picture)
#7
def verticalReflection(picture):
  h = getHeight(picture)
  w = getWidth(picture)
  for y in range(h):
    for x in range(0, w/2):
      leftPixel = getPixel(picture, x, y)
      rightPixel = getPixel(picture, w - 1 - x, y)
      color = getColor(leftPixel)
      setColor(rightPixel, color)
  show(picture)
#8 
def horizontalReflection(picture): 
  h = getHeight(picture)
  w = getWidth(picture)
  for x in range(w):
    for y in range(0, h/2):
      topPixel = getPixel(picture, x, y)
      bottomPixel = getPixel(picture, x, h-y-1)
      color = getColor(topPixel)
      setColor(bottomPixel, color)
  show(picture)
  
#9
def square(picture, startx, starty, height, width, color):
  for pixel in getPixels(picture):
    x = getX(pixel)
    y = getY(pixel)
    if startx < x < startx+width and starty < y < starty+height:
      setColor(pixel, color)
  
def combinedSquare(picture):
  square(picture, 100, 100, 100, 100, blue)
  square(picture, 120, 120, 60, 60, red)
  square(picture, 140, 140, 20, 20, green)
  show(picture)
#10
def circle(picture, xc, yc, radius, color) :
  pixels = getPixels(picture)
  for pixel in pixels :
    x = getX(pixel)
    y = getY(pixel)
    distance = math.sqrt((x - xc)**2 + (y - yc)**2)
    if distance < radius :
      setColor(pixel, color)
  show(picture)
# circle(beach, 100, 100, 100, red)
#11  
def line(picture, x1, y1, x2, y2, thickness, color) :
  pixels = getPixels(picture)
  m = 1.0 * (y2 - y1) / (x2 - x1)
  b = y1 - m * x1
  for pixel in pixels :
    x = getX(pixel)
    y = getY(pixel)
    y_line = m * x + b
    distance = int(abs(y_line - y) + 0.5)
    if distance < thickness / 2 :
      setColor(pixel, color)
  show(picture)
# line(beach, 100, 100, 300, 300, 5, red)
#12
def segment(picture, x1, y1, x2, y2, startx, endx, starty, endy, thickness, color) :
  pixels = getPixels(picture)
  m = 1.0 * (y2 - y1) / (x2 - x1)
  b = y1 - m * x1
  for pixel in pixels :
    x = getX(pixel)
    y = getY(pixel)
    y_line = m * x + b
    distance = int(abs(y_line - y) + 0.5)
    if distance < thickness / 2 :
      if startx < x < endx and starty < y < endy:
        setColor(pixel, color)
      if startx > x > endx and starty > y > endy:
        setColor(pixel, color)
  show(picture)
# segment(beach, 100, 100, 300, 300, 100, 300, 100, 300, 5, blue)
#13
def redify(picture):
  for pixel in getPixels(picture):
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)
    setColor(pixel, makeColor(r*2, g-50, b-50))
  show(picture)
#14 
def grid(picture):
  for pixel in getPixels(picture):
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)
    x = getX(pixel)
    y = getY(pixel)
    if x % 8 == 0:
      setColor(pixel, makeColor(r-255, g-255, b-255))
    if y % 8 == 0:
      setColor(pixel, makeColor(r-255, g-255, b-255))
  show(picture)
#15 
def darken(picture):
  for pixel in getPixels(picture):
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)
    setColor(pixel, makeColor(r/3, g/3, b/3))
  show(picture)
#16
def lighten(picture):
  for pixel in getPixels(picture):
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)
    setColor(pixel, makeColor(r*2, g*2, b*2))
  show(picture)
#17   
def contrast(picture, factor):
  for pixel in getPixels(picture):
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)
    setColor(pixel, makeColor(r*factor, g*factor, b*factor))
  show(picture)
#18
def extremeColors(picture):
  for pixel in getPixels(picture):
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)
    if r > g and r > b:
      setColor(pixel, red)
    if g > r and g > b:
      setColor(pixel, green)
    if b > r and b > g:
      setColor(pixel, blue)
  show(picture)
#19
def flipColors(picture):
  for pixel in getPixels(picture):
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)
    if r > g and r > b:
      setColor(pixel, makeColor(r*.5,g*1.5, b*1.5))
    if g > r and g > b:
      setColor(pixel, makeColor(r*1.5, g*.5, b*1.5))
    if b > r and b > g:
      setColor(pixel, makeColor(r*1.5, g*1.5, b*.5))
  show(picture)
    
#20
def reversebandw(picture):
  for pixel in getPixels(picture):
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)
    if r < 135 and g < 135 and b < 135:
      setColor(pixel, makeColor(r + 255, g + 255, b + 255))
    else:
      setColor(pixel, makeColor(r - 255, g - 255, b - 255))
  show(picture)
    
    
    
    
    
    
    
    
    