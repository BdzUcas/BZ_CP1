#BZ 1st Mapping Notes
#If i do mapping, am i a cartographer?
nums = [5,645,39,888,-7,6547,-90]
double_nums = []
#for num in nums:
#    double_nums.append(double(num))

double_nums = map(lambda num: num*2,nums)
for i in double_nums:
    print(i)