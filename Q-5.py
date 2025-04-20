def length(s):
    string = str(s)
    if len(string) > 8:
        return True
    else:
        return False
    
faculty_names = ["Ankur","Vinod","sachidanand","shrikant","pushpkiran"]
lst_ans = list(filter(lambda s : length(s),faculty_names))
print(lst_ans)

#OUTPUT:
# ['sachidanand', 'pushpkiran']