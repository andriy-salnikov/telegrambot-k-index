from data_request import get_data_from_api


def draw_data(data: dict):
    for element in data:
        print(f"{element}: {data[element]}")


if __name__ == "__main__":
    draw_data(get_data_from_api())