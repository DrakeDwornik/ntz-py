#! python3
import os
import notes
import getopt
import sys


# add your code in this file


# main function
def cli(args):
    notes_object = notes.Notes()
    opts, args = get_args(args)
    category = "general"
    remember_mode = False
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            notes_object.help()
            exit()
        elif opt == "-e":
            notes_object.edit_note()
        elif opt == "-r":
            remember_mode = True
            note = arg
        elif opt == "-c":
            category = arg
        elif opt == "-f":
            notes_object.forget()
        elif opt == "--clear":
            notes_object.clear()
            exit()
    if remember_mode:
        notes_object.save_note(note, category)
    notes_object.display_notes()

    # except:
    #     notes_object.display_notes()

# def

def get_args(args):
    opts, args = getopt.getopt(args, "hc:r:fe",["clear", "help"])
    # print((opts, args))
    return (opts, args)
    # return os.sys.argv


# run the main function

if __name__ == '__main__':
    cli(sys.argv[1:])
