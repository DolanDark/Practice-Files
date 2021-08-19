parent = input()
prompt = input()

if prompt == "N":
    print(f"Total members : 1 \n Comission Details \n {parent} : 250 INR")
if prompt == "Y":
    child=list(map(str,input().split(",")))
    print(f"Total members = {len(child)+1}")
    print(f"Comission Details\n {parent} : {len(child)*500}")
    for i in child:
        print(f"{i}:250 INR")
