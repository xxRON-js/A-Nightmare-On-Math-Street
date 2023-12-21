from pwn import *
import re

def adjust_operators(question: str) -> str:
    """Adjust the question to make addition and multiplication have the REVERSE order of operation"""
    question_adjusted = []
    during_plus_op = False

    for unit in question.split():
        if unit == "*":
            if during_plus_op:
                question_adjusted[-1] = f"{question_adjusted[-1]}) *"
                during_plus_op = False
            else:
                question_adjusted.append(unit)
            continue

        if unit == "+":
            # Check if the next unit contains "("
            if question[question.index(unit) + 1].startswith("("):
                question_adjusted.append(unit)
                continue

            if during_plus_op:
                question_adjusted[-1] = f"{question_adjusted[-1]} +"
            else:
                question_adjusted[-1] = f"({question_adjusted[-1]} +"
                during_plus_op = True
            continue

        question_adjusted.append(unit)

    if during_plus_op:
        question_adjusted[-1] += ")"

    question_adjusted_str = " ".join(question_adjusted)
    print(f"{question_adjusted_str=}")
    return question_adjusted_str

def solve_question():
    """Solve the question and send the answer"""
    question_str = conn.recvuntil("?", timeout=1).decode()
    print(f"{question_str=}")
    question = re.findall(r"\[\d+\]:\s+(.*?)\s+\=", question_str)[0]
    print(f"{question=}")
    question_adjusted = adjust_operators(question)
    answer = str(eval(question_adjusted))
    print(f"{answer=}")

    conn.sendline(answer)
    print("\n---\n")

    if "[500]" in question_str:
        print(conn.recvline_contains("HTB", timeout=1).decode())
        exit(0)

def main():
    global conn
    conn = remote('159.65.20.166', 31072)

    while 1:
        try:
            solve_question()
        except EOFError:
            print("EOFError...")
            break

if __name__ == "__main__":
    main()
