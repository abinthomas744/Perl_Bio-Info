#Unshift

#!/usr/bin/perl  
     
@array = ('Biomedical', 'Engineering');  
    
# Print the Inital array  
print "Original array: @array \n";  
    
# Prints the number of elements  
# returned by unshift  
print "No of elements returned by unshift: ",  
                   unshift(@array, 'Abin', 'Thomas');  
    
# Array after unshift operation  
print "\nUpdated array: @array"; 