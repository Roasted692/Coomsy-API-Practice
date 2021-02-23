import requests

#auth endpoint http://127.0.0.1:5000/auth
def basic_auth(username, password):
    response = requests.post('http://127.0.0.1:5000/auth',
                            auth = (username, password))
    if response.status_code == 200:
        return response.headers['Token']
    else:
        return print("You're retarded")

#token = You'reInItToWinIt, from basic_auth(blah,blah)

#gets list of alcohol available
def get_alcohol(token):
    response = requests.get('http://127.0.0.1:5000/alcohol',
                            headers = {'Accept': 'application/json',
                                       'Token': token},
                            )
    return response.json()

def by_price(e):
    return e

#perform first activity
def first_activity():
    #grab list of alcohol and sort based on price from greatest to least
    alcohol_number_prices = get_alcohol(basic_auth("wayne", "Youre10PlyBud!"))
    alcohol_name_prices = []
    alcohol_prices = []
    most_expensive_alcohol = []
    index = 0
    for key in alcohol_number_prices:
        alcohol_name_prices.append(alcohol_number_prices[key])
        while index < len(alcohol_name_prices):
            for other_key in alcohol_name_prices[index]:
                alcohol_prices.append(alcohol_name_prices[index][other_key])
            index += 1
    alcohol_prices.sort(reverse=True)
    most_expensive_price = alcohol_prices[0]
    for x in alcohol_number_prices.values():
        if most_expensive_price in x.values():
            most_expensive_alcohol = list(x.keys())

    print(most_expensive_alcohol[0])
    # send fucking stupid answer
    data = {'answer': f"{most_expensive_alcohol[0]}"}
    response = requests.post('http://127.0.0.1:5000/alcohol/activity/1',
                             headers = {'Accept': 'application/json',
                                        'Token': basic_auth("wayne", "Youre10PlyBud!")},
                             json = data,
                            )

    return response.text


print(first_activity())









