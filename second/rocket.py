# 1. Please complete the following:
#   Your First name and Last Name: Saif Shaikh
#   Your Student ID: 261202410


# 2. Write your program here:




import math

"""------- PART-1 --------"""
def feet_to_meter(length):
    """
    converts the input given by user from feet to meters
    1m = 3.28feet
     
    Examples:
    1) feet_to_meter(5.0) returns 1.52
    2) feet_to_meter(10.0) returns 3.05
    3) feet_to_meter(5.0) returns 3.81
    """

    length_m = (1/3.28)*length #gives length in meter
    
    return round(length_m, 2)
   

def rocket_volume(radius, height_cone, height_cyl):
    """
    finds the volume of cone and cylinder of the rocket 
    separately using different formulas and adds them to 
    give the total rocket volume
    
    Examples
    1) rocket_volume(2.0,7.0,3.0) returns 67.02
    2) rocket_volume(5.0,10.0,1.0) returns 340.34
    3) rocket_volume(1.0,1.0,1.0) returns 4.19
    """
    
    #uses the formula to find volume of cone (1/3(pi*r^2*h)
    vol_cone = math.pi*(radius**2)*height_cone/3 
    
    #uses the formula to find volume of cylinder (pi*r^2*h)
    vol_cyl = math.pi*(radius**2)*height_cyl
    
    vol_rocket = vol_cone + vol_cyl #adds both to give total volume

    return round(vol_rocket, 2)

    
def rocket_area(radius, height_cone, height_cyl):
    """
    finds the total surface area by first individually
    measuiring the surface areas of cone and cylinder and 
    then adding them. at the end the common areas are subtracted
    (as we just need the exterior surface area)
    
    Examples:
    1) rocket_area(13.4, 17.6, 3.9) returns 1823.68
    2) rocket_area(5.0,5.0,5.0) returns 346.69
    3) rocket_area(7.0,10.0,12.0) returns 950.16
    """
    #gives area of cone with the formula (pi*r(r+sqrt(h^2+r^2)))
    area_cone=math.pi*radius*(radius+math.sqrt((height_cone**2)+(radius**2)))
    
    #gives area of cylinder witht he formula (2*pi*r(h+r))
    area_cyl = 2*math.pi*radius*(height_cyl+radius)
    
    #area of the circles where the cone and cylinder overlap
    area_circle = math.pi*radius**2
    
    #gives total area removing the overlapping circle region
    area_rocket = area_cone+area_cyl-2*area_circle
    
    return round(area_rocket, 2)


def rocket_mass(radius, height_cone, height_cyl):
    """
    using the rocket_volume function which calculates the 
    volume of the rocket this function uses the volume and 
    multiples it by the density (1.25kg/m3) to given the 
    mass of the rocket
    
    Examples:
    1) rocket_mass(2.0, 7.0, 3.0) returns 82.1
    1) rocket_mass(100.0,200.0,300.0) returns 14110987.0
    1) rocket_mass(3.0,3.0,5.0) returns 207.82
    """
    
    #calls the rocket_volume function for the total rocket volume
    volume = rocket_volume(radius, height_cone, height_cyl)

    density = 1.225 #kg/m3
    mass_rocket = density*volume # formula density = mass/vol
    
    return round(mass_rocket,2)

def rocket_fuel(radius,height_cone, height_cyl,velocity_e,velocity_i,time):
    """
    takes the radius, height of cone, hegiht of cylinder,
    exhaust and initial velocities along with time time to 
    calculate the mass of fuel required in kgs. it also calls 
    the rocket_mass function to findt he mass of the rocket
    
    Examples:
    1) rocket_fuel(2.0, 3.0, 4.0, 250.0, 1000.0, 1.0) returns 4893.45
    2) rocket_fuel(20.0, 10.0, 3.5, 500.0, 200.0, 23.0) returns 22837.55
    3) rocket_fuel(1.0, 5.0, 1.2, 1000.0, 2000.0, 1.0) returns 838.54
    """
    
    #calls the rocket_mass functions to obtain the mass of rocket
    rocketmass = rocket_mass(radius, height_cone, height_cyl)
    
    #rocket burns 768 kg/s if its mass is less than 80 000 kg
    if rocketmass<80000:
        time_mass = time*768 #kg/s
        
    #rocket burns 1314 kg/s if its mass is less than/equal to 35000 kg
    elif rocketmass<= 350000:
        time_mass = time*1314 #kg/s
    
    #rocket burns 1542 kg/s otherwise
    else:
        time_mass = time*1542 #kg/s
        
    #uses the formula to find mass of fuel (m_rocket*(e^(vi/ve)-1))
    fuel_mass=time_mass+(rocketmass*((math.e**(velocity_i/velocity_e))-1))
    
    return round(fuel_mass,2)



