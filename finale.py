# Encode

# Decode
import re

lol = input('Encode(E) or Decode(D)?')


original_message = input('Original message: ')
message = list(original_message)
k = int(input('Shift = '))





def decode():
    all_con = [ord(char) for char in message]
    new_order =  [x + k for x in all_con]
    ano_con = [chr(char) for char in new_order]

    def check():
        for i in range(len(new_order)):
            if new_order[i] > 90:

                new_order[i] = (new_order[i] - 90) + 65

            elif new_order[i] < 65:

                new_order[i] = 90 - (65 - new_order[i])

    def translation():
        ''.join([*filter(str.isalnum, ano_con)])


    check()
    translation()
    ano_con = " ".join(map(str,ano_con))
    ano_con = ano_con.replace("',", "")
    print(ano_con)


def encode():
    char_con = [ord(num) for num in message]
    new_order =  [x - k for x in char_con]
    ano_con = [chr(char) for char in new_order]

    def check():
        for i in range(len(new_order)):
            if new_order[i] > 90:

                new_order[i] = (new_order[i] - 90) + 65

            elif new_order[i] < 65:

                new_order[i] = 90 - (65 - new_order[i])

    def translation():
        ''.join([*filter(str.isalnum, ano_con)])


    check()
    translation()
    ano_con = "".join(map(str,ano_con))
    ano_con = ano_con.replace("',", "")
    print(ano_con)


if lol.lower() == 'E' or lol == "E":
    print('user wanted to ENCODE')
    encode()
elif lol.lower() == 'D' or lol == "D":
    print('user wanted to DECODE')
    decode()
else:
    print('Type D or E')
