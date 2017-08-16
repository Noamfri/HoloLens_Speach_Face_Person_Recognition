import json, requests
import base64
import time
import os
from PIL import Image

with open("firas1.png", "rb") as imageFile:
    strr = base64.b64encode(imageFile.read())
    img = str(strr)
    img = img[2:len(img)-1]
    print((img))



# this script, take images URL from faces_url.txt
# and returns array of face_tokens
url = 'https://api-us.faceplusplus.com/facepp/v3/detect'
tokens = [];

with open('faces_url') as f:
    images = f.readlines()

images.clear()
images.append('2')
print(len(images))
for image in images:
    params = dict(
      api_key='LHK_bvFQXz-RwuhD7alTCeXfBftIrlXg',
      api_secret='fIT0J-oCu31yAUDCVayuqGHumVzvGdco',
      #image_base64=encoded_string
      # return_attributes='gender,age',
        #image_url =  'sdfsdfsdf'
        #image_file = open("firas1.png", "rb"),
        image_base64 = img
    )

    resp = requests.post(url=url, params=params)

    data = json.loads(resp.text)
    print(data)
    # face_token_first_index = str((data['faces'][0])).find("face_token")+14;
    # face_token_last_index  = str((data['faces'][0])).find("'",face_token_first_index);
    # face_token = str(data['faces'][0])[face_token_first_index:face_token_last_index];# face token
    # tokens.append(face_token);

print(tokens)