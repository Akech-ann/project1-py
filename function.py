def sayhi(name,age):
    print("Hello " + name + "you are " + age)

sayhi("mike ","35")
sayhi("steve ","70")

def cube(num):
    return(num*num*num)

result = cube(4)
print(result)

is_male = True
is_tall = True

if is_male and is_tall:
    print("you are a tall man")
elif is_male and not (is_tall):
    print("you are a short male") 
elif not (is_male) and is_tall:
    print("you are not a male but you are tall")     

else:
    print("You are either not male nor not tall or both")

    # Write a function that takes two numbers as input and returns their sum.
def numbers(num1,num2):
    return num1+num2
print(numbers(2,56)) 


# Write a function that takes a string as input and returns the length of the string.
def str(str1):
    return len(str1)
a = str("how are you doing")
print(a)

# Write a function that takes a list of numbers as input
#  and returns the average of the numbers.
def lis(numb):
    a = sum(numb)
    b = len(numb)
    return a/b

numb = [12,43,54,65,75]
print(lis(numb) ) 


# Write a function that takes a string as input and returns True if the 
# string is a palindrome, and False otherwise.
def k (str2):
    str2 = str2.lower().replace(" "," ") 
    if str2==str2[::-1]:
        return True
    else:
        return False
str2 = ("anna")
result = k(str2)  
print(result)      


# Write a function that takes a list of numbers as input and returns the maximum 
# number in the list.
def returns(lists):
    return max(lists)
lists = [23,54,647,675,865]
p = returns(lists)
print(p)  

# Write a function that takes a list of numbers as input and returns the 
# minimum number in the list.
def retunees(numss):
    return min(numss)

numss = [123,43,345,63,546]
k = retunees(numss)
print(k)    

# Write a function that takes a list of strings as input and returns the longest
#  string in the list.
def long(longest):
    maxstr = ""
    for x in longest:
        if len(x)>len(maxstr):
           maxstr=x
    return maxstr
longest = ["ann","masian","ivy","perfectionist"]
longer = long(longest)
print(longer)  

# Write a function that takes a list of strings as input and returns
#  the shortest string in the list.

def short(shortest):
    f = ""
    for i in shortest:
        if len(f)>len(i):
            i = f
    return i
shortest = ["montry","ilove","alumni","book"]
k = short(shortest)
print(k) 

# Write a function that takes a string as input and returns a new string with
#  all vowels removed
def vowels(str5):
    str = "aeiouAEIOU"
    str1 = ""
    for c in str5:
        if c not in str:
            str1+=c
    return str1
str5 = ("book is wonderful")   
n = vowels(str5)
print(n) 

# Write a function that takes a list of 
# numbers as input and returns a new list with all even numbers removed.
def a(str6):
    str10 =[]
    for r in str6:
        if r %2!=0:
         str10.append(r)
    return str10
str6 = [12,33,54,64,75,7,8]
l = a(str6)
print(l)            



