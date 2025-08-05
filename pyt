# a= int(input())
# if a >= 50:
#     print("go to ground floor")
# else:
#     print("go to first floor")
    
# a = (input("whats your name?"))
# if a[0]==a[len(a)-1]:
#     print("lucky")
# else:
#     print("super lucky")    

# token = int(input("amount?"))
# brand = input()
# if token==10:
#     print("chips")
# elif token==20:
#     if(brand="maaza" or "fanta" or "sprite"):  else:
#     print("water bottle")   

# a = (input("word"))
# if a[0]==a[len(a)-1]:
#     print("it is palindrome")
# else:
#     print("it is not")    
# a = (input("word"))
# if a==a[: : -1]:
#     print("it is palindrome")
# else:
#      print("it is not")    

# n= input()
# is_palindrome = True
# i=0
# j=len(n)-1
# while(i<=j):
#     if n[i]==n[j]:
#         i+=1
#         j-=1
#     else:
#         is_palindrome=False
#         break
# print("palindrome" if is_palindrome else "not palindrome")    

n= int(input())
is_prime =True
for i in range(2,n):
    if n%i ==0:
        is_prime = False
print("is a prime"if is_prime else "not a prime")        

