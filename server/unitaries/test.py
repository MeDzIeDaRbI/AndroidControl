# import the necessary packages
import requests

# define the URL to our face detection API
url = "http://127.0.0.1:8000/volume/volume/"

# load our image and now use the face detection API to find faces in
# images by uploading an image directly
payload = {'volume':'up'}
r = requests.post(url, data=payload).json()
print "2.png: {}".format(r)