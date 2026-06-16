def solution(price):
    discount = {(300_000>price>=100_000):0.95, (500_000>price>=300_000):0.9, (price>=500_000):0.8, (price<100_000):1}
    return int(price * discount[True])