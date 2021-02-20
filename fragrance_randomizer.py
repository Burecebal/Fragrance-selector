from random import choice
import json


def winter_day():
    fin_list = []
    with open('fragrances.json', 'r') as file:
        data = json.load(file)
        for i in data:
            nb = int(i['total_votes'])
            if nb < 251:
                temp_list = [i['name']] * int(0.25 * (i['winter'] + i['day']))
                fin_list.extend(temp_list)
            if 250 < nb < 501:
                temp_list = [i['name']] * int(0.33 * (i['winter'] + i['day']))
                fin_list.extend(temp_list)
            if 500 < nb < 751:
                temp_list = [i['name']] * int(0.50 * (i['winter'] + i['day']))
                fin_list.extend(temp_list)
            if 750 < nb < 1001:
                temp_list = [i['name']] * int(0.75 * (i['winter'] + i['day']))
                fin_list.extend(temp_list)
            elif 1000 < nb:
                temp_list = [i['name']] * int(i['winter'] + i['day'])
                fin_list.extend(temp_list)
    return choice(fin_list)


def winter_night():
    fin_list = []
    with open('fragrances.json', 'r') as file:
        data = json.load(file)
        for i in data:
            nb = int(i['total_votes'])
            if nb < 251:
                temp_list = [i['name']] * int(0.25 * (i['winter'] + i['night']))
                fin_list.extend(temp_list)
            if 250 < nb < 501:
                temp_list = [i['name']] * int(0.33 * (i['winter'] + i['night']))
                fin_list.extend(temp_list)
            if 500 < nb < 751:
                temp_list = [i['name']] * int(0.50 * (i['winter'] + i['night']))
                fin_list.extend(temp_list)
            if 750 < nb < 1001:
                temp_list = [i['name']] * int(0.75 * (i['winter'] + i['night']))
                fin_list.extend(temp_list)
            elif 1000 < nb:
                temp_list = [i['name']] * int(i['winter'] + i['day'])
                fin_list.extend(temp_list)
    return choice(fin_list)


def spring_day():
    fin_list = []
    with open('fragrances.json', 'r') as file:
        data = json.load(file)
        for i in data:
            nb = int(i['total_votes'])
            if nb < 251:
                temp_list = [i['name']] * int(0.25 * (i['spring'] + i['day']))
                fin_list.extend(temp_list)
            if 250 < nb < 501:
                temp_list = [i['name']] * int(0.33 * (i['spring'] + i['day']))
                fin_list.extend(temp_list)
            if 500 < nb < 751:
                temp_list = [i['name']] * int(0.50 * (i['spring'] + i['day']))
                fin_list.extend(temp_list)
            if 750 < nb < 1001:
                temp_list = [i['name']] * int(0.75 * (i['spring'] + i['day']))
                fin_list.extend(temp_list)
            elif 1000 < nb:
                temp_list = [i['name']] * int(i['winter'] + i['day'])
                fin_list.extend(temp_list)
    return choice(fin_list)


def spring_night():
    fin_list = []
    with open('fragrances.json', 'r') as file:
        data = json.load(file)
        for i in data:
            nb = int(i['total_votes'])
            if nb < 251:
                temp_list = [i['name']] * int(0.25 * (i['spring'] + i['night']))
                fin_list.extend(temp_list)
            if 250 < nb < 501:
                temp_list = [i['name']] * int(0.33 * (i['spring'] + i['night']))
                fin_list.extend(temp_list)
            if 500 < nb < 751:
                temp_list = [i['name']] * int(0.50 * (i['spring'] + i['night']))
                fin_list.extend(temp_list)
            if 750 < nb < 1001:
                temp_list = [i['name']] * int(0.75 * (i['spring'] + i['night']))
                fin_list.extend(temp_list)
            elif 1000 < nb:
                temp_list = [i['name']] * int(i['winter'] + i['day'])
                fin_list.extend(temp_list)
    return choice(fin_list)


