#En (x) = (x + n) mod 26

values = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,
            "h":7,"i":8,"j":9,"k":10,"l":11,"m":12,
            "n":13,"o":14,"p":15,"q":16,"r":17,
            "s":18,"t":19,"u":20,"v":21,
            "w":22,"x":23,"y":24,"z":25}

key_list = list(values.keys())
val_list = list(values.values())

s = input("\n\n    Enter cypher text here to encrypt: ")
a = s.lower()
j = input("\n\n    Enter the encryption key: ")
dec_key = j.lower()
#assert 
  
b = values.get(dec_key)
def decrypt(cypher, key):
    plain_text = ""
    for letter in cypher:
        if len(dec_key) != 1 or dec_key not in key_list:
            print('    The encryption key must be a single letter..!')
            print('    Press \'Enter\' then relaunch the program')
            break
        elif letter == " ":
            new_letter = " "
            plain_text += new_letter
            pass
        elif letter not in values:
            plain_text += letter 
        else:
            value = values.get(letter)
            new_value = (value + key) % 26
            position = val_list.index(new_value) 
            new_letter = key_list[position]
            plain_text += new_letter
   
                
    print('\n\n    :::>>> ',plain_text) 
    
decrypt(a,b)
print('\n\n    made by ***ismail rajabu***')
input('\n\n\n    press Enter to exit.')

