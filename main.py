import sqlite3

from NPV_CV_std_alg import NVP_CV_STD_vote_alg as NVP_CV_STD_vote_alg

#class Data(enum.Enum):
#   ID = 0
#   VERSION_ID = 1
#   VERSION_NAME = 2
#   VERSION_RELIABILITY = 3
#   VERSION_COMMON_COORDINATES = 4
#   VERSION_ANSWER = 5
#   CORRECT_ANSWER = 6
#   MODULE_ID = 7
#   MODULE_NAME = 8
#   MODULE_CONNECTIVITY_MATRIX = 9
#   MODULE_ITERATION_NUM = 10
#   EXPERIMENT_NAME = 11

db_name = 'experiment_edu.db'

def input_num(user_str='Введите пункт меню (число от 1 до 3): ', limit=(float('-inf'), float('inf')), target_type=int,
              included_borders=False, round_to=4):
    incorrect_val = True
    while incorrect_val:
        try:
            user_num = target_type(input(user_str))
            if (limit[0] >= user_num >= limit[1] and not included_borders) or \
                    (limit[0] > user_num > limit[1] and included_borders):
                raise ValueError(f'Expected value from {limit[0]} to {limit[1]}')
        except ValueError as err:
            print('Entered value is incorrect! ' + str(err))
            incorrect_val = True
        except Exception as err:
            print('Unknown error! ' + str(err))
            incorrect_val = True
        else:
            user_num = user_num.__round__(round_to)
            incorrect_val = False
    return user_num

def load_data_and_vote(module_num, experiment_name, experiment_num):
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    cursor.execute("SELECT * FROM experiment_data WHERE experiment_name=(?) Limit (?)*(?)", (experiment_name, experiment_num, module_num ))
    result = cursor.fetchall()

    #получаем 1000 ответов от эксперимента, упаковываем в список словарей, 
    # где ключ - номер версии, значение - ответ от версии, 
    # длинна списка - кол-во экспериментов.

    version_answers = []
    experiment_data = {}
    i = module_num 
    for row in result:
        experiment_data[row[2]] = row[5] # или __dict__(row[Data.VERSION_NAME],row[Data.VERSION_ANSWER])
        i -= 1
        if i == 0:
            version_answers.append(experiment_data.copy())
            i = module_num
            #experiment_data.clear() - не нужно, так как имена ключей повторяются и значения перезаписываются

    res_lst = []
    corrent_experiment = 0
    print(f"номер эксперимента \tкорректный ответ \tномер версии ")
    for experiment in version_answers:
        res_lst = [value for value in experiment.values()]
        try:
            correct_answer, version_num = NVP_CV_STD_vote_alg(res_lst)
            print(f" {corrent_experiment} \t\t\t{correct_answer} \t\t {list(experiment.keys())[version_num]} ")
            corrent_experiment+=1
        except Exception as err:
            print("Some exception: ", str(err))
       
    return 0



def main():

    while True:

        print("Выберете модуль для проведения голосования:\n")
        print("1. Модуль 3 (3 версии)\n")
        print("2. Модуль 5 (5 версий)\n")
        print("3. Модуль 7 (7 версий)\n")
        print("4. Exit")
        menu = input_num() #ввод значения с консоли, проверка на корректность с обработкой исключений
        
        if menu == 1:
            module_num = 3
            experiment_name = 'M3_I50000'
            experiment_num = 1000
            load_data_and_vote(module_num, experiment_name, experiment_num)
        elif menu == 2:
            module_num = 5
            experiment_name = 'M5_I50000'
            experiment_num = 1000
            load_data_and_vote(module_num, experiment_name, experiment_num)
        elif menu == 3:
            module_num = 7
            experiment_name = 'M7_I50000'
            experiment_num = 1000
            load_data_and_vote(module_num, experiment_name, experiment_num)
        elif menu == 4:
            break
        else:
            print("Unknown menu item. Try again")

    return 0

main()


