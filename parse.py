import pickle
import collections
from PIL import Image, ImageDraw

im = Image.new('RGBA', (800,800), 'white')
im_draw = ImageDraw.Draw(im)



#calculate frequency of each quadrant
flairs = pickle.load(open('flairs.p', 'rb'))
flair_count = collections.Counter(flairs)


# convert the subcategories into the 4 main categories
simple_count = {}


simple_count['libright'] = flair_count[':libright2: - LibRight'] + flair_count[':libright: - LibRight'] + flair_count[':right: - Right'] / 2 + flair_count[':lib: - LibCenter'] / 2
simple_count['libleft'] = flair_count[':libleft: - LibLeft'] + flair_count[':left: - Left'] / 2 + flair_count[':lib: - LibCenter'] / 2
simple_count['authleft'] = flair_count[':authleft: - AuthLeft'] + flair_count[':left: - Left'] / 2 + flair_count[':auth: - AuthCenter'] / 2
simple_count['authright'] = flair_count[':authright: - AuthRight'] + flair_count[':auth: - AuthCenter'] / 2 + flair_count[':right: - Right'] / 2


# normalize values
max_val = 0
for key in simple_count:
    if simple_count[key] > max_val:
        max_val = simple_count[key]
        
for key in simple_count:
    simple_count[key] /= max_val
print(simple_count)

# draw correctly sized quadrants
im_draw.rectangle([(400, 400), (400 - (380 * simple_count['authleft']), 400 - (380 * simple_count['authleft']))], '#f9baba')
im_draw.rectangle([(400, 400), (400 + (380 * simple_count['authright']), 400 - (380 * simple_count['authright']))],'#92d9f8')
im_draw.rectangle([(400, 400), (400 - (380 * simple_count['libleft']), 400 + (380 * simple_count['libleft']))],'#c8e4bc')
im_draw.rectangle([(400, 400), (400 + (380 * simple_count['libright']), 400 + (380 * simple_count['libright']))],'#e1c6df')


# Draw axis lines
im_draw.rectangle([(399, 10), (401,790)], 'black')
im_draw.rectangle([(10, 399), (790, 401)], 'black')

#draw arrow for axes
im_draw.polygon([(0,400), (25, 410), (25, 390)], 'black')
im_draw.polygon([(800,400), (775, 410), (775, 390)], 'black')
im_draw.polygon([(400, 0), (410, 25), (390, 25)], 'black')
im_draw.polygon([(400, 800), (410, 775), (390,775)], 'black')

im.show()
im.save('pcmrepresentation.png')


