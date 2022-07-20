import random 

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
sumbols = ['!','@','#','$','%','^','&','*','(',')','-','+']

print("PASSWORD GENERATOR")
val1 = int(input("Enter the number of words to be used: \n"))
val2 = int(input("Enter the number of integers to be used: \n"))
val3 = int(input("Enter the number of symbols to be used: \n"))
#easy level
def easy_password(a,b,c):
    samplpe = ""

    for char in range(1,val1+1):
        samplpe+=random.choice(letters)

    for char in range(1,val2+1):
        samplpe+=random.choice(numbers)

    for char in range(1,val3+1):
        samplpe+=random.choice(sumbols)

    print(f"Your expected password is: {samplpe}")


#Hard level
def hard_password(a,b,c):
    samplpe_list = []

    for char in range(1,val1+1):
        samplpe_list.append(random.choice(letters))

    for char in range(1,val2+1):
        samplpe_list.append(random.choice(numbers))

    for char in range(1,val3+1):
        samplpe_list.append(random.choice(sumbols))

    random.shuffle(samplpe_list)

    pssword = ""
    for char in samplpe_list:
        pssword += char

    print(f"Your required password is: {pssword}")


choice=str(input("Do you want Easy or Hard password? \n"))

if choice == 'Easy':
    easy_password(val1,val2,val3)
elif choice == 'Hard':
    hard_password(val1,val2,val3)
else:
    print("Enter either Easy or Hard!!!!!")



