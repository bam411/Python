file = 'Homework_8/book.txt'
people = []
id = 0


def menu():
    isRunning = True
    while isRunning:
        read()
        print('\n' + '========================')
        print('1: Показать контакты')
        print('2: Добавить контакт')
        print('3: Удалить контакт')
        print('4: Поиск контакта')
        print('5: Редактирование')
        print('6: Выход')
        print('========================')
        select = input('Выберите желаемое действие: ')

        if select == '1':
            show()
        elif select == '2':
            add()
        elif select == '3':
            delete()
        elif select == '4':
            search()
        elif select == '5':
            work = edit()
            if work:
                change(work)
        elif select == '6':
            exit()


def read():
    global people, id

    with open(file, "r", encoding="utf-8") as f:
        people = [i.strip() for i in f]
        if people:
            id = int(people[-1][0])
        return people


def show():
    if not people:
        print("Записей нет")
    else:
        print(*people, sep="\n")


def add():
    global id

    array = ['Имя', 'Номер телефона']
    answers = []
    for i in array:
        answers.append(data_collection(i))

    if not exist_contact(0, " ".join(answers)):
        id += 1
        answers.insert(0, str(id))

        with open(file, 'a', encoding="utf-8") as f:
            f.write(f'{" ".join(answers)}\n')
        print("Запись добавлена\n")
    else:
        print("Запись уже есть")


def delete():
    global people

    symbol = "\n"
    show()
    delete_record = input("Введите id: ")

    if exist_contact(delete_record, ""):
        people = [k for k in people if k[0] != delete_record]

        with open(file, 'w', encoding="utf-8") as f:
            f.write(f'{symbol.join(people)}\n')
        print("Запись удалена\n")
    else:
        print("Введенные данные неверны")


def change(data_tuple):
    global people
    symbol = "\n"

    record_id, num_data, data = data_tuple

    for i, v in enumerate(people):
        if v[0] == record_id:
            v = v.split()
            v[int(num_data)] = data
            if exist_contact(0, " ".join(v[1:])):
                print("Запись уже есть")
                return
            people[i] = " ".join(v)
            break

    with open(file, 'w', encoding="utf-8") as f:
        f.write(f'{symbol.join(people)}\n')
    print("Запись изменена\n")


def search():
    search_data = exist_contact(0, input("Поиск: "))
    if search_data:
        print(*search_data, sep="\n")
    else:
        print("Введенные данные неверны")


def exist_contact(record_id, data):
    if record_id:
        candidates = [i for i in people if record_id in i[0]]
    else:
        candidates = [i for i in people if data in i]
    return candidates


def data_collection(num):
    answer = input(f"Введите {num}: ")
    while True:
        if num in "Имя":
            if answer.isalpha():
                break
        if num == "Номер телефона":
            if answer.isdigit():
                break
        answer = input(f"Введите {num}: ")
    return answer


def edit():
    add_dict = {"1": "Имя", "2": "Номер телефона"}

    show()
    record_id = input("Введите id: ")

    if exist_contact(record_id, ""):
        while True:
            print("\nЧто хотите поменять?")
            change = input("1. Имя\n"
                           "2. Номер телефона\n"
                           "3. Выход\n")

            match change:
                case "1" | "2":
                    return record_id, change, data_collection(add_dict[change])
                case "3":
                    return 0
                case _:
                    print("Попробуйте снова.")
    else:
        print("Введенные данные неверны")


menu()
