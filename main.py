if __name__ == '__main__':
    ticket_quantity = int(input("Number of tickets: "))
    price_sum = 0
    for i in range(ticket_quantity):
        price_current = int(input("Age of ticket " + str(i + 1) + " owner: "))
        if price_current >= 0 and price_current < 18:
            pass
        elif (price_current >= 18 and price_current < 25):
            price_sum += 990
        elif (price_current >= 25):
            price_sum += 1390
    if (ticket_quantity > 3):
        price_sum *= 0.9
    print(price_sum)