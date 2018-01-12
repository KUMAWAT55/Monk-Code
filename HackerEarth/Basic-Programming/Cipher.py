input_string = input()
cipher_key = int(input())
cipher_text = ''

for input_char in input_string : 
    char_val = ord(input_char)
    
    if 65 <= char_val <= 90 : 
        cipher_text += chr( ((char_val-65) + cipher_key)%26 + 65 )
    elif 97 <= char_val <= 122 : 
        cipher_text += chr( ((char_val-97) + cipher_key)%26 + 97 )
    elif 48 <= char_val <= 57 :
        cipher_text += chr( ((char_val-48) + cipher_key)%10 + 48 )
    else :
        cipher_text += input_char
print ( cipher_text )
