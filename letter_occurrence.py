def letter_occurrence(input_string):
     # complete function implementation...
    # return count
   
    count = 0

    for l in input_string:
       
        if l == 'a' or l == 'A':

            count += 1

    return count

# Example usage with the word "amazing"
#result = letter_occurrence("amazing")
#print(result)

#result = letter_occurrence("“Always aim ambitiously")
#print(result)








