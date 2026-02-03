'''Write a program to print the following pattern 
123454321 
1234 *4321 
123  * * 321 
12   * * *  21 
1    * * * *   1'''


for i in range(5):
    # Left numbers
    for j in range(1, 6 - i):
        print(j, end="")

    # Stars
    for k in range(i):
        print(" *", end="")

    # Spaces between stars and right numbers
    for s in range(i):
        print(" ", end="")

    # Right numbers
    for j in range(5 - i, 0, -1):
        print(j, end="")

    print()
