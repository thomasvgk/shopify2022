from csv import reader

def find_median(numbers: list) -> float:
    # Returns the median value of a set of numbers.

    nums = sorted(numbers)
    middle = len(nums) // 2 

    if len(nums) % 2 != 0:
        median =  nums[middle]
    else:
        median = (nums[middle] + nums[middle- 1]) / 2

    return median

def clmn_list(file_name: str, column_name: str) -> list:
    # Creates a list of all observations in a column from a .csv file. Can only take quantitative data.

    column = list()

    with open(file_name, newline='') as file:

        data = reader(file)
        id_vars = next(data)
        pos = id_vars.index(column_name)

        for line in data:
           column.append(float(line[pos]))

    return column

order_amounts = (clmn_list('2019 Winter Data Science Intern Challenge Data Set - Sheet1.csv', 'order_amount' ))
median = find_median(order_amounts)
print(f'The median is {median}.')