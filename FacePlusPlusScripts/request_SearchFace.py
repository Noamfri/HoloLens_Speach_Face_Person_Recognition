import json, requests
# this script, search for image in the  faceset by outer_id
#

image = 'http://i67.tinypic.com/2jfinw5.png' # ronaldo
url = 'https://api-us.faceplusplus.com/facepp/v3/search'

params = dict(
      api_key='LHK_bvFQXz-RwuhD7alTCeXfBftIrlXg',
      api_secret='fIT0J-oCu31yAUDCVayuqGHumVzvGdco',
      image_url = image,
      outer_id= 'my_faces'
    )

resp = requests.post(url=url, params=params);
data = json.loads(resp.text);
print(data['time_used'])
print(data['results'])
