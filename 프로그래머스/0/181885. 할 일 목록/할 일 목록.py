def solution(todo_list, finished):
    todo_status = zip(todo_list, finished)
    return [i for i, j in todo_status if not j]