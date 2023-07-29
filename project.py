print("##Number System Conversion##")

print("1: Binary to decimal,octal,hexadecimal")
print("2: Decimal to binary,octal,hexadecimal")
print("3: Octal to binary,decimal,hexadecimal")
print("4: Hexadecimal to binary,decimal,octal")
num = int(input("Select operation you want to perform :"))

if num==2:
    print("5: Decimal to Binary")
    print("6: Decimal to Hexadecimal")
    print("7: Decimal to Octal")
    num1 = int(input("Select Operation You want To Perform:"))
    n = int(input("Enter Number:"))
    # Decimal to binary
    if num1 == 5:
       l = list()  
       while n != 0:
         r = n % 2
         l.append(r)
         n = n//2  # this is used to round up to near whole
       l.reverse()
       print("The Binary Form of given number is ")
       for ele in l:
        print(ele, end="")
    
# Decimal to Hexadecimal 
    if num1 == 6:
       def f_decToHex(n):
          return hex(n)
       v_hex = f_decToHex(n)
       print("Hexadecimal form of given number is ",format(v_hex[2:]))
    
# Decimal to Octal    
    if num1==7:
      temp = n
      i=1
      sum=0
      while temp != 0:
       rem = int(temp % 8)
       rem = int(temp % 8)
       sum = sum + i * rem
       i = i * 10
       temp = temp/8
      print("Octal Number =" , sum)
      
      
if num==1:
    print("5: Binary to decimal")
    print("6: binary to hexadecimal")
    print("7: Decimal to Octal")
    num1 = int(input("Select Operation You want To Perform:"))
    n = input("Enter Number:")
    if num1==5:
        decimal_num = int(n, 2) 
        print(f"Decimal: {decimal_num}")
    if num1==6:
        hexadecimal_num = hex(n)
        print(f"Decimal: {hexadecimal_num}")
    if num1==7:
        octal_num = oct(n)
        print(f"Decimal: {octal_num}")        
        
        
if num==3:
    print("5: octal to decimal")
    print("6: octal to decimal")
    print("7: octal to hexadecimal")
    num1 = int(input("Select Operation You want To Perform:"))
    n = input("Enter Number:")
    if num1==5:
        decimal_num = int(n, 8) 
        print(f"Decimal: {decimal_num}")
    if num1==6:
        binary_num = bin(n)
        print(f"Decimal: {binary_num}")
    if num1==7:
        hexadecimal_num = hex(n)
        print(f"Decimal: {hexadecimal_num}")   
        
        
       
if num==4:
    print("5: hexadecimal to decimal")
    print("6: hexadecimal to binary")
    print("7: hexadeciaml to octal")
    num1 = int(input("Select Operation You want To Perform:"))
    n = input("Enter Number:")
    if num1==5:
        decimal_num = int(n, 16) 
        print(f"Decimal: {decimal_num}")
    if num1==6:
        binary_num = bin(n)
        print(f"Decimal: {binary_num}")
    if num1==7:
        octal_num = oct(n)
        print(f"Decimal: {octal_num}")                        
                     