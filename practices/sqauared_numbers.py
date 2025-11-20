#BZ 1st Squared Nmbers
#create numbers list
nums = [3, 7, 12, 25, 30, 45, 50, 65, 70, 85, 90, 105, 110, 125, 130, 145, 150, 165, 170, 185, 190, 205, 210, 225, 230, 245, 250, 265, 270, 285]
#create a list of all the numbers in that list squared
squared_list = list(map(lambda num:num*num,nums))
#for every item in the list of squared numbers
for sqrd in squared_list:
    #Print the origanal number and the squared number
    print(f'Original: {nums[squared_list.index(sqrd)]} Squared: {sqrd}')

#60 characters (mapping):
#o=range(99)
#for i,j in zip(map(lambda n:n*n,o),o):print(j,i)

#57 characters (using lists):
#o=range(99)
#for i,j in zip([n*n for n in o],o):print(j,i)

#31 characters:
#for i in range(99):print(i,i*i)