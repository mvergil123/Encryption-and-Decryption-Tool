#   Mike Vergil
#   CSCI 128 – Section L
#   Assessment 9
#   References: w3schools.com
#   Time: 4 hours

import string

def encrypt(phrase, number):

    lowercase_list = list(string.ascii_lowercase)
    uppercase_list = list(string.ascii_uppercase)

    #alters the shift value


    #this will see how many times it has to go through
    number = number % 26

    encrypted_text = ""
    ind = 0

    for letter in phrase:
        #iterates through each letter
        if letter.isalpha():
            #is a letter
            if letter.islower():
                #lowercase letter
                ind = lowercase_list.index(letter)
                if ind+number >= 26:
                    value = (ind+number) - 26
                    letter = lowercase_list[0+value]
                else: 
                    letter = lowercase_list[ind+number]
            else:
                #capital letter
                ind = uppercase_list.index(letter)
                if ind+number >= 26:
                    value = (ind+number) - 26
                    letter = uppercase_list[0+value]
                else: 
                    letter = uppercase_list[ind+number]

        encrypted_text += letter
    
    return encrypted_text



def decrypt(text, keyword):
    worduni = ord(keyword[0])
    worduni2 = ord(keyword[1])
    if len(keyword) > 2:
        worduni3 = ord(keyword[2])

    ind = 0
    for num in range(26):
        word = encrypt(text, num)
        for letter in word:
            value = ord(letter)
            if value == worduni and word.index(letter) != len(word) - 1:
                ind = word.index(letter)
                next_value = ord(word[ind+1])
                if next_value == worduni2 and len(keyword) > 2:
                    final_value = ord(word[ind+2])
                    if final_value == worduni3:
                        if num == 0:
                            pass
                        else:
                            num = 26-num
                        return (word, num)
                elif next_value == worduni2:
                        if num == 0:
                            pass
                        else:
                            num = 26-num
                        return (word, num)            
                else:
                    continue

    return("ERROR")

def test_encrypt(word, shift, expected):
    result = encrypt(word, shift)
    assert result == expected



def test_decrypt(word, keyword, expected_word, expected_shift):
    result = decrypt(word, keyword)
    if result == "ERROR":  
        actual_word = result
        actual_shift = 0  
    else:
        actual_word = result[0]
        actual_shift = result[1]

    assert actual_word == expected_word
    assert actual_shift == expected_shift


                
            
if __name__ == "__main__":
    option = int(input("OPTION> "))
    if option == 1:
        #encrypt
        message = str(input("MESSAGE> "))
        shift = int(input("SHIFT> "))
        print(f"OUTPUT {encrypt(message, shift)}")
    elif option == 2:
        #decrypt
        message = input("MESSAGE> ")
        key = input("KEY> ")
        result = decrypt(message, key)
        if result == "ERROR":
            print("OUTPUT",result)
        else:
            print(f"OUTPUT {result[0]}")
            print(f"OUTPUT {result[1]}")

    else:
        #all the tests written will run
            test_encrypt("My secret message", 10, "Wi combod wocckqo")
            test_encrypt("N0t numb3r5", 7, "U0a ubti3y5")
            test_encrypt("Large negative shift", -82, "Hwnca jacwpera odebp")
            test_decrypt("Ger csy vieh xlmw?", "read", "Can you read this?", 4)
            test_decrypt("Ujqhlgyjshzq ak fwsl!", "is", 'Cryptography is neat!', 18)
            test_decrypt("Ujqhlgyjshzq ak fwsl!", "message", "ERROR", 0)
        
