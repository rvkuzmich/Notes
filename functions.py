import file_operations
import Note
import view

note_length = 1

def add_note():
    note = view.create_note(note_length)
    array = file_operations.file_read()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    file_operations.file_write(array, 'a')
    print('Заметка добавлена')

def show(text):
    logic = True
    array = file_operations.file_read()
    if text == 'date':
        date = input('Введите дату в формате дд.мм.гггг: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(Note.Note.map_note(notes))
        if text == 'id':
            logic = False
            print(f'ID: {Note.Note.get_id(notes)}')
        if text == 'date':
            logic = False
            if date in Note.Note.get_date(notes):
                print(Note.Note.map_note(notes))
    if logic:
        print('Заметок нет')

def note_show_edit_delete(text):
    id = input('Введите id заметки: ')
    array = file_operations.file_read()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = view.create_note(note_length)
                Note.Note.set_title(notes, note.get_title())
                Note.Note.set_body(notes, note.get_body())
                Note.Note.set_date(notes)
                print('Заметка сохранена')
            elif text == 'del':
                array.remove(notes)
                print('Заметка удалена')
            elif text == 'show':
                print(Note.Note.map_note(notes))
    if logic:
        print('Такой заметки нет, проверьте правильность id')
    file_operations.file_write(array, 'a')