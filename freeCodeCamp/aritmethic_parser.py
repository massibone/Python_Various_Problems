'''
data massimo 5 operazioni es 3001-2, 23+5 mi dà:
3001 -    23+
      2         5
-----      --
2999       28
'''
def arithmetic_arranger(problems, show_answers=False):
    # Error Handling for Too Many Problems
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""

    for problem in problems:
        # Parsing the problem string
        try:
            parts = problem.split()
            first_operand = parts[0]
            operator = parts[1]
            second_operand = parts[2]
        except ValueError:
            return "Error: Invalid problem format."

        # Error Handling for Operator and Digits
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not first_operand.isdigit() or not second_operand.isdigit():
            return 'Error: Numbers must only contain digits.'
        if len(first_operand) > 4 or len(second_operand) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # Determining the width of each problem
        max_width = max(len(first_operand), len(second_operand)) + 2

        # Formatting the first line (top operand)
        first_line += first_operand.rjust(max_width)
        
        # Formatting the second line (operator and bottom operand)
        second_line += operator + second_operand.rjust(max_width - 1)

        # Formatting the third line (dashes)
        third_line += "-" * max_width
        
        # Calculating and formatting the answer if requested
        if show_answers:
            if operator == '+':
                result = str(int(first_operand) + int(second_operand))
            else:
                result = str(int(first_operand) - int(second_operand))
            
            fourth_line += result.rjust(max_width)

        # Adding spacing between problems
        if problem != problems[-1]:
            first_line += "    "
            second_line += "    "
            third_line += "    "
            fourth_line += "    "
            
    # Constructing the final output string (Spostato fuori dal ciclo)
    if show_answers:
        return f"{first_line}\n{second_line}\n{third_line}\n{fourth_line}"
    else:
        return f"{first_line}\n{second_line}\n{third_line}"

