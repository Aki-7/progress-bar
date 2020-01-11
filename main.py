#! python3
import sys, shutil

PREFIX = "#P"
PREFIX_LEN = 2
i = 0
n = 0
line = ""
is_progress_log = False

def parse_progress_log():
    global line, i , n, is_progress_log
    if not line.startswith(PREFIX):
        is_progress_log = False
        return
    try:
        body = line[PREFIX_LEN:]
        if (body.strip() == "exit"):
            exit()
        i_t, n_t = body.split("/")
        i = int(i_t); n = int(n_t)
        is_progress_log = True
    except ValueError:
        is_progress_log = False


def readline():
    global line
    line = sys.stdin.readline()

def clear_line():
    sys.stdout.write("\033[2K\033[G")

def write_progress_bar():
    global i , n
    ratio = 1 if n <= 0 or n <= i else float(i)/n
    columns = shutil.get_terminal_size().columns
    percentage_str = "{:.1f}%".format(ratio*100)
    max_arrow_len = columns - len(percentage_str) - 2
    arrow_len = int(max_arrow_len * ratio - 1)
    out = "["
    for k in range(max_arrow_len):
        if k < arrow_len:
            out += "-"
        elif k == arrow_len:
            out += ">"
        else:
            out += " "
    else:
        out += "]"
        out += percentage_str
    sys.stdout.write(out)

def output():
    clear_line()
    if not is_progress_log:
        sys.stdout.write(line)
    write_progress_bar()

if __name__ == "__main__":
    while True:
        readline()
        parse_progress_log()
        output()
        sys.stdout.flush()
