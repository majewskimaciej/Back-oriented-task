from fastapi import FastAPI
from app.nbp import get_response, get_difference, get_rates_min_max, get_rates_average

app = FastAPI(
    title='Backend oriented task',
    docs_url='/'
)

rates_url = 'https://api.nbp.pl/api/exchangerates/rates'


def min_max_average(rates):
    print(rates)
    min_value = rates[0]
    max_value = min_value

    for rate in rates:
        if rate < min_value:
            min_value = rate
        if rate > max_value:
            max_value = rate

    return {'min': min_value, 'max': max_value}


@app.get('/average/{code}/{date}')
async def get_average(code: str, date: str):
    response = get_response(rates_url + f'/a/{code}/{date}/')
    rate = get_rates_average(response)

    return {'average': rate}


@app.get('/minmax/{code}/{n}')
async def get_min_max_average(code: str, n: int):  # check naming convention for api calls
    response = get_response(rates_url + f'/a/{code}/last/{n}/')
    rates = get_rates_min_max(response)
    result = min_max_average(rates)

    return result


@app.get('/difference/{code}/{n}')
async def get_major_difference(code: str, n: int):
    response = get_response(rates_url + f'/c/{code}/last/{n}/')
    difference = get_difference(response)
    result = max(difference)

    return {'major': round(result, 4)}
