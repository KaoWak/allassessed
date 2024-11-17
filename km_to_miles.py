def km_to_miles(kilometers):
    # complete function implementation here...

    conversion = 0.62 
    miles = kilometers * conversion
    return miles
 

kilometers = 120
miles = km_to_miles(kilometers)
print(f"{kilometers} kilometers is{miles} miles.")