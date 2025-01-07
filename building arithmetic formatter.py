def arithmetic_arranger(problems, show_answers=False):
    #Check for too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    #Lists to store each line    
    first_line =[]
    second_line =[]
    dash_line = []
    answer_line = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."
        operand1, operator, operand2 = parts

        #Check operator validity
        if operator not in ('+' , '-'):
            return "Error: Operator must be '+' or '-'."
        #Check if operands are valid numbers
        if not (operand1.isdigit() and operand2.isdigit()):
            return "Error: Numbers must only contain digits."
        #Check operand size
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        #Perform formatting
        width = max(len(operand1) , len(operand2)) + 2
        first_line.append(operand1.rjust(width))
        second_line.append(operator+" "+operand2.rjust(width - 2))
        dash_line.append("-"*width)

        if show_answers:
            if operator == "+":
                answer = str(int(operand1) + int(operand2))
            elif operator == "-":
                answer = str(int(operand1) - int(operand2))
            answer_line.append(answer.rjust(width))

    #Join lines        
    arranged_problems = (
        "    ".join(first_line) + "\n" +
        "    ".join(second_line) + "\n" +
        "    ".join(dash_line)
    )
    if show_answers:
        arranged_problems += "\n" + "    ".join(answer_line)

    return arranged_problems

print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"], True)}')
print(f'\n{arithmetic_arranger(["1 + 2", "1 - 9380"], True)}')
print(f'\n{arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"], True)}')
print(f'\n{arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"], True)}')
print(f'\n{arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"], True)}')
print(f'\n{arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"], True)}')
print(f'\n{arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"], True)}')
print(f'\n{arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"], True)}')
print(f'\n{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')
print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')