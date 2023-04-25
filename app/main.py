from fastapi import FastAPI
import nbp

app = FastAPI(
    title='Backend oriented task',
    docs_url='/'
)

rates_url = 'https://api.nbp.pl/api/exchangerates/rates'


@app.get('/average/{code}/{date}')
async def average(code: str, date: str):
    response = nbp.get_response(rates_url + f'/a/{code}/{date}/')
    rate = nbp.get_rates_average(response)

    return {'average': rate}


@app.get('/minmax/{code}/{n}')
async def min_max_average(code: str, n: int):
    response = nbp.get_response(rates_url + f'/a/{code}/last/{n}/')
    rates = nbp.get_rates_min_max(response)
    min_value = rates[0].get('mid')
    max_value = min_value

    for rate in rates:
        if rate.get('mid') < min_value:
            min_value = rate.get('mid')
        if rate.get('mid') > max_value:
            max_value = rate.get('mid')

    print(min_value)
    return {'min': min_value, 'max': max_value}


@app.get('/difference/{code}/{n}')
async def major_difference(code: str, n: int):
    response = nbp.get_response(rates_url + f'/c/{code}/last/{n}/')
    difference = nbp.get_difference(response)
    result = max(difference)

    return {'major': round(result, 4)}
