""""data_structure = [  [1, 2, 3],  {'a': 4, 'b': 5},  (6, {'cube': 7, 'drum': 8}),  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])] ''
"А есть ли универсальное решение для подсчёта суммы всех чисел и длин всех строк?" '"""
def calculate_structure_sum(data_structure):
    sum_ = 0
    for i in data_structure:
        if  isinstance(i,int):
            sum_ = sum_ + i
        elif isinstance(i,str):
            sum_ = sum_ + len(i)
        elif isinstance(i,(list,tuple,set)):
            sum_ = calculate_structure_sum(i) + sum_
        elif isinstance(i,dict):
            sum_ = calculate_structure_sum(i.keys()) + sum_
            sum_ = calculate_structure_sum(i.values()) + sum_
    return sum_

data_structure = [  [1, 2, 3],  {'a': 4, 'b': 5},  (6, {'cube': 7, 'drum': 8}),  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])]
print(calculate_structure_sum(data_structure))








