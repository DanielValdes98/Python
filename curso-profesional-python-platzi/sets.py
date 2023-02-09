# MANEJO DE SETS

def remove_duplicates(some_list):
    without_duplicate = []
    for element in some_list:
        if element not in without_duplicate:
            without_duplicate.append(element)
    return without_duplicate

def remove_duplicates_set(some_list):
    return list(set(some_list))

def run():
    random_list = [1,1,1,2,4,1,5,9,7,5,2,3,4]
    print(remove_duplicates(random_list))
    print(remove_duplicates_set(random_list))

if __name__ == "__main__":
    run()