def calculate_cost(radius, height_cone, height_cyl, velocity_e,\
    velocity_i, time, tax):
    """
    it uses the rocket_fuel function to obtain the mass of
    the fuel and calculates the cost of the fuel $7.331/kg,
    cost of materal (area from rocket_area function) is $4.5/kg
    along with the tax (if required) of 14.975% as it in Montreal
    
    Examples:
    1) calculate_cost(2.0, 3.0, 4.0, 250.0, 1000.0, 1.0, True)
    returns 41688.31
    2) calculate_cost(5.0, 1.0, 6.5, 100.0, 1100.0, 1.23, False)
    returns 288583087.69
    3) calculate_cost(3.25, 1.5, 6.0, 500.0, 900.0, 0.5, True)
    returns 15477.24
    """
    
    #calls the fuel_mass function for the mass of fuel
    fuel_mass = rocket_fuel(radius, height_cone, height_cyl,\
        velocity_e, velocity_i, time)
    
    #calls the area_rocket function for the total surface area of rocket
    area_rocket = rocket_area(radius, height_cone, height_cyl)
    
    #calculates the cost of material
    cost_material = area_rocket*4.5 #$4.5/m2
    
    #calculates the cost of fuel
    cost_fuel = fuel_mass*7.331 #$7.331/kg
    
    #gives the total cost by adding
    combined_cost = cost_material + cost_fuel
    
    #asks the user if tax needs to be included
    if tax==1:
        combined_cost += combined_cost*0.14975 #14.975% tax is added
    
    return round(combined_cost,2)


"""------ PART-2 --------"""


def compute_storage_space(radius, height_cyl):
    """
    this function takes the radius and height(cylinder portion)
    of the rocket as positive float and computes the 
    width, length and height of the storage space
    
    Examples:
    1) compute_storage_space(5.0, 10.0) returns (7.07, 7.07, 5.0)
    2) compute_storage_space(7.5, 11.0) returns (10.61, 10.61, 5.5)
    3) compute_storage_space(12.0,15.0) returns (16.97, 16.97, 7.5)
    """
    #computes the length, width and height using the formulas
    
    l_rocket = radius*math.sqrt(2) #length = radius*sqrt(2)
    w_rocket = radius*math.sqrt(2) #width = radius*sqrt(2)
    h_rocket = height_cyl/2 #height = height_cyl/2
    
    return round(l_rocket,2), round(w_rocket,2), round(h_rocket,2)


def load_rocket(rocket_mass, radius, height_cyl):
    """
    This function is used to measure the final mass weight of
    the rocket including all the other materials added to the 
    storage container. It also has a condition that the storage 
    cannot have more than 4% of the total weight and the volume
    cannot be more than 60% of storage volume.
    """
    
    r_length, r_width, r_height = compute_storage_space(radius, height_cyl)
    rocket_vol = r_length * r_height * r_width
    
    weight_constraint = 0.04 * rocket_mass  # Maximum weight
    volume_constraint = 0.60 * rocket_vol  # Maximum volume
    
    min_weight, max_weight, min_vol = 10, 512, 0.5  # Constraints
    vol_filled, weight_filled = 0, 0
    
    if weight_constraint >= min_weight and volume_constraint >= min_vol:
        ask_weight = ""
        while (ask_weight != "Done" and 
               volume_constraint - vol_filled >= min_vol and 
               weight_constraint - weight_filled >= min_weight):
            ask_weight = input("Please enter the weight of the next item (type 'Done' when you are done filling the rocket): ")
            
            if ask_weight != "Done":
                ask_weight = float(ask_weight)
                ask_width = float(input("Enter item width: "))
                ask_length = float(input("Enter item length: "))
                ask_height = float(input("Enter item height: "))
                
                ask_vol = ask_width * ask_height * ask_length
                
                if (ask_weight > max_weight or ask_weight < min_weight or
                    ask_vol < min_vol or
                    vol_filled + ask_vol > volume_constraint or
                    weight_filled + ask_weight > weight_constraint):
                    print('Item could not be added... please try again...')
                else:
                    vol_filled += ask_vol
                    weight_filled += ask_weight
        else:
            print('No more items could be added')
    else:
        print('No more items can be added')
    
    return round(rocket_mass + weight_filled, 2)


