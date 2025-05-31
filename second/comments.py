"""use docstrings (three commas) after every function explaining what it doe
__________________________________________________________________________________________________

PART-1
__________________________________________________________________________________________________

Q1) feet_to_meter 
-- converts length from feet --> meter
-- rounds to two decimal places
-- 1m is 3.28 feet
-- returns in meter

Q2) rocket_volume
-- takes radius, height_cone, height_cyl (in meters)
-- returns volume (Vcone = 1/3 pi*r2*h, Vcyl = pi*r2*h)
-- round to two decimal places

Q3) rocket_area
-- takes radius, height_cone, height_cyl (in meters)
-- returns surface area (check doc)
-- dont count shared circle face (-pi*r2)
-- total surface area Arocket=Acone+Acyl−2Acircle
-- round to two decimal places

Q4) rocket_mass
-- density = 1.225 kg/m3
-- calculate rocket mass by M = D*V
-- round to two decimal places

Q5) rocket_fuel
-- takes radius, height_cone, height_cyl, velocity_e, velocity_i, time
-- finds mfuel (see eq in doc)
-- use math.e for e value
-- consider the fuel required after (check doc)

Q6) calculate_cost
-- takes radius, height_cone, height_cyl, velocity_e, velocity_i, time, tax
-- cost of fuel $7.331/kg and cost of materials $4.5/m2
-- tax is 14.975%
-- round answer to two decimal places

__________________________________________________________________________________________________

PART-2
__________________________________________________________________________________________________

Q7) compute_storage_space
-- takes radius and height (in float)
-- returns the width, length and height of storage space (check doc for formula)
-- round to two decimal places

Q8) load_rocket
-- takes rockets initial weight, radius, cylinders height

-- call compute_storage_space function to compute dimenstions and volume (multiply l*b*h)
-- total weight of the items should not exceed 4% of rockets total weight 
-- boxes should not occupy more than 60% of storage space volume
-- function will verify if the two conditions are satisfied or return  “No moreitems can be added" 

-- the function will continously ask for user to entire weight, height, width, depth of object until it fills up the given space
-- it should print "Item could not be added...  please try again..." --> .  If the weight of the item is too low or too high(less than or equal to10 kg,greater than or equal to512 kg, or would make thetotal weight 4% or more of the initial weight of the rocket)
-- it should print “Item could not be added" -->  if adding the new item makes us exceed 60% of the storage’s volume, or if thevolume of the box is less than 0.5m3)

-- it should print “No more items can be added" --> total weight of the items is greater than or equal to (10 kg less than 4% of the rocket’sweight) or if the total volume of the boxes is greater than (0.5m3less than 60% of therocket’s volume)
-- if the user types "Done" --> stop asking for more 
-- return the new weight rounded to 2 decimal places

Q9) projectile_sim
-- takes simulation time, interval, inital velocity, andn angle (in radians)
-- returns none
-- see formula from doc and calculate y
-- it calculates height at each interval until the max sim time (or until rocket lands, which occurs when height is less than/equal to zero) 
-- code given (edit it)

Q10) rocket_main
-- inputs none returns none
-- ask the user for the radius, cone height, and cylinder height of the rocket (all infeet)
-- ask the user for the exhaust velocity, initial velocity, angle of launch, and length of the up-coming trip (inm/s,m/s, radians, and seconds respectively).  All these are float number
-- ask the user whether to factor in tax
-- calculate the cost of the trip and display it
-- determine the initial weight of the rocket(we ignore the weight of the fuel for simplicity)
-- load the rocket
-- ask the user for the simulation time and simulation interval for the projectile simulation(both in seconds)
-- launch the projectile simulation(we use the “initial” velocity for this part

-- the user should enter 1=yes 0=no


"""