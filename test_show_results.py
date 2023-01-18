import json
import const
time_sum_gen = 0
time_sum_spik = 0
time_sum_pm = 0
time_sum_ng= 0
total_time = 0
mem_sum = 0
with open(r'./test_data/statistics.txt', 'r') as fp:
    test_cases = json.load(fp)
#max_size = len(test_cases[len(test_cases)-1][0][0])
max_size = const.input_size_max
test_size = const.test_size

for j in range (1,max_size+1):
    for i in range(len(test_cases)):
        if (len(test_cases[i][0][0]) == j):
            time_sum_gen += float(test_cases[i][1])
            time_sum_spik += float(test_cases[i][2])
            time_sum_pm += float(test_cases[i][3])
            time_sum_ng += float(test_cases[i][4])
            total_time += float(test_cases[i][5])
            mem_sum += float(test_cases[i][6])
            print(test_cases[i])
    print("Gen  time (s): ",time_sum_gen/test_size)        
    print("Spiking matrix time (s): ",time_sum_spik/test_size)
    print("Production matrix time (s): ", time_sum_pm/test_size)
    print("Net gain time (s): ",time_sum_ng/test_size)
    print("Total Time (s): ",total_time/test_size)
    print("Mem (bytes): ", mem_sum/test_size)
    time_sum_gen = 0
    time_sum_spik = 0
    time_sum_pm = 0
    time_sum_ng= 0
    total_time = 0
    mem_sum = 0