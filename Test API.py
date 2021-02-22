import requests

#auth endpoint http://127.0.0.1:5000/auth
def basic_auth(username, password):
    response = requests.post('http://127.0.0.1:5000/auth',
                            auth = (username, password))
    if response.status_code == 200:
        return response.headers['Token']
    else:
        return print("You're retarded")



print(basic_auth("wayne", "Youre10PlyBud!"))

#token = You'reInItToWinIt, from basic_auth(blah,blah)

#gets list of alcohol available
def get_alcohol(token):
    response = requests.get('http://127.0.0.1:5000/alcohol',
                            headers = {'Accept': 'application/json',
                                       'Token': token},
                            )
    return print(response.json())

get_alcohol(basic_auth("wayne", "Youre10PlyBud!"))









