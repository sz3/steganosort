import sys
from json import dumps

from flask import Flask
from steganosort.util import dict_encode


app = Flask(__name__, static_url_path='')


_DATA = {
    1988: 351.57,
    1989: 353.12,
    1990: 354.39,
    1991: 355.61,
    1992: 356.45,
    1993: 357.10,
    1994: 358.83,
    1995: 360.82,
    1996: 362.61,
    1997: 363.73,
    1998: 366.70,
    1999: 368.38,
    2000: 369.55,
    2001: 371.14,
    2002: 373.28,
    2003: 375.80,
    2004: 377.52,
    2005: 379.80,
    2006: 381.90,
    2007: 383.79,
    2008: 385.59,
    2009: 387.43,
    2010: 389.90,
    2011: 391.65,
    2012: 393.86,
    2013: 396.52,
    2014: 398.64,
    2015: 400.83,
    2016: 404.22,
    2017: 406.55,
    2018: 408.52,
    2019: 411.43,
}


@app.route('/')
def index():
    res = dict_encode(_DATA, b'M.Loa CO2.')
    return dumps(res)


if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    app.run(host='0.0.0.0', port=port)
