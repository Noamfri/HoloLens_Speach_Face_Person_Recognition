import json, requests
# this script, creates face_Set and the id=my_faces
# returns the face_set token
url = 'https://api-us.faceplusplus.com/facepp/v3/faceset/create'

params = dict(
      api_key='W1hXIcFVeBKI6SisUlXEeT-sDKyBqM1n',
      api_secret='GBp6p7C3-VIHQaJ3Akd2ccGCHnGIRpfg',
	  display_name='SecurityGuardFaces',
      outer_id= 'faces'
    )

resp = requests.post(url=url, params=params);
data = json.loads(resp.text);
faceset_token = data['faceset_token'];
print(faceset_token);#e98767b2c03a5faacd593b5936dc02fe