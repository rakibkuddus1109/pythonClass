# Operator is symbol which performs operation between two or more operands

# Arithmatic operator (+,-,*,/,%,//,**)
# Relational/Comparison operator (==,!=,>,<,>=,<=)
# Logical operator (and,or,not)
# Assignment operator (=,+=,-=)
# Membership operator (in,not in)
# Identity operator (is,is not)
# Bitwise operator (Bitwise And(&),Bitwise Or(|),Bitwise XOR(^),Bitwise Not(~), Left Shift(<<), Right Shift(>>))

# a=32%5
# print(a)

# a=32//5
# print(a)

# a=32/5
# print(a)

# a,b=32//5,32%5
# print(a,b)

# a+=6
# b-=3
# print(a,b)

# a,b=int(input("Enter a value:")),int(input("Enter b value:"))
# print (a/b,a%b,a//b,a**b)
# print(a==b,a!=b,a>=b,a<=b,a<b,a>b)

# a="Python is a programming language"
# print("program" in a)
# print("python" not in a)

# a=["python","django","datascience"]
# print("django" in a)
# print("djang0" in a)
# print("science" in a)
# print("thon" not in a)

# a=67
# b=67

# print(a is b)

# a="python"
# b="Python"

# print(a is b)

# a=(1,2,3)
# b=(1,2,3)

# print(a is b)
# print(id(a))
# print(id(b))

# a=[1,2,3]
# b=[1,2,3]

# print (a is b)
# print(id(a))
# print(id(b))

# print(bin(73))

# A       B       A&B         A|B         A^B
# --------------------------------------------
# 0       1        0           1           1
# 1       0        0           1           1
# 1       0        0           1           0
# 1       1        1           1           0
# 0       0        0           0           1

a=34
b=23
# 34 -- 100010
# 23 -- 010111
# -------------
#       000010  -- Result of & Operation (2)
#       110111  -- Result of | Operation (55) 
#       110101  -- Result of ^ Operation (53)

print(a&b)
print(a|b)
print(a^b)

# Left Shift -- It will shift left most bit towards right & replace with 0
print(a<<1) # 00100010<<1=01000100 (68)
# Right Shift -- It will shift right most bit towards left & replace with 0
print(b>>1) # 00010111>>1=00001011 (11)

# Bitwise Not (~)
# 00100010 -- 34
# 11011101 -- 1's complement of above (replacing 1 with 0 and 0 with 1)
# 00100011 -- 35 (if above ends with 1 then right most would start with 1 and then replace 1 with 0 & 0 with 1)
print(~a)

