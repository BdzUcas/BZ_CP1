#BZ 1st Squared Nmbers
#create numbers list
nums = [3, 7, 12, 25, 30, 45, 50, 65, 70, 85, 90, 105, 110, 125, 130, 145, 150, 165, 170, 185, 190, 205, 210, 225, 230, 245, 250, 265, 270, 285]
#create a list of all the numbers in that list squared
squared_list = list(map(lambda num:num*num,nums))
#for every item in the list of squared numbers
for sqrd in squared_list:
    #Print the origanal number and the squared number
    print(f'Original: {nums[squared_list.index(sqrd)]} Squared: {sqrd}')