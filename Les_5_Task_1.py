'''
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал
(т.е. 4 числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
'''
from collections import namedtuple


num_company = int(input('Введите количество предприятий: '))
total_profit = 0

company = namedtuple('company', 'name_company, quarter_1, quarter_2, quarter_3, quarter_4, profit_company')
companys = []

for i in range(num_company):
    name_company = input(f"Название предприятия {i+1}: ")
    quarter_1 = float(input("Прибыль за 1 квартал: "))
    quarter_2 = float(input("Прибыль за 2 квартал: "))
    quarter_3 = float(input("Прибыль за 3 квартал: "))
    quarter_4 = float(input("Прибыль за 4 квартал: "))
    profit_company = quarter_1 + quarter_2 + quarter_3 + quarter_4
    total_profit += profit_company
    companys.append(company(name_company=name_company, quarter_1=quarter_1, quarter_2=quarter_2, quarter_3=quarter_3, quarter_4=quarter_4, profit_company=profit_company))

average_profit = total_profit / num_company
print(f'Средняя прибыль для всех предприятий = {average_profit}')

for company in companys:
    if company.profit_company >= average_profit:
        print(f'У предприятия {company.name_company}  прибыль выше среднего')
    else:
        print(f'У предприятия {company.name_company}  прибыль ниже среднего')

