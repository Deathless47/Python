'''
Так как я сдаю задание уже после разбора, то решил для себя разобрать показанные вами примеры, поэтому и
есть еще 1 файл 'Les_6_Task_1_1', не для оценки и проверки
'''
import sys
import random

def sum_memory(objects):
    sum_mem = 0
    unique_id = set()
    for key, value in objects.items():
        if key.startswith('__'):
            continue
        elif hasattr(value, '__call__'):
            continue
        elif hasattr(value, '__loader__'):
            continue
        elif id(value) in unique_id:
            continue
        else:
            unique_id.add(id(value))
            sum_mem += sys.getsizeof(value)
            print(f'переменная {key} класса {type(value)} хранит {value} '
                  f'и занимает {sys.getsizeof(value)} байт')

    return sum_mem

array_2 = [random.randint(1, 1_000) for _ in range(10)]
print(array_2)
max_ = max(array_2)
min_ = min(array_2)
max_, min_ = min_, max_

print(array_2)
print('*' * 75)
print(sum_memory(locals()))

'''
Результат по сумме байт, получается аналогичным результату 2 варианта из файла Les_6_Task_1/

[539, 93, 340, 944, 990, 710, 878, 789, 945, 779]
[539, 93, 340, 944, 990, 710, 878, 789, 945, 779]
***************************************************************************
переменная array_2 класса <class 'list'> хранит [539, 93, 340, 944, 990, 710, 878, 789, 945, 779] и занимает 184 байт
переменная max_ класса <class 'int'> хранит 93 и занимает 28 байт
переменная min_ класса <class 'int'> хранит 990 и занимает 28 байт
240
'''

