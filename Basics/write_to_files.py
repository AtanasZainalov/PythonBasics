flavors_rel_path = "./data/flavors.txt"
def write_text_file(file_path,lines):
    with open(file_path, 'a') as file_obj:
        for line in lines:
            file_obj.write(line)
        return file_obj

# option 2 with loop

new_flawors =["\nbanana","\npineapple","\noreo"]
write_text_file(flavors_rel_path,new_flawors)

students_rel_path = "./data/students.txt"
new_students = ["Busra","\nRustam","\nNatalia"]
write_text_file(students_rel_path,new_students)

