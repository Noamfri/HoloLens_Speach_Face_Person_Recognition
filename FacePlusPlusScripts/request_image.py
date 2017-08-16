import json, requests
import base64

with open("Images/firas_pic.png", "rb") as imageFile:
    strr = base64.b64encode(imageFile.read())
    rd = str(imageFile)
    img = str(strr)
    img = img[2:len(img)-1]

with open("Images/firas_pic.png", "rb") as imageFile:
    strr = base64.b64encode(imageFile.read())
    rd = str(imageFile)
    img = str(strr)
    img = img[2:len(img)-1]
#with open("firas1.png", "rb") as image_file:
# encoded_string = base64.b64encode(image_file.read());


url = 'https://api-us.faceplusplus.com/facepp/v3/faceset/create'

params = dict(
    api_key='LHK_bvFQXz-RwuhD7alTCeXfBftIrlXg',
    api_secret='fIT0J-oCu31yAUDCVayuqGHumVzvGdco',
    #image_base64_1= str(encoded_string),
    #image_base64_2= str(encoded_string2),
#image_base64_2= base64.urlsafe_b64encode(str('C:\Users\Public\firas2.png')),
    image_url='http://i66.tinypic.com/wkr5lt.png',
    image_url2='http://i66.tinypic.com/11j2a2g.png'
)

resp = requests.post(url=url, params=params)
data = json.loads(resp.text)



url = 'https://api-us.faceplusplus.com/facepp/v3/search'

params = dict(
    api_key='LHK_bvFQXz-RwuhD7alTCeXfBftIrlXg',
    api_secret='fIT0J-oCu31yAUDCVayuqGHumVzvGdco',
    #image_base64_1= str(encoded_string),
    #image_base64_2= str(encoded_string2),
#image_base64_2= base64.urlsafe_b64encode(str('C:\Users\Public\firas2.png')),
    image_url='http://i66.tinypic.com/wkr5lt.png',
    image_url2='http://i66.tinypic.com/11j2a2g.png'
)

resp = requests.post(url=url, params=params)
data = json.loads(resp.text)

print("time = "+str(data['time_used'])+" milliseconds");
#print("confidence= "+str(data['confidence'])+"%");
