import json
import os
import logging


class Notes():
    def __init__(self):
        self.categories_index = []
        self.home_dir = os.path.expanduser("~")
        self.file = f"{self.home_dir}/notes/notes.json"
        self.notes_dict = {}
        self.load_json()


    def load_json(self):
        file_exists = os.path.exists(self.file)
        if file_exists:
            self.load_dict_from_file()
            self.index_dictionary()
        else:
            self.notes_dict = {"general": [["my first note", False]]}
            self.save_dict_to_file()

    def save_dict_to_file(self):
        try:
            f = open(self.file, "w")

        except OSError as e:
            print("Error opening the file. Please ensure the file has appropriate permissions.")
            logging.error(e)

        else:
            json.dump(self.notes_dict, f)
            f.close()

    def load_dict_from_file(self):
        try:
            f = open(self.file, "r")
        except OSError as e:
            print("Error opening the file. Please ensure the file exists and has appropriate permissions.")
            logging.error(e)
        else:
            data = f.read()
            self.notes_dict = json.loads(data)
            self.index_dictionary()
            f.close()


    def display_notes(self):
        for category in self.notes_dict:
            print(f"{self.categories_index.index(category):3d}. {category}")
            i = 0
            for note in self.notes_dict[category]:
                if note[1] is False:
                    print("\t", f"{i :3d}. {note[0]}")
                    i += 1

            ### comprehension didn't work for counting (notes with same contents didn't index properly
            # [print("\t",f"{self.notes_dict[category].index(note):3d} {note[0]}") for note in self.notes_dict[category] if note[1] is False]

    def clear(self):
        safe_delete = input("type 'DELETE' to clear all notes: ")
        if safe_delete == "DELETE":
            self.notes_dict = {}
            self.index_dictionary()
            self.save_dict_to_file()
            print("all notes cleared")
        else:
            print("nothing deleted")

    def save_note(self, note: str, category: str = "general"):
        if category in self.notes_dict:
            self.notes_dict[category].append([note, False])
        else:
            self.notes_dict[category] = [[note, False]]
        self.index_dictionary()
        self.save_dict_to_file()

    def index_dictionary(self):
        self.categories_index = []
        self.categories_index = list(self.notes_dict.keys())

    def remove_note(self,category_id, note_id):
        del self.notes_dict[self.categories_index[category_id]][note_id]
        if len(self.notes_dict[self.categories_index[category_id]]) == 0:
            del self.notes_dict[self.categories_index[category_id]]
        self.save_dict_to_file()
        self.index_dictionary()

    def edit_note(self):
        self.display_notes()
        category_id = int(input("enter a category number for the note to edit: "))
        note_id = int(input("enter a note number for the note to edit: "))
        new_note = input("enter the new note: ")
        new_category = input(f"enter new note category (id or text): ")
        try:
            new_category = int(new_category)
            self.save_note(new_note, self.categories_index[new_category])
        except ValueError:
            self.save_note(new_note, new_category)
        self.remove_note(category_id,note_id)
        self.index_dictionary()

    def forget(self):
        self.display_notes()
        category_id = int(input("enter a category number for the note to forget: "))
        note_id = int(input("enter a note number for the note to forget: "))
        self.remove_note(category_id, note_id)
        self.index_dictionary()

    def help(self):
        string = """
A simple note program
-h print this help text
-r remember something (put in quotes if longer than 1 word
-c put the thing to be remmebered into a category (generic is used if omitted)
-e enter edit mode
-f enter forget mode
--clear clear all notes

if no arguments are supplied, prints out existing notes
"""
        print(string)