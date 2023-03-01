# ---------- constants ----------
msg_ = {0: "Enter an equation",
        1: "Do you even know what numbers are? Stay focused!",
        2: "Yes ... an interesting math operation. " \
            "You've slept through all classes, haven't you?",
        3: "Yeah... division by zero. Smart move...",
        4: "Do you want to store the result? (y / n):",
        5: "Do you want to continue calculations? (y / n):",
        6: " ... lazy",
        7: " ... very lazy",
        8: " ... very, very lazy",
        9: "You are",
        10: "Are you sure? It is only one digit! (y / n)",
        11: "Don't be silly! It's just one number! Add to the memory? (y / n)",
        12: "Last chance! Do you really want to embarrass yourself? (y / n)"}


operations = ["+", "-", "*", "/"]
memory = 0.0


# ---------- helpers ----------


def is_one_digit(value):
    return value.is_integer() and -10 < value < 10


def check(x, y, oper):
    msg = ""
    if is_one_digit(x) and is_one_digit(y):
        msg += msg_[6]
    if (x == 1 or y == 1) and oper == "*":
        msg += msg_[7]
    if (x == 0 or y == 0) and oper in ["*", "+", "-"]:
        msg += msg_[8]
    if msg:
        msg = msg_[9] + msg
        print(msg)


def recive_equation():
    calc = input(msg_[0] + "\n")
    x, oper, y = calc.split()

    x = memory if x == "M" else float(x)
    y = memory if y == "M" else float(y)

    if oper not in operations:
        raise TypeError

    return [x, oper, y]


def calculation(x, oper, y):
    if oper == "+":
        res = x + y
    elif oper == "-":
        res = x - y
    elif oper == "*":
        res = x * y
    else:
        res = x / y

    return res


def recive_yes_no_answer(msg_index):
    answer = None
    while answer not in ["y", "n"]:
        answer = input(msg_[msg_index] + "\n")
    return answer


def do_save_res():
    answer = recive_yes_no_answer(4)
    if answer == "y":
        if is_one_digit(res):
            msg_index = 10
            answer = None
            while answer not in ["y", "n"] \
                    or msg_index <= 12 and answer == "y":
                answer = input(msg_[msg_index] + "\n")
                msg_index += 1
        if answer == "y":   
            return True
    return False


# ---------- script ----------


while True:
    res = 0
    try:
        x, oper, y = recive_equation()
        res = calculation(x, oper, y)
    except ValueError:
        print(msg_[1])
        continue
    except TypeError:
        print(msg_[2])
        continue
    except ZeroDivisionError:
        print(msg_[3])
        continue

    check(x, y, oper)
    print(res)

    if do_save_res():
        memory = res
    
    answer = recive_yes_no_answer(5)
    if answer == "n":
        break
