# in this code you have to write a code for encrypt and decrypt from next 2 letter
# Example encrypt   => kapil = mcrkn
# decrypt =>  mcrkn = kapil



chars =         ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
shifted_chars = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']

def find_in_list(query, chars):
# this function is used to find the position of the "query" in the "mainlist". If "query" is in the list then it returns its position, otherwise it returns None
    mainlist_len = len(chars)
    range_for_loop = range(mainlist_len)
    index = None
    for i in range_for_loop:
        element = chars[i]
        if element == query:
            index = i
    return index


def encrypt_message(plain_msg):
# this fucnction takes "plain_msg" as an argument and print/return the encrypted message. The "plain_msg" is tranfered into "encrypted_msg" using "shifted_chars" list. Example, if plain_msg = "ng" then n => p, g => i  and hence encrypted_msg = "pi"
    encrypted_msg = ""
    for character in plain_msg:
      # for character in msg
        if character in chars:
            char_index = find_in_list(character, chars)
            new_char = shifted_chars[char_index]
            encrypted_msg = encrypted_msg + new_char
        else:
            encrypted_msg = encrypted_msg + character
    return encrypted_msg

def decrypt_message(encrypted_msg):
# this fucnction takes "encrypted_msg" as an argument and print/return the encrypted message. The "encrypted_msg" is tranfered into "decrypted_msg" using "shifted_chars" list. Example, if encrypted_msg = "pi" then p => n, i => g  and hence decrypted_msg = "ng"
    decrypted_msg = ""
    for character in encrypted_msg:
        if character in shifted_chars:
            char_index = find_in_list(character, shifted_chars)
            new_char = chars[char_index]
            decrypted_msg = decrypted_msg + new_char
        else:
            decrypted_msg = decrypted_msg + character
    return decrypted_msg


while True:
	choice = str(input("What do you want to do? 1. Encrypt a message 2. Decrypt a message  Enter `e` or `d` respectively!"))
	if choice == 'e':
	    plain_message = str(input("Enter message to encrypt??"))
	    print (encrypt_message(plain_message))
	elif choice == 'd':
	    encrypted_msg = str(input("Enter message to decrypt?"))
	    print (decrypt_message(encrypted_msg))
	else:
	    play_again = str(input("Do you want to try agian or Do you want to exit? (Y/N)"))
	    if play_again == 'Y' or play_again == "y":
	        continue
	    else:
        	break
