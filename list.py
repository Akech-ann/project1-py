# Write a program that creates a list of integers from 1 to 10,
#  and then prints the sum of all the even numbers in the list.




def a (numb):
    w = 0
    for x in numb:
        if x %2==0:
            w+=x
    return w     
 
numb = list(range(1,11))
d = a(numb) 
print(d)    
# Write a program that prompts the user to enter a sentence, and then prints out a list of all the unique words in the sentence 
# (i.e., no word should appear twice in the list).

def splite(arr):
    x = arr.split()
    p = []
    for word in x:
        if(word not in p):
            p.append(word)
    return p
arr =   "the best day day of my life was 2016 december"
k = splite(arr)
print(k)          


# Write a program that uses a tuple to represent a person's name, age, and gender, and then prints out a message that says "Hello, my name 
# is [name], I am [age] years old, and I am [gender]."


