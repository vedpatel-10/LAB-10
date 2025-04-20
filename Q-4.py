lst = ['madam','Python',"malayalam",12321]

def palindrome(s):
   string =  str(s)
   if string== string[::-1]:
      return True
   else:
      False
    
lst_ans = list(filter(lambda s : palindrome(s),lst))
print(lst_ans)

#OUTPUT:
# ['madam', 'malayalam', 12321] 