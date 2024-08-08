customers=[(5,2),(5,4),(10,3),(20,1)]   



def average(customers):
    current_time=0
    total=0
    
   
    for arrival_time, time_required in customers:
        if current_time<arrival_time:
            current_time=arrival_time
        
        waiting_time=(current_time+time_required)-arrival_time
        total=total+waiting_time
       
        current_time=current_time+time_required
    return total/len(customers)


    
print("the average waiting time is : ",average(customers))
'''
commented output
the average waiting time is :  3.25

'''