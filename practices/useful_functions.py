def int_input(prompt,error):
    while True:
        num = input(prompt).lower().strip()
        if num.isdigit():
            return int(num)
        else:
            print(error)
def str_input(prompt):
    return str(input(prompt)).lower().strip()
def strip_input(prompt):
    return str(input(prompt)).lower().replace(' ','').replace('!','').replace('?','').replace(',','').replace('.','')
