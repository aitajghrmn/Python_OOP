n=int(input("Enter a number: "))

print("Cüt ədədlər: ", end='')

for i in range (1 , n+1 ) :
    if i % 2 == 0:
        print(i, end=' ')

print()

print("Tək ədədlər: ", end='')

for i in range (1 , n+1 ) :
    if i % 2 != 0:
        print(i, end=' ')
