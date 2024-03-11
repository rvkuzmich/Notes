import Note

def create_note(number):
    title = check_input_text_length(input('Введите заголовок: '), number)
    body = check_input_text_length(input('Введите текст заметки: '), number)
    return Note.Note(title = title, body = body)

def menu():
    print('Программа "Заметки".\nДоступные функции:\n1 - Показать все заметки, 2 - Добавить заметку,'+
          '\n3 - Удалить заметку, 4 - Редактировать заметку,\n5 - Показать заметку по id, 6 - Выход')

def check_input_text_length(text, n):
    while len(text) < n:
        print(f'Текст не может быть короче {n} символов\n')
        text = input('Введите текст: ')
    else:
        return text
    
def exit_notes():
    print('Завершение работы')