def read_text_file(file_path):
    print("3. Reading the file bu creating lines")
    try:
        with open(file_path) as file_obj:
            lines= file_obj.readlines()
    except FileNotFoundError as err:
        print(err)
    return lines


file_rel_path = "data/flavors.txt"