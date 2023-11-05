import os


def list_file_create(directory):
    dict_file = {}
    list_files = os.listdir(directory)
    for filename in list_files:
        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as f:
            file_contents = f.readlines()
        dict_file[filename] = len(file_contents)
    return dict_file


def file_res(directory):
    dict_file = list_file_create(directory)
    sorted_files = sorted(dict_file.items(), key=lambda item: item[1])
    
    with open('new_text_file.txt', 'w', encoding='utf-8') as output_file:
        for filename, length in sorted_files:
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as f:
                text_file = f.readlines()
            output_file.write(filename + '\n')
            output_file.write(str(length) + '\n')
            output_file.writelines(text_file)
            output_file.write('\n')

file_res('txt')