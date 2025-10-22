#BZ 1st Ceaser Cypher Encoder/Decoder
#Define possible inputs
input_encode = ['encode','1','code']
input_decode = ['decode','2','uncode']
input_force_decode = ['brute force decode','3','force decode','force']
input_end = ['end','terminate','exit','4','done','lose','win','die']
#Define encode function
def encode(text,key):
    #Define empty encoding string
    encoded = ''
    #define empty encoded character string
    encoded_char = ''
    #loop through characters of input
    for char in text:
        #if character is not a letter
        if not char.isalpha():
            #append the character to encoded string
            encoded += char
            #continue to next iteration
            continue
        #set encoded character string to character's ascii value
        encoded_char = ord(char)
        #increase ascii value by key
        encoded_char += key
        #if encoded  character is greater than the value of z
        if encoded_char > 122:
            #set encoded character to the value of a  minus 1 plus the amount over the value of z
            encoded_char = 96 + encoded_char - 122
        #if encoded  character is greater than the value of Z
        elif encoded_char > 90 and encoded_char < 97:
            #set encoded character to the value of A minus 1 plus the amount over the value of Z
            encoded_char = 64 + encoded_char - 90
        #change endoded character back to a string
        encoded_char = chr(encoded_char)
        #append encoded character to encoding string
        encoded += encoded_char
    #return encoded string
    return encoded
#define decode function
def decode(text,key):
   #Define empty decoding string
    decoded = ''
    #define empty decoded character string
    decoded_char = ''
    #loop through characters of input
    for char in text:
        #if character is not a letter
        if not char.isalpha():
            #append the character to decoded string
            decoded += char
            #continue to next iteration
            continue
        #set decoded character string to character's ascii value
        decoded_char = ord(char)
        #decrease ascii value by key
        decoded_char -= key
        #if decoded character is less than the value of A
        if decoded_char < 65:
            #set decoded character to the value of Z plus 1 minus the amount under the value of A
            decoded_char = 91 - (65 - decoded_char)
        #if decoded character is less than the value of a
        if decoded_char < 97 and decoded_char > 90:
            #set decoded character to the value of z plus 1 minus the amount under the value of a
            decoded_char = 123 - (97 - decoded_char)
        #change dedoded character back to a string
        decoded_char = chr(decoded_char)
        #append decoded character to decoding string
        decoded += decoded_char
    #return decoded string
    return decoded
#loop forever
while not False:
    #loop forever
    while not False:
        #have user input whether they want to encode, decode, brute force decode, or exit
        op = input('1. Encode, 2. Decode, 3. Force Decode, or 4. Exit?\n')
        #check if input is in valid encode inputs
        if op in input_encode:
            #have the user input something to encode
            uncoded = input('What would you like to encode?\n')
            #forever
            while not False:
                #have the user input the key
                key = input('What key would you like to use?\n')
                #if the key is a number
                if key.isdigit():
                    #convert the input to an integer
                    key = int(key)
                    #exit the loop
                    break
                #otherwise
                else:
                    #tell the user to input a number
                    print('Please input a number!')
            #run encode function
            coded = encode(uncoded,key)
            #display output
            print(coded)
        #else, check if input is in valid decode inputs
        elif op in input_decode:
            #have the user input something to decode
            uncoded = input('What would you like to decode?\n')
            #forever
            while not False:
                #have the user input the key
                key = input('What is the key?\n')
                #if the key is a number
                if key.isdigit():
                    #convert the input to an integer
                    key = int(key)
                    #exit the loop
                    break
                #otherwise
                else:
                    #tell the user to input a number
                    print('Please input a number!')
            #run decode function
            coded = decode(uncoded,key)
            #display output
            print(coded)
        #else, check if input is in valid force decode inputs
        elif op in input_force_decode:
            #have the user input something to decode
            uncoded = input('What would you like to decode?\n')
            for key in range(1,26):
                print(decode(uncoded,key))
        #else, check if input is in valid end inputs
        elif op in input_end:
            #thank the user
            print('Thanks for using this program!')
            #exit the loop
            break
        #otherwise
        else:
            #tell the user to input a valid input
            print('Please use a valid input!')

