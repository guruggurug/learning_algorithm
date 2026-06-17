def solution(numbers, direction):
    # right면 인덱스 +1
    # left면 인덱스 -1
    direction = 1 if direction == 'right' else 0
    answer = []
    if direction:
        return [numbers[-1]] + numbers[0:-1]
    else:
        return numbers[1:] + [numbers[0]]