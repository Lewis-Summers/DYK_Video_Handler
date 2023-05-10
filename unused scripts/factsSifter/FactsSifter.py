with open('/unused scripts/factsSifter/xtraFacts.txt', 'r', encoding="utf-8") as input_file:
    # Read all the lines into a list
    lines = input_file.readlines()

# Remove duplicates from the list
lines = list(set(lines))

# Open the output file for writing
for line in lines:
    if len(line) > 99:
        with open('output.txt', 'a', encoding="utf-8") as output_file:
            output_file.writelines(line)
    else:
        with open('input.txt', 'a', encoding="utf-8") as output_file:
            output_file.writelines(line)

# with open('output.txt', 'w', encoding="utf-8") as output_file:
#    output_file.writelines(lines)