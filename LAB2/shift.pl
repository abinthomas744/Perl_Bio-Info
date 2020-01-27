#!/usr/bin/perl 
  
# Shift 

@array1 = ("Thomas", "Biomedical", "Abin"); 
print "Original Array: @array1\n"; 
$shifted_element = shift(@array1); 
@array1[3] = $shifted_element; 
print "Updated Array: @array1";