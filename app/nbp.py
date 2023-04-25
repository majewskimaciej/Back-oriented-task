from fastapi import HTTPException
import requests


def get_response(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
    except requests.exceptions.HTTPError as eh:
        raise HTTPException(status_code=404, detail=eh.response.text)
    except requests.exceptions.Timeout as et:
        raise HTTPException(status_code=408, detail=et.response.text)
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=400, detail=e.response.text)

    return result


def get_rates_average(response):
    rate = response.json().get('rates')
    result = rate[0].get('mid')
    print(result)
    return result


def get_rates_min_max(response):
    rates = response.json().get('rates')
    result = []
    for item in rates:
        result.append(item)
    print(result)
    return result


def get_difference(response):
    rates = response.json().get('rates')
    result = []
    for item in rates:
        bid = item.get('bid')
        ask = item.get('ask')
        temp = bid - ask
        if temp >= 0:
            result.append(temp)
        else:
            result.append(-temp)
    print(result)
    return result
