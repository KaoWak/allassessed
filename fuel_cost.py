def fuel_cost(distance_miles):
# Constants
 MPG = 50  # Miles per gallon
 LITERS_PER_GALLON = 4.5
 PRICE_PER_LITER = 1.49  

 gallons_needed = distance_miles / MPG
    
 liters_needed = gallons_needed * LITERS_PER_GALLON 
 total_cost = liters_needed * PRICE_PER_LITER
    
 return total_cost

distance = float(input("enter distance in miles"))
cost = fuel_cost(distance)
print(f" total cost for {distance} miles is £{cost}")
