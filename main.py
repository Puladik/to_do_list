import sqlite3
#with sqlite3.connect('todolist.db') as con: \\\\\\\\\\\\\\\\\\\\\\\\\\\\
def create():
        con = sqlite3.connect('todolist.db')
        cursor = con.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        complited INTEGER DEFAULT 0
        )''')
        con.commit()
        con.close()

def add(title, description):
        con = sqlite3.connect('todolist.db')
        cursor = con.cursor()
        cursor.execute('INSERT INTO tasks (title, description) VALUES (?, ?)', (title, description))
        con.commit()
        con.close()

def view():
        con = sqlite3.connect('todolist.db')
        cursor = con.cursor()
        cursor.execute('SELECT * FROM tasks')
        tasks = cursor.fetchall()
        con.close()
        if not tasks:
            print('Список задач пустой')
        else:
            for task in tasks:
                print(f"Номер: {task[0]}, Заголовок: {task[1]}, Описание: {task[2]}, Статус: {'Выполнено' if task[3] else 'Не выполнено'}")

def completed(task_id):
        con = sqlite3.connect('todolist.db')
        cursor = con.cursor()
        cursor.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (task_id,))
        con.commit()
        con.close()

def delete(task_id):
        con = sqlite3.connect('todolist.db')
        cursor = con.cursor()
        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        con.commit()
        con.close()

def delete_all():
        con = sqlite3.connect('todolist.db')
        cursor = con.cursor()
        cursor.execute('DELETE FROM tasks')
        con.commit()
        con.close()

def main():
    create()
    while True:
        print("\nМеню:")
        print("1. Добавить задачу")
        print("2. Просмотреть задачи")
        print("3. Отметить задачу как выполненную")
        print("4. Удалить задачу")
        print("5. Удалить все задачи")
        print("6. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите заголовок задачи: ")
            description = input("Введите описание задачи: ")
            add(title, description)
            print("Задача добавлена успешно!")
        elif choice == "2":
            view()
        elif choice == "3":
            task_id = int(input("Введите ID задачи для отметки как выполненной: "))
            completed(task_id)
            print("Задача отмечена как выполненная!")
        elif choice == "4":
            task_id = int(input("Введите номер задачи для удаления: "))
            delete(task_id)
            print("Задача удалена")
        elif choice == "5":
            delete_all()
            print("Все задачи удалены")
        elif choice == "6":
            print("До встречи")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")
if __name__ == "__main__":
    main()