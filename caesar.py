#Encode

#Decode
import re

lol = input('Encode(E) or Decode(D)?')


original_message = input('Original message: ')
message = list(original_message)
k =int(input('Shift = '))






def encode():
    all_con = [ord(char) for char in message]
    new_order =  [x+ k for x in all_con]
    ano_con = [chr(char) for char in new_order]
     def check():
     for i in range(len(new_order)):
         if new_order[i] > 90:

             new_order[i] = (new_order[i]-90)+65

         elif new_order[i] < 65:

             new_order[i] = 90 - (65-new_order[i])
     def translation():
      re.sub('\W+','', ano_con)

     check()
     translation()

def decode():
    char_con = [ord(num) for num in message]
    new_order =  [x - k for x in all_con]
    ano_con = [chr(char) for char in new_order]
    def check():
     for i in range(len(new_order)):
         if new_order[i] > 90:

             new_order[i] = (new_order[i]-90)+65

         elif new_order[i] < 65:

             new_order[i] = 90 - (65-new_order[i])
    def translation():
     re.sub('\W+','', ano_con)

    check()
    translation()


if lol.lower() == 'E':
    print('user wanted to ENCODE')
    encode()
elif lol.lower() == 'D':
    print('user wanted to DECODE')
    decode()
else:
    print('Type D or E')






































