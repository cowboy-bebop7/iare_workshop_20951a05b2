n=850
n_four_weeks = 4 * n

fed_per = 0.11
state_per = 0.055
pen_per = 0.062
s = fed_per + state_per + pen_per

total_deduction = n_four_weeks * s

net =  n_four_weeks - total_deduction 
print(net)
