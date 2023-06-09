from main import water

############################## water temperature ##########################

check_1=True

if check_1:
    print(water(Temperature=62))

############################## water pressure ####################################

check_2=True

if check_2:
    print(water(Pressure=303))

############################# water temp x ###################################3

check_3=True

if check_3:
    print(water(Temperature=66,Enthalpy=500))

############################## pressure enthalpy x ###########################

check_4=True

if check_4:
    print(water(Pressure=500,Enthalpy=670))

#############################3 temperature entropy #############################3

check_5=True

if check_5:
    print(water(Temperature=66,Entropy=5))

#############################3 pressure entropy #############################3

check_5=True

if check_5:
        print(water(Pressure=1000,Entropy=5))
