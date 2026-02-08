'''WAP to input a list of scores for N students in a list data type. Find the score of the runner
up and print the output. 
Sample Input 
N = 5 
Scores= 2 3 6 6 5 
Sample output 
5 '''

n = int(input())
scores = list(map(int, input().split()))

unique_scores = list(set(scores))
unique_scores.sort()

print(unique_scores[-2])

