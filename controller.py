import functions as function
import view

def run():
    user_choice = ''
    while user_choice != 6:
        view.menu()
        user_choice = input().strip()
        if user_choice == '1':
            function.show('all')
        elif user_choice == '2':
            function.add_note()
        elif user_choice == '3':
            function.show('all')
            function.note_show_edit_delete('del')
        elif user_choice == '4':
            function.show('all')
            function.note_show_edit_delete('edit')
        elif user_choice == '5':
            function.show('id')
            function.note_show_edit_delete('show')
        elif user_choice == '6':
            view.exit_notes()
            break