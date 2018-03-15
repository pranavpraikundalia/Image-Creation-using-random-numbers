
#https://www.random.org/integers/?num=10&min=1&max=6&col=1&base=10&format=plain&rnd=new
import requests
import numpy as np
import re, time
from PIL import Image
# api-endpoint
URL = "https://www.random.org/integers/?"

size=128
num=size*size
col=1
base=10
formati='plain'
rnd='new'
mini=0
#This is the max value of RGB in integer.
maxi=16777215


# defining a params dict for the parameters to be sent to the API
PARAMS = {'num': num,'min':mini,'max':maxi, 'col':col, 'base':base, 'format': formati, 'rnd': rnd}

numbers=[]

# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)

#Decoding the content from bits to string
d = r.content.decode('ASCII')
d=list(map(int,d.split()))
for i in range(size):
    numbers.append(d[(i*size):(i*size)+size])



#Creating the image from a numpy array using PIL library
im = Image.fromarray(np.asarray(numbers),'RGB')
im=im.resize((size,size), Image.ANTIALIAS)
im.show()
