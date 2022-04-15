scene = makePicture('C:\\Users\\Omar Syed\\Downloads\\tinyscene.jpg')
waldo = makePicture('C:\\Users\\Omar Syed\\Downloads\\tinywaldo.jpg')
bigscene = makePicture('C:\\Users\\Omar Syed\\Downloads\\scene.jpg')

def comparePicture(scene, waldo, startX, startY):
  sh = getHeight(scene)
  sw = getWidth(scene)
  wh = getHeight(waldo)
  ww = getWidth(waldo)
  
  counter = 0
  for x in range(ww):
    for y in range(wh):
      pixel1 = getPixel(scene, startX + x, startY + y)
      pixel2 = getPixel(waldo, x, y)
      r1 = getRed(pixel1)
      r2 = getRed(pixel2)
      diff = abs(r1 - r2)
      counter = counter + diff
  
  if counter<75000:
    addRect(scene, startX-1, startY-1, ww, wh, red)
    show(scene)
    

        
def fasterSearch(scene, waldo):
  greyscale(waldo)
  greyscale(scene)
  sh = getHeight(scene)
  sw = getWidth(scene)
  wh = getHeight(waldo)
  ww = getWidth(waldo)
  pile = []
  pixel1 = getPixel(waldo, 1, 1)
  r1 = getRed(pixel1)
  for x1 in range(sw-ww):
    for y1 in range(sh-wh):
      pixel2 = getPixel(scene, x1, y1)
      r2 = getRed(pixel2)
      if abs(r1-r2)<3:
        comparePicture(scene, waldo, x1, y1)
        
def greyscale(picture):
  for pixel in getPixels(picture):
    L = (getRed(pixel) + getGreen(pixel) + getBlue(pixel)) / 3 
    setColor(pixel, makeColor(L, L, L))
        





