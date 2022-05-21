per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
if __name__ == '__main__':
    money = int(input())
    deposit = list(i * money / 100 for i in per_cent.values())
    print(deposit)
    print("Максимальная сумма, которую вы можете заработать —", max(deposit))