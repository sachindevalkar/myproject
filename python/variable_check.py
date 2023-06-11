varname=eval(input("Enter the value to identify vartype : "))
             
if type(varname)==float:
    print("Type of variable is float")
             
elif type(varname)==int:
    print("Type of variable is int")

elif type(varname)==bool:
    print("Type of variable is bool")

elif type(varname)==str:
    print("Type of variable is str")
            
elif type(varname)==list:
    print("Type of variable is list")

elif type(varname)==tuple:
    print("Type of variable is tuple")

elif type(varname)==dict:
    print("Type of variable is Dictionaries")

elif type(varname)==set:
    print("Type of variable is set")

elif type(varname)==frozenset:
    print("Type of variable is frozenset")


else:
    print("Unknown variable type")

