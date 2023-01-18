import json
time_sum_gen = 0
time_sum_spik = 0
time_sum_pm = 0
time_sum_ng= 0
total_time = 0
mem_sum = 0
with open(r'./single_instance/statistics.txt', 'r') as fp:
    test_cases = json.load(fp)

time_sum_gen += float(test_cases[0][1])
time_sum_spik += float(test_cases[0][2])
time_sum_pm += float(test_cases[0][3])
time_sum_ng += float(test_cases[0][4])
total_time += float(test_cases[0][5])
mem_sum += float(test_cases[0][6])

print(test_cases[0])
print("Gen  time (s): ",time_sum_gen)        
print("Spiking matrix time (s): ",time_sum_spik)
print("Production matrix time (s): ", time_sum_pm)
print("Net gain time (s): ",time_sum_ng)
print("Total Time (s): ",total_time)
print("Mem (bytes): ", mem_sum)
time_sum_gen = 0
time_sum_spik = 0
time_sum_pm = 0
time_sum_ng= 0
total_time = 0
mem_sum = 0