item1=int(input("eneter the first price"))
item2=int(input("eneter the second price"))
item3=int(input("eneter the third price"))
item4=int(input("eneter the fouth price"))
item5=int(input("eneter the fourth price"))
sub_total=item1+item2+item3+item4+item5
Tax=(sub_total*6)/100
total=sub_total+Tax
print("The sub total is ",sub_total)
print("the tax is ",Tax)
print("the total is ",total)
