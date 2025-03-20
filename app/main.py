import os


def copy_file(command: str) -> None:
    try:
        command_split = command.split()
        if len(command_split) != 3 or command_split[0] != "cp":
            return

        if command_split[1] == command_split[2]:
            return

        if not os.path.isfile(command_split[1]):
            return

        with (open(command_split[1], "r") as file_in,
              open(command_split[2], "w") as file_out):
            file_out.write(file_in.read())
    except IndexError:
        return
