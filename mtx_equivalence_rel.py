def is_transitive(matrix): 
    for i in range (len(matrix)):
        for j in range (len(matrix)):
            if (matrix[i][j]): # если выполняется отношение между элементами ij
                for k in range (len(matrix)): 
                    if (matrix[j][k]): # проверка, выполняется ли отношение jk
                        if not (matrix[i][k]): return False # выполняется ли отношение ik, если не выполняется, то возвращаем значение false
    return True

def is_reflexive(mtx):
    for i in range(len(mtx)):
        for j in range(len(mtx)):
            if not (mtx[i][j] == mtx[j][i]):
                return False   
    return True

def is_simmetric(mtx):
    #for k in range(0,n-1):
    #   for l in range(k+1,n):
    for i in range(1, len(mtx)):
        for j in range(i):
            if mtx[i][j] != mtx[j][i]:
                return False
    return True

def is_equivalent(rel):
    return is_reflexive(rel) and is_simmetric(rel) and is_transitive(rel)

def bool_composition(mtx):
    eq_mtx =  [[0] * len(mtx) for i in range(len(mtx))]
    for i in range(len(mtx)):
        for j in range(len(mtx)):
            for k in range(len(mtx)):
                eq_mtx[i][j] |= mtx[i][k] and mtx[k][j]
    return eq_mtx #операция булевых композиций
    
def print_mtx(mtx):
    for i in mtx: 
        for i2 in i: 
            print(i2, end=' ') 
        print()
    



