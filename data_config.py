# Configuration file for data
import os
from typing import Final, Dict, List
import sys

# Set working directory to the directory containing the script that was used to invoke the Python interpreter
CWD: Final[str] = sys.path[0]

# Data paths to directories (external drive): /media/len/ExterneFestplateLenCewa/DataBase
OHLC_DP: Final[str] = os.path.join(CWD, 'data', 'ohlc')
VOLP_DP: Final[str] = os.path.join(CWD, 'data', 'vol')

# Column names. These list should only be used for initialization of data frames. Use the corresponding dicts
OHLC_CNL: Final[List[str]] = ['ots', 'open', 'high', 'low',
                              'close', 'vol', 'cts', 'qav', 'not', 'tbbav', 'tbqav', 'ignore', 'cw']
AGTR_CNL: Final[List[str]] = ['atid', 'px',
                              'qx', 'ftid', 'ltid', 'ts', 'bm', 'btpm']
VOL_CNL: Final[list[str]] = ['px', 'qx']

# Reference dictionaries
OHLC_CN: Final[Dict[str, str]] = {
    'openTime': 'ots',
    'open': 'open',
    'high': 'high',
    'low': 'low',
    'close': 'close',
    'volume': 'vol',
    'closeTime': 'cts',
    'quoteAssetVol': 'qav',
    'numberOfTrades': 'not',
    'takerBuyBaseAssetVol': 'tbbav',
    'takerBuyQuoteAssetVol': 'tbqav',
    'ignore': 'ignore',
    'calendarWeek': 'cw',
}
AGTR_CN: Final[Dict[str, str]] = {
    'aggTradeId': 'atid',
    'price': 'px',
    'quantity': 'qx',
    'firstTradeId': 'ftid',
    'lastTradeId': 'ltid',
    'timestamp': 'ts',
    'buyerMaker': 'bm',
    'bestTradPriceMatch': 'btpm',
}
VOLP_CN: Final[Dict[str, str]] = {
    'price': 'px',
    'quantity': 'qx',
}
