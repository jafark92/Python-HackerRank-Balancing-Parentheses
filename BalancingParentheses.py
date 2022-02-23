s = ")))()(()))"

num_of_opening_bracket = s.count("(")
num_of_closing_bracket = s.count(")")

print("Minium number of required parentheses: ", abs(num_of_closing_bracket - num_of_opening_bracket))
