# gnome-fast-shortcut

Python script to quickly add a keyboard shortcut to your GNOME environment, without leaving the command line.

The functional part of the script is taken from [this *Ask Ubuntu* answer](https://askubuntu.com/a/597414), I simply added an `argparse`-based interface to make it harder to misuse the script.

## Usage

### 1. Get the script

#### Via wget

```bash
wget -q https://raw.githubusercontent.com/ozerodb/gnome-fast-shortcut/main/create-kb-shortcut.py
```

#### Via curl

```bash
curl -sO https://raw.githubusercontent.com/ozerodb/gnome-fast-shortcut/main/create-kb-shortcut.py
```

#### Manually

Download the repository or copy-paste the content of `create-kb-shortcut.py` into your own Python script.

### 2. Set a new keyboard shortcut

```bash
python3 create-kb-shortcut.py --name=... --command=... --binding=...
```

or

```bash
python3 create-kb-shortcut.py -n=... -c=... -b=...
```

Some of the most used keys:

```bash
Super key:                 <Super>
Control key:               <Primary> or <Control>
Alt key:                   <Alt>
Shift key:                 <Shift>

numbers:                   1 (just the number)
letters:                   T (just the letter)
Spacebar:                  space
Slash key:                 slash
```

## Examples

### Launching the terminal with <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>T</kbd>

```bash
python3 create-kb-shortcut.py --name='Launch the terminal' --command='gnome-terminal' --binding='<Ctrl><Alt>T'
```

### Launching the file explorer with <kbd>Super</kbd> + <kbd>F</kbd>

```bash
python3 create-kb-shortcut.py --name='Launch the file explorer' --command='nautilus' --binding='<Super>F'
```
