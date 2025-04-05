import yaml
def write_txt_file(file_path,lines,mode="a"):

    with open(file_path,mode=mode) as file_obj:
        for line in lines:
            file_obj.write(line)
        return file_obj


def read_yaml_file(file_path):
      with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
        return data

#######
print("hello GIT")
"HW play with GIT, see the changes, sign up for GIT HUb"
"3-30/2025 no class"
"4/03/2025 - 7 pm"
"finish om 24th approximately last day of tools"
