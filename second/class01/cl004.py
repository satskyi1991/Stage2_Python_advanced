

def bank (sum_of_deposit,years,percent):
    sum = sum_of_deposit * (1 + percent/100)**years
    return sum

print(bank(1000, 1, 15))
