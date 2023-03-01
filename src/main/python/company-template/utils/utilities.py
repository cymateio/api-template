import yaml
import os
import datetime


# This is only used in Test Class + Run Test
def read_config(file_path):
    basepath = os.path.realpath(os.path.dirname(__file__))
    config_directory = basepath.split("src/")[0] + "config/"
    with open(config_directory + file_path, "r") as file:
        data = yaml.safe_load(file)
    return data


def gather_queries(queries):
    query_list = [(f"{k}={v}") for k,v in queries.items()]
    return "&".join(query_list)

# data = {
#     "latitude": "37.34",
#     "longitude": "-121.89",
#     "hourly": "temperature_2m",
#     "current_weather": "true",
#     "temperature_unit": "celsius",
#     "start_date": "2023-02-22",
#     "end_date": "2023-02-23"
# }

# start_day = datetime.date.today() # .strftime("%Y-%m-%d")
# end_day = start_day + datetime.timedelta(days=5)

def get_date_today():
    return datetime.date.today()

def get_date_future(n):
    start_day = get_date_today()
    return start_day + datetime.timedelta(days=n)
    # return end_day.strftime("%Y-%m-%d")

