# reverse the digits of given number without using built-in function

num = int(input('Enter a number: '))
rev = ''
while num > 0:
    rev += str(num % 10)
    num //= 10
print(f'Reversed Number: {rev}')

print("THIS PROGRAM IS WRITTEN BY Riya :- 0221BCA029")