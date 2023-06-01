# InterpoLation search
# Интерполяционный поиск
# работает быстрее чем бинарный поиск
import random
 
n = 40
arr = []
for i in range(n):
    number = random.randint(1, 100)
    arr.append(number)

to_search = random.randint(1, 100)
answer = -1

########################################################################     

arr.sort()
left = 0
right = len(arr) - 1
while (left <= right and
        to_search >= arr[left] and
        to_search <= arr[right]):
    #_____________________________________________________
    part1 = float(right - left) / (arr[right] - arr[left])
    part2 = to_search - arr[left]
    # Поскольку индекс должен быть целым числом
    # Мы преобразуем part1 * part2 d wtkjt
    index = left + int(part1 * part2)
    #_____________________________________________________
    
    if arr[index] == to_search:
        answer = index
        break
    elif arr[index] < to_search:
        left = index + 1
    else:
        right = index - 1
            
########################################################################     

print(arr)
print(to_search)
print('___________________')

if answer != -1:
    print(f'Элемент в списка был, его индекс:{answer}') 
else:
    print('Элемента в списке не было')        