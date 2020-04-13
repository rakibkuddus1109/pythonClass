# Datatypes in Python
    # Numbers: (int,float,complex(a+ib))
    # String: (str(anything that is declared inside "")) Ex: "Hyderabad123#"
    # List: (Sequence of values declared inside [], values are separated with comma) 
        # Ex: [1,'Python',5.4,[11,12,13]]
    # Tuples: (Sequence of values declared inside (), each value is separated with comma)
        # Ex: (1,'Python',5.4,(11,12,13))
    # Dictionary: (Sequence of Key/Value pair declared inside {}, each of them separated with comma)
        # Ex: {key1:value1,key2:value2} 
        # {'State':['Telangana','Andhra','Tamilnadu'],'Capital':['Hyderabad','Vizag','Chennai']}
    #Sets: (Sequence of values separated with comma declared inside {}, removes duplicate automatically)
        #Ex: {1,'Python',4.5,1} -- Sets would remove the duplicate 1 from here

# **Mutable: List/Dictionary/Sets (change can be made)
# **Immutable: Numbers/String/Tuples (no change can be made)

a,b=int(input("Enter a value:")),int(input("Enter b value:"))
# b=int(input("Enter b value:"))
print (a/b,a%b,a//b,a**b)
print(a==b,a!=b,a>=b,a<=b,a<b,a>b)

print(not(a==b,a!=b,a>=b,a<=b,a<b,a>b))