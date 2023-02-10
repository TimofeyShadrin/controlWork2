import datetime

import note
import repository
import utils

atr_of_note = {'id': '',
               'Added': '',
               'Title': '',
               'Body': ''}

list_of_notes = []


def view():
    global list_of_notes
    print('Commands:\n'
          '   add - add note,\n'
          '   list - view all notes,\n'
          '   find - find a note by criteria,\n'
          '   del - delete not by id,\n'
          '   help - print this menu,\n'
          '   update - update note by id,\n'
          '   exit')
    while True:
        choose = input('Please enter the command: ')
        if choose == 'add':
            title = input('Please enter the title: ')
            body = input('Please enter the message: ')
            object_note = note.Note(title, body)
            list_of_notes.append(dict(zip(atr_of_note, [object_note.get_id(),
                                                        str(object_note.get_create_date()).rsplit('.', 1)[0],
                                                        object_note.get_title(),
                                                        object_note.get_text()])))
            repository.save_notes(*list_of_notes)
            list_of_notes = []
            test = str(object_note.get_create_date()).rsplit('.', 1)[0]
            print(datetime.datetime.strptime(test, "%Y-%m-%d %H:%M:%S"))
        elif choose == 'help':
            print('Commands:\n'
                  '   add - add note,\n'
                  '   list - view all notes,\n'
                  '   find - find a note by criteria,\n'
                  '   del - delete not by id,\n'
                  '   help - print this menu,\n'
                  '   exit')
        elif choose == 'list':
            if not repository.read_notes():
                print('No notes found')
            else:
                for row in repository.read_notes():
                    list_of_notes.append(row)
                for your_note in sorted(list_of_notes, key=lambda item: int(item.get('id'))):
                    utils.print_dict(your_note)
            list_of_notes = []
        elif choose == 'find':
            print('Subcommands:\n'
                  '   id - find by id,\n'
                  '   date - find by regex of date,\n'
                  '   exit')
            answer = input('Please input subcommand: ')
            if answer == 'id':
                index = input('Please enter id: ')
                if not repository.get_by_id(index):
                    print(f'No note with id = {index} found')
                else:
                    utils.print_dict(repository.get_by_id(index))
                print('You are back in the main menu')
            elif answer == 'date':
                regex = input('Please enter part of date: ')
                if not repository.get_by_date(regex):
                    print(f'No note with date = {regex} found')
                else:
                    utils.print_dict(repository.get_by_date(regex))
                print('You are back in the main menu')
            elif answer == 'exit':
                print('You are back in the main menu')
            else:
                print('Your input is incorrect')
                print('You are back in the main menu')
        elif choose == 'del':
            index = input('Enter the id\'s number to delete your note: ')
            if not repository.delete_by_id(index):
                print(f'No note with id = {index} found')
            else:
                print(f'Note deleted successfully')
            print('You are back in the main menu')
        elif choose == 'update':
            index = input('Please enter id of note for update: ')
            if not repository.get_by_id(index):
                print(f'No note with id = {index} found')
            else:
                title = input('Please enter the title: ')
                body = input('Please enter the message: ')
                repository.delete_by_id(int(index))
                object_note = note.Note(title, body)
                repository.save_by_id(index,
                                      dict(zip(atr_of_note, [int(index),
                                                             str(object_note.get_create_date()).rsplit('.', 1)[0],
                                                             object_note.get_title(),
                                                             object_note.get_text()])))
        elif choose == 'exit':
            print('Good bye')
            break
        else:
            print('Your input is incorrect')
