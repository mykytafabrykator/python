#!/usr/bin/env python3
import geocoder  # pipenv install geocoder
import json
from config import API
from urllib.request import urlopen


def getLocation(geo: str) -> list:
    '''Gets longitude and latitude with help of an API from input string'''

    g = geocoder.bing(geo, key=API)
    results = g.json
    try:
        res = [results['lat'], results['lng']]
        return res
    except:
        print(f'[-] An error happenned, while searching for geo location: {geo}')
        error = '404'
        return error


def getJSON(lst: list) -> dict:
    '''From given list with latitude and longitude
    gets a temperature with a help of an API of open-meteo'''

    with urlopen(f'http://api.open-meteo.com/v1/forecast?latitude={lst[0]}&longitude={lst[1]}&hourly=temperature_2m') as response:
        source = response.read()

    data = json.loads(source)
    temperature = data['hourly']['temperature_2m']
    timeLine = data['hourly']['time']

    dic = dict(zip(timeLine, temperature))
    return dic


def getResult(dic: dict) -> list:
    '''Gets the result in form of 24 hrs from dictionary'''
    counter = 0
    res = []
    for key, value in dic.items():
        res.append([key, value])
        counter += 1
        if counter == 25:
            break

    return res


def main(city):
    '''Main function'''
    loc = getLocation(city)
    if loc == '404':
        return '[-] An error happenned'
    answerJSON = getJSON(loc)
    result = getResult(answerJSON)
    result = result[::6]
    return result


if __name__ == '__main__':
    main(input())
