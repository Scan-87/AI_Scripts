import argparse

# Считываем опции с командной строки
def get_args():
    parser = argparse.ArgumentParser("Sorry, I'm too lazy...")
    parser.add_argument("-z", "--number", help="Initial number Z", required=True)
    parser.add_argument("-w", "--weight", help="Weight vector W", required=True)
    parser.add_argument("-r", "--treshold", help="Treshold R", required=True)
    parser.add_argument("-f", "--file", help="File with dataset", required=True)
    return parser.parse_args()

# Обозначение глобальных переменных для считаных параметров
options = get_args()
Z = options.number
W = options.weight
R = options.treshold
filename = options.file
list_Z = list(Z)
list_W = list(W)

# Подсчет суммы векторов, в "маске" которых стоят единицы
def mask_sum(study, weight):
    rem = 0
    for i in range (0, len(study)):
        if study[i] == '1':
            rem = rem + int(weight[i])
    print("Сумма: " + str(rem))
    return rem


# Варианты развития событий
def True_Positive():
    print("True Positive. Веса не меняются")

def False_Negative(study):
    print("False Negative! Увеличиваем веса на 1")
    for i in range (0, len(study)):
        if study[i] == '1':
            list_W[i] = str(int(list_W[i]) + 1)
    print("W: ", end='')
    print(list_W)

def False_Positive(study):
    print("False Positive! Уменьшаем веса на 1")
    for i in range (0, len(study)):
        if study[i] == '1':
            list_W[i] = str(int(list_W[i]) - 1)
    print("W: ", end='')
    print(list_W)

def True_Negative():
    print("True Negative. Веса не меняются")


# Сравнение ожидаемого значения с подаваемым. Далее проверяется, не превышено ли пороговое значение. В зависимости от этого выбирается дальнейшее действие
def choise(rem, treshold, expect, study):
    if expect == study:
        if rem > treshold:
            True_Positive()
        else:
            False_Negative(study)
    else:
        if rem > treshold:
            False_Positive(study)
        else:
            True_Negative()


# Главная функция
if __name__ == "__main__":
    # открываем файл с значениями цифр A, B, C. По одному в строке
    lessons = open(filename, "r")

    print("Исходный набор весов:")
    print(list_W)
    print("Исходное число:")
    print(list_Z)
    ex = 1
    for line in lessons:
        print("\nПодаем значение " + str(ex) + ":")
        list_A = list(line.rstrip())
        print("W: ", end='')
        print(list_W)
        print(str(ex) + ": ", end='')
        print(list_A)
        currem = mask_sum(list_A, list_W)
        choise(currem, int(R), list_Z, list_A)
        ex += 1
    lessons.close()

