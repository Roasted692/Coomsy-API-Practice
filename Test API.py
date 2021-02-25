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


    # send fucking stupid answer
    data = {'answer': f"{most_expensive_alcohol[0]}"}
    response = requests.post('http://127.0.0.1:5000/alcohol/activity/1',
                             headers = {'Accept': 'application/json',
                                        'Token': basic_auth("wayne", "Youre10PlyBud!")},
                             json = data,
                            )

    return response.text


print(first_activity())



def second_activity():
    # grab list of alcohol and sort based on price from greatest to least
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
    alcohol_prices.sort()
    most_expensive_price = alcohol_prices[0]
    for x in alcohol_number_prices.values():
        if most_expensive_price in x.values():
            most_expensive_alcohol = list(x.keys())


    # send fucking stupid answer
    data = {'answer': f"{most_expensive_alcohol[0]}"}
    response = requests.post('http://127.0.0.1:5000/alcohol/activity/2',
                             headers={'Accept': 'application/json',
                                      'Token': basic_auth("wayne", "Youre10PlyBud!")},
                             json=data,
                             )

    return response.text

print(second_activity())

def third_activity():
    alcohol_number_prices = get_alcohol(basic_auth("wayne", "Youre10PlyBud!"))
    alcohol_name_prices = []
    alcohol_prices = []
    top_10_most_expensive_alcohols = []
    index = 0
    for key in alcohol_number_prices:
        alcohol_name_prices.append(alcohol_number_prices[key])
        while index < len(alcohol_name_prices):
            for other_key in alcohol_name_prices[index]:
                alcohol_prices.append(alcohol_name_prices[index][other_key])
            index += 1
    alcohol_prices.sort(reverse=True)
    sort_index = int(.10 * len(alcohol_prices))
    top_10percent_most_expensive_prices = alcohol_prices[:sort_index]
    for x in alcohol_number_prices.values():
        for y in top_10percent_most_expensive_prices:
            if y in x.values():
                top_10_most_expensive_alcohols.append(x)

    data = {'answer': top_10_most_expensive_alcohols}
    response = requests.post('http://127.0.0.1:5000/alcohol/activity/3',
                             headers={'Accept': 'application/json',
                                      'Token': basic_auth("wayne", "Youre10PlyBud!")},
                             json=data,
                             )


    return response.text



def fourth_activity():
    alcohol_number_prices = get_alcohol(basic_auth("wayne", "Youre10PlyBud!"))



print(third_activity())


