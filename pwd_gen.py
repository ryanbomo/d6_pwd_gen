#!/usr/bin/python

import sys, random, sqlite3, getopt



def create_index():
    satisfied = False
    while not satisfied:
        number_1 = random.randint(1,6)
        number_2 = random.randint(1,6)
        number_3 = random.randint(1,6)
        number_4 = random.randint(1,6)
        number_5 = random.randint(1,6)
        final_num = (10000*number_1)+(1000*number_2)
        final_num = final_num + (100*number_3)+(10*number_4)
        final_num = final_num +(1*number_5)
        if (final_num < 66634):
            satisfied = True
    return final_num

def create_dict(db_name):
    word_dict = {}
    db = sqlite3.connect(db_name)
    c = db.cursor()
    sqlite_get = "SELECT * FROM words;"
    for row in c.execute(sqlite_get):
        word_dict[row[0]] = row[1]
    return word_dict

def create_numbers_list(num_words):
    list_num = []
    for i in range(num_words):
        list_num.append(create_index())
    return list_num

def create_password(db_name, num_words):
    word_dict = create_dict(db_name)
    list_num = create_numbers_list(num_words)
    password = ""
    for i in list_num:
        print(str(i) + " - " + word_dict[i])
        password = password + word_dict[i]
    return password

def quick(num):
    password = create_password("words.db", num)
    return password

'''
def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hd:n:")
    except getopt.GetoptError:
        print('pwd_gen.py -d <database_name> -n <number_words>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('pwd_gen.py -d <database_name> -n <number_words>')
            sys.exit(2)
        elif opt in ("-d"):
            database_name = arg
        elif opt in ("-n"):
            word_num = int(arg)
    password = create_password(database_name, word_num)
    print(password)
    return password

if __name__ == "__main__":
    main(sys.argv[1:])

    
'''
