import phys_lab_calc as phys

my_data = open("data.txt").readlines()  # input file with data

my_data = phys.get_data(my_data)
my_dict = phys.get_dict_data(my_data)  # where data is list of strings

phys.print_dict_data(my_dict)

avrg = phys.average(my_data)

print('avrg = ', avrg)

disp = phys.dispersion(my_data)
print('dispersion = ', disp)

standard_deviation = phys.standard_deviation(my_data)
print('standard_deviation = ', standard_deviation)

rand_error = phys.random_error(my_data, 1.0553)  # Student's t-test as second argument
print('random_error = ', rand_error)

abs_error = phys.absolute_error(0.005, 0, rand_error)
print('abs_error = ', abs_error)
