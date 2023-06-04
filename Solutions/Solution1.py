def average_multiples_of_3(numbers):
    sum_multiples_3 = 0
    count_multiples_3 = 0

    for num in numbers:
        if num % 3 == 0:
            sum_multiples_3 += num
            count_multiples_3 += 1

    if count_multiples_3 == 0:
        return -1
    else:
        average_multiples_3 = sum_multiples_3 / count_multiples_3
        return average_multiples_3
