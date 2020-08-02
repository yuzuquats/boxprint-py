from enum import Enum


# -, |, TL, TR, BL, BR
class BoxTypes(Enum):
    LIGHT = "\u2500\u2502\u250C\u2510\u2514\u2518"
    HEAVY = "\u2501\u2503\u250F\u2513\u2517\u251B"
    DOUBLE = "\u2550\u2551\u2554\u2557\u255A\u255D"
    ROUND = "\u2500\u2502\u256D\u256E\u2570\u256F"

   # TODO: Dashed boxes don't look good, should they even exist?
    LIGHT_DOUBLE_DASHED = "\u254C\u254E\u250C\u2510\u2514\u2518"
    HEAVY_DOUBLE_DASHED = "\u254D\u254F\u250F\u2513\u2517\u251B"
    LIGHT_TRIPLE_DASHED = "\u2504\u2506\u250C\u2510\u2514\u2518"
    HEAVY_TRIPLE_DASHED = "\u2505\u2507\u250F\u2513\u2517\u251B"
    LIGHT_QUADRUPLE_DASHED = "\u2508\u2506\u250C\u2510\u2514\u2518"
    HEAVY_QUADRUPLE_DASHED = "\u2509\u2507\u250F\u2513\u2517\u251B"


def next_newline_index(string, start, end):
    for i in range(start, end):
        # TODO: handle other kinds of newlines?
        if string[i] == '\n':
            return i
    return -1


def bprint(text="", width=80, box_type=BoxTypes.ROUND, print_func=print):
    line = [box_type.value[0]] * width
    line[0] = box_type.value[2]
    line[-1] = box_type.value[3]
    print_func("".join(line))

    text_per_line = width - 4
    strlen = len(text)
    # TODO: handle other kinds of newlines?
    if text[-1] == "\n":
        strlen -= 1

    end = 0
    buf = ""
    while end < strlen:
        previous_end = end
        end += text_per_line
        end = min(strlen, end)
        newline_index = next_newline_index(text, previous_end, end)
        # TODO: rewrite this portion
        if newline_index != -1:
            end = newline_index - 1
        if end == -1:
            buf = ""
        else:
            buf = text[previous_end:end]
        if newline_index != -1:
            end = newline_index + 1

        buf = buf.ljust(text_per_line, " ")
        print_func(f"{box_type.value[1]} {buf} {box_type.value[1]}", )

    line[0] = box_type.value[4]
    line[-1] = box_type.value[5]
    print_func("".join(line))