def projectile_sim(simulation_time, interval, v0, angle):
    """
    This function simulates the projectile motion by calculating 
    the height of the projectile at each interval.
    
    Parameters:
    simulation_time (float): Total simulation time in seconds.
    interval (float): Time interval for height calculation.
    v0 (float): Initial velocity in m/s.
    angle (float): Launch angle in radians.
    
    Example:
    1) projectile_sim(10, 3, 100.0, 1.55) prints
    0.0
    255.79
    423.29
    502.5
    
    2) projectile_sim(5, 1, 500.0, 3) prints
    0.0
    65.66
    121.5
    167.54
    203.76
    230.18
    
    3) projectile_sim(7, 4, 100.0, 2) prints
    0.0
    285.24
    
    """
    a = 9.81  # gravity in m/s^2
    
    # Converted while loop to for loop
    for time in range(0, int(simulation_time / interval) + 1):
        t = time * interval  # Actual time
        height = -0.5 * a * (t ** 2) + v0 * math.sin(angle) * t

        if height > 0 or t == 0:
            print(round(height, 2))

    
def rocket_main(inputs=None):
    """
    this function combines all the things together to give
    a good user interface and in an organized manner
    """
    
    print("Welcome to the Rocket Simulation!")
    # Ask the user for input
    radius_ft = float(input("Enter the rocket radius in feet: "))
    height_cone_ft = float(input("Enter the rocket cone height in feet: "))
    height_cyl_ft = float(input("Enter the rocket cylinder\
 height in feet: "))
    velocity_e = float(input("Enter the exhaust velocity for\
 the upcoming trip: "))
    velocity_i = float(input("Enter the initial velocity for\
 the upcoming trip: "))
    angle = float(input("Enter the angle of launch for the \
 upcoming trip: "))
    time = float(input("Enter the length of the upcoming trip: "))
    tax = int(input("Would you like to factor in tax? \
 Enter 1 for yes, 0 for no: "))

    # Convert inputs to meters
    radius = feet_to_meter(radius_ft)
    height_cone = feet_to_meter(height_cone_ft)
    height_cyl = feet_to_meter(height_cyl_ft)

    # Calculate and display the cost
    cost = calculate_cost(radius, height_cone, height_cyl, \
        velocity_e, velocity_i, time, tax)
    
    print("This trip will cost $", cost)
    print("Now loadng the rocket:")
    
    r_mass = rocket_mass(radius, height_cone, height_cyl)
    y = load_rocket(r_mass, radius, height_cyl)
    
    print("The rocket and its equipement will weigh ", y, "kg")
    
    simulation_time = float(input("Enter the simulation time: "))
    interval = float(input("Enter the simulation interval: "))
    
    projectile_sim(simulation_time, interval, velocity_i, angle)

#if __name__ == "__main__":
 #   rocket_main()
 
def load_rocket(initial_weight, radius, height_cyl):

    # First we compute the volume of the storage space.
    w, l, h  = compute_storage_space(radius, height_cyl)
    storage_space  = w * l  * h

    # We setup the conditions:
    max_total_weight  = 0.05 * float(initial_weight)
    max_total_volume  = 0.4 * storage_space
    MIN_BOX_WEIGHT = 20
    MIN_BOX_VOLUME = 0.125
    MAX_BOX_WEIGHT = 500

    total_weight  = 0
    total_volume = 0 

    # We setup the flow control 
    done  = False
    while done == False:
                    
        # Now we input the item
        box_weight = input('Please enter the weight of ' \
                           'the next (type "Done" when you ' \
                           'are done filling the rocket):')
                    
        if box_weight == "Done":
            done = True
            return round((total_weight + initial_weight), 2)
        else:
            box_weight = float(box_weight)
                    
            box_width = float(input("Enter item width:"))
            box_length = float(input("Enter item length:"))         
            box_height = float(input("Enter item height:"))     
                    
            # Compute the volume of the item
            box_volume = float(box_width * box_length * box_height)
                        
            # Now we evaluate the conditions
            if max_total_weight - total_weight < MIN_BOX_WEIGHT \
                or max_total_volume - total_volume < MIN_BOX_VOLUME:
                done = True
                print("No more items can be added")
                    
            elif (total_weight + box_weight) > max_total_weight \
                or (total_volume + box_volume) > max_total_volume \
                or box_weight < float(MIN_BOX_WEIGHT) \
                or box_weight > float(MAX_BOX_WEIGHT) \
                or box_volume < MIN_BOX_VOLUME: 
                print("Item could not be added... please try again...")
            else:
                total_volume += box_volume
                total_weight += box_weight 
                        
    return round(total_weight, 2)



