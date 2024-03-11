import Note

def file_write(array, mode):
    file = open('notes.csv', mode = 'w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open('notes.csv', mode = mode, encoding='utf-8')
    for notes in array:
        file.write(Note.Note.to_string(notes) + '\n')
    file.close

def file_read():
    try:
        array = []
        file = open('notes.csv', 'r', encoding='utf-8')
        notes = file.read().strip().split('\n')
        for string in notes:
            split_string = string.split(';')
            note = Note.Note(id = split_string[0], date = split_string[1], title = split_string[2], body = split_string[3])
            array.append(note)
    except Exception:
        print('Заметок нет')
    finally:
        return array