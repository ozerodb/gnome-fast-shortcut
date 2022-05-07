import subprocess
import argparse


def _get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n",
        "--name",
        type=str,
        required=True,
        help="the name of the shortcut (displayed in settings)",
    )
    parser.add_argument(
        "-c",
        "--command",
        type=str,
        required=True,
        help="the command to be executed",
    )
    parser.add_argument(
        "-b",
        "--binding",
        type=str,
        required=True,
        help="the combination of keys",
    )
    return parser.parse_args()


def _main():
    # parsing arguments
    args = _get_args()

    # making sure there are no empty strings
    if not all([args.name, args.command, args.binding]):
        print("Arguments cannot be empty strings")
        raise SystemExit

    # defining keys & strings to be used
    key = "org.gnome.settings-daemon.plugins.media-keys custom-keybindings"
    subkey1 = key.replace(" ", ".")[:-1] + ":"
    item_s = "/" + key.replace(" ", "/").replace(".", "/") + "/"
    firstname = "custom"

    # get the current list of custom shortcuts
    get = lambda cmd: subprocess.check_output(["/bin/bash", "-c", cmd]).decode("utf-8")
    array_str = get("gsettings get " + key)

    # in case the array was empty, remove the annotation hints
    command_result = array_str.lstrip("@as")
    current = eval(command_result)

    # make sure the additional keybinding mention is no duplicate
    n = 1
    while True:
        new = item_s + firstname + str(n) + "/"
        if new in current:
            n = n + 1
        else:
            break

    # add the new keybinding to the list
    current.append(new)

    # create the shortcut, set the name, command and shortcut key
    cmd0 = "gsettings set " + key + ' "' + str(current) + '"'
    cmd1 = "gsettings set " + subkey1 + new + " name '" + args.name + "'"
    cmd2 = "gsettings set " + subkey1 + new + " command '" + args.command + "'"
    cmd3 = "gsettings set " + subkey1 + new + " binding '" + args.binding + "'"

    for cmd in [cmd0, cmd1, cmd2, cmd3]:
        subprocess.call(["/bin/bash", "-c", cmd])


if __name__ == "__main__":
    _main()