def summer_day():
    fin_list = []
    with open('fragrances.json', 'r') as file:
        data = json.load(file)
        for i in data:
            nb = int(i['total_votes'])
            if int(i['total_votes']) < 251:
                temp_list = [i['name']] * int(0.25 * (i['summer'] + i['day']))
                fin_list.extend(temp_list)
            if 250 < nb < 501:
                temp_list = [i['name']] * int(0.33 * (i['summer'] + i['day']))
                fin_list.extend(temp_list)
            if 500 < nb < 751:
                temp_list = [i['name']] * int(0.50 * (i['summer'] + i['day']))
                fin_list.extend(temp_list)
            if 750 < nb < 1001:
                temp_list = [i['name']] * int(0.75 * (i['summer'] + i['day']))
                fin_list.extend(temp_list)
            elif 1000 < nb:
                temp_list = [i['name']] * int(i['winter'] + i['day'])
                fin_list.extend(temp_list)
    return choice(fin_list)


def summer_night():
    fin_list = []
    with open('fragrances.json', 'r') as file:
        data = json.load(file)
        for i in data:
            nb = int(i['total_votes'])
            if nb < 251:
                temp_list = [i['name']] * int(0.25 * (i['summer'] + i['night']))
                fin_list.extend(temp_list)
            if 250 < nb < 501:
                temp_list = [i['name']] * int(0.33 * (i['summer'] + i['night']))
                fin_list.extend(temp_list)
            if 500 < nb < 751:
                temp_list = [i['name']] * int(0.50 * (i['summer'] + i['night']))
                fin_list.extend(temp_list)
            if 750 < nb < 1001:
                temp_list = [i['name']] * int(0.75 * (i['summer'] + i['night']))
                fin_list.extend(temp_list)
            elif 1000 < nb:
                temp_list = [i['name']] * int(i['winter'] + i['day'])
                fin_list.extend(temp_list)
    return choice(fin_list)


def fall_day():
    fin_list = []
    with open('fragrances.json', 'r') as file:
        data = json.load(file)
        for i in data:
            nb = int(i['total_votes'])
            if nb < 251:
                temp_list = [i['name']] * int(0.25 * (i['fall'] + i['day']))
                fin_list.extend(temp_list)
            if 250 < nb < 501:
                temp_list = [i['name']] * int(0.33 * (i['fall'] + i['day']))
                fin_list.extend(temp_list)
            if 500 < nb < 751:
                temp_list = [i['name']] * int(0.50 * (i['fall'] + i['day']))
                fin_list.extend(temp_list)
            if 750 < nb < 1001:
                temp_list = [i['name']] * int(0.75 * (i['fall'] + i['day']))
                fin_list.extend(temp_list)
            elif 1000 < nb:
                temp_list = [i['name']] * int(i['winter'] + i['day'])
                fin_list.extend(temp_list)
    return choice(fin_list)


def fall_night():
    fin_list = []
    with open('fragrances.json', 'r') as file:
        data = json.load(file)
        for i in data:
            nb = int(i['total_votes'])
            if nb < 251:
                temp_list = [i['name']] * int(0.25 * (i['fall'] + i['night']))
                fin_list.extend(temp_list)
            if 250 < nb < 501:
                temp_list = [i['name']] * int(0.33 * (i['fall'] + i['night']))
                fin_list.extend(temp_list)
            if 500 < nb < 751:
                temp_list = [i['name']] * int(0.50 * (i['fall'] + i['night']))
                fin_list.extend(temp_list)
            if 750 < nb < 1001:
                temp_list = [i['name']] * int(0.75 * (i['fall'] + i['night']))
                fin_list.extend(temp_list)
            elif 1000 < nb:
                temp_list = [i['name']] * int(i['winter'] + i['day'])
                fin_list.extend(temp_list)
    return choice(fin_list)