#First we define the function
def projectile_sim(simulation_time, interval, initial_velocity, angle):

    #Then we create a for loop to stay in the interval time
    for i in range(0, simulation_time + 1, interval):
        h = ((-1/2) * 9.8 * i**2) + (initial_velocity * math.sin(angle) * i )

    #We make sure that the simulation stops when the rocket touches the ground
        if not( i | 0 and h < 0) :
            print(round(h, 2))

    #Quon 10 rocket_main():

"""

```

(None) -| None

Uses all of the other functions to create, load and launch the rocket

| | | rocket_main()
| | | Welcome to the Rocket Simulation!
| | | Enter the rocket radius in feet:50
| | | Enter the rocket cone height in feet:100
| | | Enter the cylinder height in feet:200
| | | Enter the exhaust velocity for the upcoming trip:700
| | | Enter the initial velocity for the upcoming trip300
| | | Enter the angle of launch of the upcoming trip0.8
| | | Enter the initial length of the upcoming trip1000
| | | Would you like to factor in tax? 1 for yes, 0 for no:1
| | | This trip will cost $9826238.52
| | | Now loading the rocket:
| | | Please enter the weight of the next (type "Done" when you are done filling the rocket):100
| | | Enter item width:5
| | | Enter item length:5
| | | Enter item height:5
| | | Please enter the weight of the next (type "Done" when you are done filling the rocket):Done
| | | The rocket and its equipment will weigh 63690.19 kg
| | | Enter the simulation total time:8
| | | Enter the simulation interval:2
| | | Now simulating the ro trajectory:
| | | 0.0
| | | 410.79
| | | 782.35
| | | 1114.66
| | | 1407.73

```
"""
def rocket_main():
    print('Welcome to the Rocket Simulation!')
    #First we get the lengths in feet
    radius = float(input("Enter the rocket radius in feet:"))
    height_cone = float(input("Enter the rocket cone height in feet:"))
    height_cyl = float(input("Enter the cylinder height in feet:"))

    #Then we convert
    radius = feet_to_meter(radius)
    height_cone = feet_to_meter(height_cone)
    height_cyl = feet_to_meter(height_cyl)

    velocity_e = float(input('Enter the exhaust '\
                        'velocity for the upcoming trip:'))
    velocity_i = float(input("Enter the initial velocity for the upcoming trip"))
    angle = float(input("Enter the angle of launch of the upcoming trip"))
    length = float(input("Enter the initial length of the upcoming trip"))
    if input('Would you like to factor in tax? 1 for yes, 0 for no:') == 1:
        tax = False
    else:
        tax  = True

    #Then we calculate the cost : 
    cost = calculate_cost(radius, height_cone,\
            height_cyl, velocity_e, velocity_i, length, tax)
    print('This trip will cost $' + str(cost))

    #Now we calculate the initial weight :
    initial_weight = rocket_mass(radius, height_cone, height_cyl)

    #Now we load the rocket 
    print('Now loading the rocket:')
    print('The rocket and its equipment will weigh',\
        load_rocket(initial_weight, radius, height_cyl),\
        'kg')

    #Now we simulate the launch :
    simulation_time = int((input('Enter the simulation total time:')))
    interval = int((input('Enter the simulation interval:')))
    print('Now simulating the ret trajectory:')
    projectile_sim(simulation_time, interval, velocity_i, angle)

"""______________________________________________________________________"""




