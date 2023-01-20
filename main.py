import requests
import matplotlib.pyplot as plt


# Url da API para taxa de desocupação trimestral de indivíduos com 14 anos ou mais
URL = "https://apisidra.ibge.gov.br/values/t/6380/n1/all/v/4098/p/all/d/v4098%201"


def get_json(url):
    page = requests.get(url)
    content = page.json()
    return content[1:]


def prepare_data(json):
    trimester = 3
    year = 2012

    x = []
    y = []

    for data in json:
        x.append(year + trimester / 12)
        y.append(float(data["V"]))

        trimester += 1

        if trimester == 12:
            year += 1
            trimester = 0
    return x, y


def plot_data(data):
    plt.plot(data[0], data[1])
    plt.title('Desemprego trimestral')
    plt.xlabel('Tempo')
    plt.ylabel('Desemprego em pontos percentuais')
    plt.show()


def main():
    json = get_json(URL)
    data = prepare_data(json)
    plot_data(data)


main()