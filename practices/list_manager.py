#BZ 1st Shopping List Manager
shop_list = []
view_response = ['1','view','see','list','view list','show','show list','see list','print','print list','one']
add_response = ['2','add','append','new','new item','add item','add to list','new list item','add list item','append item','append list item','two']
remove_response = ['3','remove','remove item','delete','delete item','undo','three']
exit_responce = ['4','exit','end','terminate','exit list','exit program','end program','terminate program','four']
def print_list(print_list):
    for i in print_list:
        print(f'{print_list.index(i)+1}: {i}')
while True:
    action = input('1. View List\n2. Add Item\n3. Remove Item\n4. Exit\n> ')
    #Write your code here
    if action in view_response:
        print('')
        print_list(shop_list)
        input('Press enter to continue\n')
    elif action in add_response:
        print('')
        to_add = input('Enter item to add:\n> ')
        shop_list.append(to_add)
        print(f'{to_add} has been added.')
        input('Press enter to continue\n')
    elif action in remove_response:
        print('')
        to_remove = input('Enter item to remove:\n> ')
        if to_remove.isdigit():
            if int(to_remove) <= len(shop_list) and int(to_remove) > 0:
                print(f'{shop_list[int(to_remove)-1]} has been removed.')
                shop_list.pop(int(to_remove)-1)
            else:
                print('Index out of range!')
        elif to_remove in shop_list:
            shop_list.remove(to_remove)
            print(f'{to_remove} has been removed.')
        else:
            print('Please input an item on the list!')
        input('Press enter to continue\n')
    elif action in exit_responce:
        break