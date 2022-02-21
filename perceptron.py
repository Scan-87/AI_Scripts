import argparse

def get_args():
    parser = argparse.ArgumentParser("Sorry, I'm too lazy...")
    #parser.add_argument("-z", "--number", help="Initial number Z. Ex: 4", required=True)
    parser.add_argument("-m", "--matrix", help="Weight matrix file. Ex: 4_8463956723", required=True)
    #parser.add_argument("-r", "--treshold", help="Treshold R", required=True)
    parser.add_argument("-d", "--dataset", help="numbers in dataset. Ex: 4,6,9", required=True)
    return parser.parse_args()

options = get_args()
#Z = options.number
D = options.dataset
filename = options.matrix

attribute = {'0': '111001011', '1': '001100010', '2': '011000101', '3': '010110100', '4': '101010010', '5': '110010011', '6': '000111011', '7': '010101000', '8': '111011011', '9': '111010100'}


# Подсчет суммы векторов, в "маске" которых стоят единицы
def mask_sum(study, weight):
    sums = {}
    termlist = []
    for j in range (0, 10):
        ret = 0
        list_study = list(attribute[study])
        for i in range (0, len(list_study)):
            if list_study[i] == '1':
                list_weight = list(weight[str(j)])
                ret = ret + int(list_weight[i])
        sums[j] = ret
        #print("> " + str(j) + ": " + str(ret))
    print("[*] Нашли суммы векторов")
    print(sums)
    maxsum = max(sums.values())
    print("[*] Максимальная сумма - " + str(maxsum))
    
    for k in sums: 
        if sums[k] == maxsum:
            termlist.append(k)
    print("[*] Элемент(ы) с максимальной суммой: ", end='')
    print(termlist)

    # decision making process to adjust weights
    if len(termlist) == 1:
        if termlist[0] == study:
            print("\n[+] True Positive. Ничего не меняем")
            print("[?] В списке сумм максимальная сумма - только у подаваемого числа")
            # do nothing
        else:
            print("\n[-] True Negative")
            print("[?] В списке сумм максимальная сумма - не у подаваемого числа. Нужно увеличить вес подаваемого и уменьшить вес полученного")
            print("[*] Уменьшаем веса вектора " + str(termlist[0]))
            #print("@@@ Now we are entering the danger zone!")
            # study = '4'
            # weight[study] = 857255435
            # attribute[study] = 001100010
            #print(weight[study])
            #print(attribute[study])
            list_W = list(weight[study])
            list_S = list(attribute[study])
            #print(weight[str(termlist[0])])
            list_T = list(weight[str(termlist[0])])
            #print(list_T)

            # decrement weight[str(termlist[0])] with mask attribute[study]
            for m in range (0, len(list_S)):
                #print(list_S[m])
                if list_S[m] == '1':
                    list_T[m] = str(int(list_T[m]) - 1)
            #print(list_T)
            #print(''.join(list_W))
            weight[str(termlist[0])] = ''.join(list_T)
            print("[*] Новые веса:")
            print(weight, sep="")

                    
            # increment weight[study] with mask attribute[study]
            list_W = list(weight[study])
            print("[*] Теперь увеличим вес вектора " + str(study))
            #print(weight[study])
            for n in range (0, len(list_S)):
                if list_S[n] == '1':
                    list_W[n] = str(int(list_W[n]) + 1)
            print("[*] Новые веса: ")
            weight[study] = ''.join(list_W)
            print(weight)
                    
            #print("@@@ Leaving danger zone")
    else:
        for l in range (0, len(termlist)):
            print("[?] В списке максимальных весов несколько чисел несколько чисел")
            if termlist[l] != study:
                print("[*] Число не равно заданному, уменьшаем его веса")
                print("[*] Уменьшаем веса элемента " + str(termlist[l]))
                # decrement weight[str(termlist[l])] with mask attribute[study]
                list_S = list(attribute[study])
                list_T = list(weight[str(termlist[l])])
                for m in range (0, len(list_S)):
                    #print(list_S[m])
                    if list_S[m] == '1':
                        list_T[m] = str(int(list_T[m]) - 1)
                        #print(list_T)
                print("[*] Новые веса: ")
                #print(''.join(list_W))
                weight[str(termlist[l])] = ''.join(list_T)
                print(weight)

            print("[?] Теперь, когда мы покарали лишние числа, моджно увеличить на 1 веса искомого ичсла")
            print("[*] Увеличиваем веса вектора " + study)
            # increment weight[study] with mask attribute[study]
            list_W = list(weight[study])
            #print("Now lets increment weight[study]:")
            #print(weight[study])
            for n in range (0, len(list_S)):
                if list_S[n] == '1':
                    list_W[n] = str(int(list_W[n]) + 1)
            print("[*] Новые веса: ")
            weight[study] = ''.join(list_W)
            print(weight)
    return ret


if __name__ == "__main__":
    matrix = open(filename, 'r')
    weight = {}
    for line in matrix:
        matrsplit = (line.rstrip()).split('_')
        weight[matrsplit[0]] = matrsplit[1]
    print("Матрица весов:")
    for key, value in weight.items():
	    print(key, value)

    #print("Распознаваемая цифра " + Z + ": ")
    #print(attribute[Z])

    data = D.split(',')

    for test in data:
        print("\n[*] Подаем на вход цифру " + str(test))
        mask_sum(test, weight)

