#########################
# Author: Zouber Ismail
# Assignment 3 
# Date july 11 2022
#########################

    
    
def get_number_purchases(filename):
  
    # opening a text file
    file1 = open(filename, "r")
  
    # setting flag and index to 0
    
    purchase_num = ""
  
    # Loop through the file line by line
    for line in file1:  
        line_vals = line.split()
        purchase_num = line_vals[1]
          
# checking condition for string found or not
    
    file1.close() 
    
    return int(purchase_num.strip('#'))
  
    # closing text file    
    
    
def get_total_purchases(filename):
    string1 = 'Total Cost'
    total = 0
  
    # opening a text file
    file1 = open(filename, "r")
  
   
    
    
  
    # Loop through the file line by line
    for line in file1:  
        
        
    # checking string is present in line or not
        if string1 in line:
            order_total_cost = line.split()
            total += int(order_total_cost[len(order_total_cost)-1])
            
    file1.close() 
    return total 

def get_average_purchases(filename):
    number_purchases = get_number_purchases(filename)
    total = get_total_purchases(filename)
    
    return float(total/number_purchases)

def get_number_customer_purchases(filename, customer):
    string1 = customer
    count = 0
  
    # opening a text file
    file1 = open(filename, "r")
  
    
  
    # Loop through the file line by line
    for line in file1:  
        
        
    # checking string is present in line or not
        if string1 in line:
            count += 1
          
# checking condition for string found or not
    if count == 0: 
        print("No orders") 
    
    file1.close() 
    return count
        
def get_total_customer_purchases(filename, customer):

    count = 0
  
    # opening a text file
    file1 = open(filename, "r")
    lines = file1.readlines()
    

  
    # Loop through the file line by line
    x = 0
    is_end = False
    num_purchases = get_total_purchases(filename)
    while is_end == False:
        if x > len(lines)-1:
            is_end = True
            break
            
        line = lines[x].split()
        cust_name = line[len(line)-1]
        
        
        if cust_name == customer:
            total_line = lines[x+5].split()
            count +=  int(total_line[len(total_line)-1])
            
        x += 6
        
             
    if count == 0: 
        print("No orders") 
    
    file1.close() 
    return count
    
def get_average_customer_purchases(filename, customer):
    total = get_total_customer_purchases(filename, customer)
    num = get_num_customer_purchases(filename, customer)
    return float(total/num)

def get_most_popular_product(filename):
    desktop = 'Desktop'
    laptop = 'Laptop'
    tablet = 'Tablet'
    toaster = 'Toaster'
    desk_count = 0
    lap_count = 0
    tab_count = 0
    toast_count = 0
  
    
    file1 = open(filename, "r")
  
   
    for line in file1:  
       
        if desktop in line:
            line_vals = line.split()
            desk_count += int(line_vals[len(line_vals)-1])
        
        if laptop in line:
            line_vals = line.split()
            lap_count += int(line_vals[len(line_vals)-1])
            
        if tablet in line:
            line_vals = line.split()
            tab_count += int(line_vals[len(line_vals)-1])
            
        if toaster in line:
            line_vals = line.split()
            toast_count += int(line_vals[len(line_vals)-1])
        
    file1.close() 
    
    highest = max(max(desk_count,lap_count),max(tab_count, toast_count))
    
    if highest == desk_count:
        return desktop
    
    if highest == lap_count:
        return laptop
    
    if highest == tab_count:
        return tablet
    
    return toaster



if __name__ == "__main__":
    filename = "test.txt"
    customer = "John"
    num = get_total_customer_purchases(filename, customer)
    print(num)
        
    