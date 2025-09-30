#BZ 1st Shopping List Manager
shop_list =[]
def print_list(print_list):
    for i in print_list:
        print(f'{print_list.index(i)+1}: {i}')
while True:
    action = input('1. View List\n2. Add Item\n3. Remove Item\n4. Exit\n> ')
    #Write your code here
    if action == '1':
        print('')
        print_list(shop_list)
        print('')
    elif action == '2':
        print('')
        to_add = input('Enter item to add:\n> ')
        shop_list.append(to_add)
        print(f'{to_add} has been added.')
        print('')
    elif action == '3':
        print('')
        to_remove = input('Enter item to remove:\n> ')
        if to_remove.isdigit():
            if int(to_remove)-1 <= len(shop_list):
                shop_list.pop(int(to_remove)-1)
                print(f'{shop_list[int(to_remove)-1]} has been removed.')
            else:
                print('Index out of range!')
        elif to_remove in shop_list:
            shop_list.remove(to_remove)
            print(f'{to_remove} has been removed.')
        else:
            print('Please input an item on the list!')
        print('')

    elif action == '4':
        break