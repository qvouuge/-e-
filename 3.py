files_data = []

for i in range(1, 4):
    file_name = f"{i}.txt"
    with open(file_name, encoding='utf-8') as f:
        lines = f.readlines()
        files_data.append((file_name, len(lines), lines))

files_data.sort(key=lambda x: x[1])

with open('result.txt', 'w', encoding='utf-8') as result_file:
    for file_name, line_count, lines in files_data:
        result_file.write(f"{file_name}\n")
        result_file.write(f"{line_count}\n")
        result_file.writelines(lines)
        result_file.write('\n')