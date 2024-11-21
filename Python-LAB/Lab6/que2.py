students = {'Tom','Jerry','Pikachu','Spidey','Doraemon','Chota Nheem','Nagraj','Baalveer','Motu','Patlu'}
plant_drive = {'Spidey','Motu','Patlu'}
millitry_exbi ={'Nagraj','Pikachu','Spidey'}
attended_class = {'Doraemon','Baalveer'}
print("Student who attend Both" ,plant_drive & millitry_exbi)
print("Student who attend only one event :",plant_drive ^ millitry_exbi)
print("Bunked classes :" ,students - (plant_drive | millitry_exbi | attended_class))