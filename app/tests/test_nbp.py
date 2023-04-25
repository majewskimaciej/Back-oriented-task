from app.nbp import get_rates_average, get_rates_min_max, get_difference


def test_nbp_average():
    temp = [{'no': '001/A/NBP/2022', 'effectiveDate': '2022-01-03', 'mid': 4.0424}]
    result = get_rates_average(temp)
    assert result == 4.0424


def test_nbp_min_max_average():
    temp = [{'no': '079/A/NBP/2023', 'effectiveDate': '2023-04-24', 'mid': 4.1905},
            {'no': '080/A/NBP/2023', 'effectiveDate': '2023-04-25', 'mid': 4.1649}]
    result = get_rates_min_max(temp)
    assert result == [4.1905, 4.1649]


def test_nbp_difference():
    temp = [{'no': '079/C/NBP/2023', 'effectiveDate': '2023-04-24', 'bid': 4.1629, 'ask': 4.2471},
            {'no': '080/C/NBP/2023', 'effectiveDate': '2023-04-25', 'bid': 4.1329, 'ask': 4.2163}]
    result = get_difference(temp)
    assert result == [0.08420000000000005, 0.08340000000000014]
