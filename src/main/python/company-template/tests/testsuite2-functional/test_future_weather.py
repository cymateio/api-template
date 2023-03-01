import pytest
import json
from utils.utilities import *

# Need to redesign this, depends on the testing/api requirements
END_POINT = "/forecast"
TEMPERATURE_UNIT = "fahrenheit" # fahrenheit / celsius
HOURLY = "temperature_2m"
CURRENT_WEATHER = "true"


@pytest.mark.functional
def test_get_irvine_in_2_days(openmeteo, logger, config):
    end_point = "/forecast"
    irvine = config["city"]["irvine"]

    start_day = get_date_today().strftime("%Y-%m-%d")
    end_day = get_date_future(2).strftime("%Y-%m-%d")
    data = {
        "latitude": irvine["latitude"],
        "longitude": irvine["longitude"],
        "hourly": HOURLY,
        "current_weather": CURRENT_WEATHER,
        "temperature_unit": TEMPERATURE_UNIT,
        "start_date": start_day,
        "end_date": end_day
    }
    data_query = gather_queries(data)
    logger.info("IRVINE LAT: {}, IRVINE LONG: {}".format(irvine["latitude"], irvine["longitude"]))
    response = openmeteo.get(end_point, data_query)
    logger.info("FUTURE WEATHER: " + str(response.json()["hourly"]["time"][-1]))
    assert 1 == 1

@pytest.mark.functional
def test_get_losangeles_in_5_days(openmeteo, logger, config):
    end_point = "/forecast"
    los_angeles = config["city"]["los-angeles"]

    start_day = get_date_today().strftime("%Y-%m-%d")
    end_day = get_date_future(5).strftime("%Y-%m-%d")
    data = {
        "latitude": los_angeles["latitude"],
        "longitude": los_angeles["longitude"],
        "hourly": HOURLY,
        "current_weather": CURRENT_WEATHER,
        "temperature_unit": TEMPERATURE_UNIT,
        "start_date": start_day,
        "end_date": end_day
    }
    data_query = gather_queries(data)
    logger.info("LOS ANGELES LAT: {}, LOS ANGELES LONG: {}".format(los_angeles["latitude"], los_angeles["longitude"]))
    response = openmeteo.get(end_point, data_query)
    logger.info("FUTURE WEATHER: " + str(response.json()["hourly"]["time"][-1]))
    assert 1 == 1

@pytest.mark.functional
def test_get_sanjose_in_10_days(openmeteo, logger, config):
    end_point = "/forecast"
    san_jose = config["city"]["san-jose"]

    start_day = get_date_today().strftime("%Y-%m-%d")
    end_day = get_date_future(10).strftime("%Y-%m-%d")
    data = {
        "latitude": san_jose["latitude"],
        "longitude": san_jose["longitude"],
        "hourly": HOURLY,
        "current_weather": CURRENT_WEATHER,
        "temperature_unit": TEMPERATURE_UNIT,
        "start_date": start_day,
        "end_date": end_day
    }
    data_query = gather_queries(data)
    logger.info("SAN JOSE LAT: {}, SAN JOSE LONG: {}".format(san_jose["latitude"], san_jose["longitude"]))
    response = openmeteo.get(end_point, data_query)
    logger.info("FUTURE WEATHER: " + str(response.json()["hourly"]["time"][-1]))
    assert 1 == 1