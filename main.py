import json
import datetime

# Определяем класс Note
class Note:
    def __init__(self, id, title, body, date):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

# Определяем функцию для сохранения заметок в файл в формате json
def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file, default=lambda x: x.__dict__)

# Определяем функцию для чтения заметок из файла
def read_notes():
    with open('notes.json', 'r') as file:
        notes_json = json.load(file)
        notes = []
        for note_json in notes_json:
            id = note_json['id']
            title = note_json['title']
            body = note_json['body']
            date_str = note_json['date']
            date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
            note = Note(id, title, body, date)
            notes.append(note)
        return notes

# Определяем функцию для добавления заметки
def add_note():
    id = input("Введите идентификатор заметки: ")
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    date = datetime.datetime.now()
    note = Note(id, title, body, date)
    notes = read_notes()
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена")

# Определяем функцию для редактирования заметки
def edit_note():
    id = input("Введите идентификатор заметки, которую хотите отредактировать: ")
    notes = read_notes()
    for note in notes:
        if note.id == id:
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новое тело заметки: ")
            note.title = title
            note.body = body
            note.date = datetime.datetime.now()
            save_notes(notes)
            print("Заметка успешно отредактирована")
            return
    print("Заметка с указанным идентификатором не найдена")

# Определяем функцию для удаления заметки
def delete_note():
    id = input("Введите идентификатор заметки, которую хотите удалить: ")
    notes = read_notes()
    for note in notes:
        if note.id == id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена")
            return
    print("Заметка с указанным идентификатором не найдена")

# Определяем функцию для фильтрации заметок по дате
def filter_notes_by_date():
    date_str = input("Введите дату для фильтрации (в формате YYYY-MM-DD): ")
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    notes = read_notes()
    filtered_notes = [note for note in notes if note.date.date() == date.date()]
    for note in filtered_notes:
        print("Заголовок:", note.title)
        print("Тело:", note.body)
        print("Дата:", note.date)
        print()
    if len(filtered_notes) == 0:
        print("Заметки с указанной датой не найдены")

# Определяем функцию для обработки команд пользователя
def process_command(command):
    if command == "add":
        add_note()
    elif command == "edit":
        edit_note()
    elif command == "delete":
        delete_note()
    elif command == "filter":
        filter_notes_by_date()
    else:
        print("Некорректная команда")

# Основной цикл программы
while True:
    command = input("Введите команду (add, edit, delete, filter) или 'exit' для выхода: ")
    if command == "exit":
        break
    process_command(command)
