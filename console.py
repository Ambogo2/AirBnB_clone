import cmd

class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb)'

    def do_quit(self):
        quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()