#this is a reference(in alphabetical order) for the entire program to function and move the alphabets back on forth in 
string_of_alphabets = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
#new parameters message and shift_number and uses for and if statements checking for alphabets using string_of_alphabets and then gets their pos using indexing and finally creates a result
def Encrypt(message, shift_number):
    result = ""
    for i  in message:
        if i in string_of_alphabets:
            position = string_of_alphabets.index(i)
            new_position = (position + shift_number) % 26 
            result = result + string_of_alphabets[new_position]
        else:
          result = result + i
    print(result)
#same as encrypt just subtracts the position from the shift and divides it by 26 
def Decrypt(message,shift_number):
    result = ''
    for i in message:
        if i in string_of_alphabets:
            position = string_of_alphabets.index(i)
            new_position = (position - shift_number) % 26
            result = result + string_of_alphabets[new_position]
        else:
            result = result + i
    print(result)
#simple keeps everything in lower to avoid case sensitive troubles ;/
Cypher = input("Enter the code you want to encrypt/decrypt:" , )
shift = int(input("enter the shift in alphabets:",))
Cypher =  Cypher.lower()

#one mistake i did was using "e" and "d" instead or encrypt and decrypt idk it created sm issues
choice = input("do you want to Encrypt or Decrypt?:",)
if choice.lower() == "encrypt":
    Encrypt(Cypher , shift)
elif choice.lower() == "decrypt":
    Decrypt(Cypher , shift)


    
