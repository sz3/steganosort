import requests

from steganosort.util import dict_decode


def main(server):
    res = requests.get(server).json()
    res = dict_decode(res)
    print(res)


if __name__ == '__main__':
    main('http://localhost:8000')
