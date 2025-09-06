def square_numbers(*args, round_result=False):

    squared = []
    for num in args:
        sq = num ** 2
        if round_result:
            sq = round(sq)
        squared.append(sq)
    return squared



print(square_numbers(2, 3, 4))  
print(square_numbers(1.5, 2.3, round_result=True))  
