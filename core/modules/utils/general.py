import os
from pystyle import Colors, Colorate

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def ascii_art():
    art = """
    __ __      _ _____                                 
   / //_/___ _(_) ___/_________ _____  ____  ___  _____
  / ,< / __ `/ /\__ \/ ___/ __ `/ __ \/ __ \/ _ \/ ___/
 / /| / /_/ / /___/ / /__/ /_/ / / / / / / /  __/ /    
/_/ |_\__,_/_//____/\___/\__,_/_/ /_/_/ /_/\___/_/ 26

❱ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ /ᴊᴡᴇ0
"""
    print(Colorate.Color(Colors.gray, art, True))

def nice_output(output):
    message = []
    def calc_padding(key):
        return len(max([str(x.get(key)) for x in output.values()], key=len)) + 10
    def head_lines(sizes, lefts="+", middles="+", rights="+", fill="-"):
        messagex = lefts
        iter = 0
        for size in sizes:
            messagex += f"{fill * size}{fill}"
            if iter < len(sizes) - 1:
                messagex += middles
            else:
                messagex += rights
            iter += 1
        message.append(messagex)
    paddings = [calc_padding(key) for key in output.get(list(output.keys())[0])]
    titles = list(output.get(list(output.keys())[0]).keys())
    head_lines(paddings, "╭", "┬", "╮", "─")
    title_bar = "".join(f"│ {title.title()}{' ' * (paddings[titles.index(title)] - len(title))}" for title in titles) + "│"
    message.append(title_bar)
    head_lines(paddings, "├", "┼", "┤", "─")
    for port in list(output.keys()):
        x = 0
        line = ""
        for value in list(output.get(port).values()):
            line += f"│ {value}{' ' * (paddings[x] - len(str(value)))}" if x < len(titles) - 1 else f"│ {value}{' ' * (paddings[x] - len(str(value)))}│"
            x += 1
        message.append(line)
    head_lines(paddings, "╰", "┴", "╯", "─")

    print("\n".join(message))