import requests
from datetime import datetime, timedelta


def get_data_from_api():
    url = "https://services.swpc.noaa.gov/products/noaa-planetary-k-index-forecast.json"
    response = requests.get(url)
    json = response.json()
    three_days_ago = (datetime.now() - timedelta(days=3)).strftime("%Y-%m-%d")
    data = {}
    for entry in json[1:]:
        date = entry[0][:10]
        value = round(float(entry[1]))
        if date < three_days_ago:
            continue
        if date not in data or value > data[date]:
            data[date] = value
    return data


if __name__ == "__main__":
    print(get_data_from_api())
    