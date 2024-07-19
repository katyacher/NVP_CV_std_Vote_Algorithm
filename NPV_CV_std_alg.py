import random
from statistics import stdev
from mtx_equivalence_rel import*

def print_mtx(mtx):
    for i in mtx: 
        for i2 in i: 
            print(i2, end=' ') 
        print()

def NVP_CV_STD_vote_alg(res_lst):
    #Вычисляем среднеквадратическое отклонение, берем его в качестве значения точности (эпсилон).
    epsilon = stdev(res_lst)
    
    #Составляем матрицу согласования
    consensus_mtx = [[0] * len(res_lst) for i in range(len(res_lst))]

    for i in range(len(res_lst)):
        for j in range(len(res_lst)):
            if abs(res_lst[i] - res_lst[j]) <= epsilon:
                consensus_mtx[i][j] = 1
            else:
                consensus_mtx[i][j] = 0

    #проверка на эквивалентность,пока матрица не выпоолняет условие эквивалентности
    #и колличество проведенных булевых композиций на матрице не равно N-1
    
    n = 0
    while not is_equivalent(consensus_mtx) or n == len(res_lst) - 1:
        #изменение матрицы - операция булевых композиций по формуле E^2 = R U R o R = R U R^2
        consensus_mtx = bool_composition(consensus_mtx)
        n+=1

    if not is_equivalent(consensus_mtx):
        print("Voting is not possible, please chack your data")
        return 0,0
    else:
        # подсчет голосов
        answers_lst = [0] * len(res_lst)

        for i in range(len(res_lst)):
            for j in range(len(res_lst)):
                if  consensus_mtx[i][j] == 1:
                    answers_lst[i] += 1

        
        # Ищем строки с максимальным колличеством голосов
        max_value = max(answers_lst, default=None)
       
        max_indexes_lst = [index for index, value in enumerate(answers_lst) if value == max_value] if max_value is not None else []  
        # Если ответов с максимальным кол-вом голосов несколько, выбираем один случайным образом 
        
        if len(max_indexes_lst) > 1:
            max_index = random.choice(max_indexes_lst)
        return res_lst[max_index], max_index
   
        