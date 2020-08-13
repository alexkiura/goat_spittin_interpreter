import sys
import traceback
from itertools import count


def run_commands(line_num):
    if line_num == 1:
        print("Welcome to Goat spittin interpreter. Where goats spit")
    source = input(f"[{line_num}]🎤 🐐: ")
    try:
        if "exit" in result :
            print("Exiting Goat interpreter")
            return source
        exec(source, {})

    except Exception:
        print("Exception")
        print("-"*60)
        traceback.print_exc(file=sys.stdout)
        print("-"*60)

    except SystemExit:
        print("Exiting Goat interpreter")
        return


if __name__ == "__main__":
    for line in count(1):
        result = run_commands(line_num=line)
        if result and "exit" in result:
            break
