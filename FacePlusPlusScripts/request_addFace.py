import json, requests
# this script, add face to faceset_Token
# returns the face_set token
# '', '', '', '']

faceset_token = list();
#faceset_token.append('15647c0bc7b3eddd0a23de0ef1509657')
#faceset_token.append('4d4f8196e70b466c0dea648ca8119ff3')
#faceset_token.append('6d0b9cc7a00b3694f7eb75ba85e3ab19')
#faceset_token.append('a0bc9f4a76dd0641beaa71bb9661b63e')
faceset_token.append('942329bd3e319e31f0eefea4cf597d09')
url = 'https://api-us.faceplusplus.com/facepp/v3/faceset/addface'

params = dict(
      api_key='LHK_bvFQXz-RwuhD7alTCeXfBftIrlXg',
      api_secret='fIT0J-oCu31yAUDCVayuqGHumVzvGdco',
      outer_id= 'my_faces',
      face_tokens = ",".join(faceset_token),
    )

resp = requests.post(url=url, params=params);
data = json.loads(resp.text);



print(data);