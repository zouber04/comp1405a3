#########################
# Author: Zouber Ismail
# Assignment 3 
# Date july 11 2022
#########################

    
    
get_number_purchases(filename):
    string1 = 'Purchase #'
    count = 0
  
    # opening a text file
    file1 = open(filename, "r")
  
    # setting flag and index to 0
    
    purchase_num = 0
  
    # Loop through the file line by line
    for line in file1:  
        purchase_num+= 1
        string1 += " "+str(purchase_num)
    # checking string is present in line or not
        if string1 in line:
            count += 1
          
# checking condition for string found or not
    if count == 0: 
    print("No orders") 
    
    filename.close() 
    return count
  
    # closing text file    
    
    
get_total_purchases(filename):
    string1 = 'Total Cost'
    total = 0
  
    # opening a text file
    file1 = open(filename, "r")
  
   
    
    
  
    # Loop through the file line by line
    for line in file1:  
        
        
    # checking string is present in line or not
        if string1 in line:
            order_total_cost = line.split()
            total += int(order_total_cost[2])
            
    filename.close() 
    return total 