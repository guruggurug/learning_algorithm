def solution(order):
    price = 0
    for o in order:
        if o == 'anything':
            price += 4500
        elif 'cafelatte' in o:
            price += 5000
        elif 'americano' in o:
            price += 4500
    return price