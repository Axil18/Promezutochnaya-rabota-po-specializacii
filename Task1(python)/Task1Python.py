import json
import datetime

NOTES_FILE = "notes.json"

def load_notes():
    try:
        with open(NOTES_FILE, "r") as file:
            notes_data = json.load(file)
    except FileNotFoundError:
        notes_data = []
    return notes_data

def save_notes(notes_data):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes_data, file, indent=4)

def create_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.datetime.now().isoformat()
    note = {
        "id": len(notes_data) + 1,
        "title": title,
        "body": body,
        "timestamp": timestamp
    }
    notes_data.append(note)
    save_notes(notes_data)
    print("Заметка успешно создана.")

def read_notes():
    if not notes_data:
        print("Список заметок пуст.")
    else:
        print("Список заметок:")
        for note in notes_data:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Дата/время создания: {note['timestamp']}")
            print("-----------------------")

def edit_note():
    note_id = int(input("Введите ID заметки, которую хотите отредактировать: "))
    for note in notes_data:
        if note["id"] == note_id:
            new_title = input("Введите новый заголовок заметки: ")
            new_body = input("Введите новый текст заметки: ")
            note["title"] = new_title
            note["body"] = new_body
            note["timestamp"] = datetime.datetime.now().isoformat()
            save_notes(notes_data)
            print("Заметка успешно отредактирована.")
            break
    else:
        print("Заметка с указанным ID не найдена.")

def delete_note():
    note_id = int(input("Введите ID заметки, которую хотите удалить: "))
    for note in notes_data:
        if note["id"] == note_id:
            notes_data.remove(note)
            save_notes(notes_data)
            print("Заметка успешно удалена.")
            break
    else:
        print("Заметка с указанным ID не найдена.")

def main_menu():
    print("=== Меню заметок ===")
    print("1. Просмотреть список заметок")
    print("2. Создать новую заметку")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("0. Выйти")
    print("===================")

notes_data = load_notes()

while True:
    main_menu()
    choice = input("Выберите пункт меню (введите соответствующую цифру): ")
    if choice == "1":
        read_notes()
    elif choice == "2":
        create_note()
    elif choice == "3":
        edit_note()
    elif choice == "4":
        delete_note()
    elif choice == "0":
        break
    else:
        print("Некорректный ввод. Попробуйте снова.")

print("Программа завершена.")