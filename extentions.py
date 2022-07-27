import json
import requests
from lxml import etree
from config import currency_map


class APIException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException('Невозможно перевести в ту же валюту')

        try:
            quote_key = currency_map[quote]
        except KeyError:
            raise APIException(f'Неизвестная валюта: {quote}')

        try:
            base_key = currency_map[base]
        except KeyError:
            raise APIException(f'Неизвестная валюта: {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_key}&tsyms={base_key}")
        total_base = json.loads(r.content)[currency_map[base]] * amount
        return total_base