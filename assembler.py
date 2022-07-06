f=open(r"C:\CSSS\CO\abc.txt")
Open=f.read().splitlines()

Reg_add ={"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}


Opcode ={    
"add":["10000","A"],
"sub":["10001","A"],
"movI":["10010","B"],
"movR":["10011","C"],
"ld":["10100","D"],
"st":["10101","D"],
"mul":["10110","A"],
"div":["10111","C"],
"rs":["11000","B"],
"ls":["11001","B"],
"xor":["11010","A"],

"or":["11011","A"],
"and":["11100","A"],
"not":["11101","C"],
"cmp":["11100","C"],

"jmp":["11111","E"],
"jlt":["01100","E"],
"jgt":["01101","E"],
"je":["01111","E"],
"hlt":["01010","F"]}

Regsym=['add', 'sub', 'mov', 'st', 'mul', 'div', 'rs', 'ls', 'xor', 'or', 
'and', 'not', 'cmp', 'jmp', 'jlt', 'jgt', 'je', 'hlt']

Reg=[ "R0", "R1" , "R2" , "R3" , "R4" , "R5" , "R6"]
flag=[ "R0", "R1" , "R2" , "R3" , "R4" , "R5" , "R6" , "FLAGS"]
label=["hlt"]
var=[]
err=False

#Main Funtion

def Range(a):
    global err
    try:
        n = int(a[1:])
        if(n>255 or n<0):
            print("Line: ",line_number,"Not in range")
            err=True

    except:
        print("Line: ",line_number,"Invalid value")
        err=True

def A(value):
    global err
    if(len(value)!=4):
        print("Line: ",line_number,"Inavlid Syntax")
        err=True
        return

    for i in range(1,len(value)):
        if(value[i]=="FLAGS"):
            print("Line: ",line_number,"Invalid flag declare")
            err=True

        elif(value[i] not in Reg):
            print("Line: ",line_number, "Invalid register name ")
            err=True

def B(value):
    global err
    if(len(value)!=3):
        print("Line: ",line_number,"Invalid Syntax")
        err=True
        return   

    if(value[1]=="FLAGS"):
        print("Line: ",line_number,"Inavlid flag")
        err=True

    elif(value[1] not in Reg):
        print("Line: ",line_number,"Inavlid register name")
        err=True
        
    a= value[2]
    if(a[0]!="$"):
        print("Line: ",line_number,"Invalid syantax")
        err=True
    else:
        Range(a)

def C(value):
    global err
    if(len(value)!=3):
        print("Line: ",line_number,"Invalid syntax")
        err=True
        return

    if(value[1]=="FLAGS"):
        print("Line: ",line_number,"Inavlid flag")
        err=True

    elif(value[1] not in Reg):
        print("Line: ",line_number,"Invalid register")
        err=True

    if(value[0]=="movR" and value[2] not in flag):
        print("Line: ",line_number,"Invalid syntax")
        err=True

    elif value[0]!="movR" and value[2] not in Reg:
        print("Line: ",line_number,"Invalid name")
        err=True

def D(value):
    global err
    if(len(value)!=3):
        print("Line: ",line_number,"Inavlid syntax")
        err=True
        return
        
    if(value[2] in label):
        print("Line: ",line_number,"Invalid label")
        err=True

    elif(value[2] not in var):
        print("Line: ",line_number,"Invalid variable")
        err=True

def E(value):
    global err
    if(len(value)!=2):
        print("Line: ",line_number,"Invalid syntax")
        err=True
        return

    if(value[1] in var):
        print("Line: ",line_number,"Inavlid varibale")
        err=True
            
    elif(value[1] not in label):
        print("Line: ",line_number,"Invalid label ")
        err=True

def F(value):
    if(line_number!=len(Open)):
        print("Line: ", line_number , "Add hlt at end")
        err=True

    elif(len(value)!=1):
        print("Line: ",line_number,"Inavlid syntax")
        err=True




def variable(value):
    global err
    global flag
    if(value[0]!="var"):
        flag=1

    if value[0]=="var" and len(value)!=2:
        print("Line: ",line_number,"invalid syntax")
        err=True
        return

    if value[0]=="var":
        if(flag==1):
            print("Line: ",line_number,"Invlaid variable")
            err=True
        if(value[1] in var):
            print("Line: ",line_number,"Invlaid variable")
            err = True
        else:
            var.append(value[1])   

def func_label(value):
    global err
    if(value[0][-1]==":"):
        if(value[0][0:-1] in label):
            print("Line: ",line_number,"Invalid labels")
            err=True
        else:
            label.append(value[0][0:-1])

def func_hlt(value):
    global err
    if(len(value)==2 ):
        if value[1]!="hlt":
            print("Line: ",(line_number)+1,"Add hlt at end")
            err=True

    elif(value[0]!="hlt"):
        print("Line: " ,(line_number)+1 ,"Add hlt at end")
        err=True



line_number =0 
flag=0
i=0
while (i<len(Open)):
    line_number+=1
    y=len(Open[i])
    if(y==0):
        continue
    value = list(Open[i].split())
    variable(value)
    i+=1

line_number=0   
i=0  
while (i<len(Open)):
    line_number+=1
    y=len(Open[i])
    if(y==0):
        continue
    value = list(Open[i].split())
    func_label(value)
    i+=1    

line_number=0                                                      
for i in Open:
    line_number+=1
    if(len(i)==0):
        continue

    value = list(i.split())

    if line_number==len(Open):
        func_hlt(value)

    if(value[0]=="var"):
        continue

    if(value[0][0:-1] in label):
        value.pop(0)

    if(len(value)==0):
        print("Line: ",line_number,"invalid defnation of label")
        err=True
        continue
    
    if(value[0] not in Regsym):
        print("Line: ",line_number,value[0],"Invalid instrction name")
        err=True
        continue

    if(value[0]=="mov" and len(value)>=2):
        c = value[2][0]
        if(65<=ord(c)<=90 or 97<=ord(c)<=122):
            value[0]="movR"
        else:
            value[0]="movI"
    
    if (Opcode[value[0]][1] == "A"):
        A(value)
            
    elif (Opcode[value[0]][1] == "C"):
        C(value)
        
    elif (Opcode[value[0]][1] == "B"):
        B(value)

    elif (Opcode[value[0]][1] == "D"):
        D(value)
    
    elif (Opcode[value[0]][1] == "E"):
        E(value)

    elif (Opcode[value[0]][1] == "F"):
        F(value)

    else:
        print("Line: ",line_number,"invalid syntax",sep=' ')
        err=True


label={}
var={}

t=1
address=-1

if(err==True):
    exit()




for i in Open: #loop store address of all variables
    if len(i)==0:
        continue
    value = list(i.split())
    
    if(value[0] in Regsym):
        address+=1

    if value[0]=="hlt":
        label[value[0]+":"]=address

    if(value[0][-1]==":"):
        address+=1
        label[value[0]]=address
        
i=0
while (i<len(Open)):    #loop store address of labels
    y=len(Open[i])
    if(y==0):
        continue
    value = list(Open[i].split())
    if value[0]=="var" and len(value)==2:
        var[value[1]]=t+address
        t+=1
    i+=1
for i in Open:  #convert assemmbly to binary

    if(len(i)==0):
        continue

    value = list(i.split())
    if( len(value)>1 and value[0] in label and value[1] in Regsym):
        value.pop(0)

    if (value[0] in Regsym):

        if(value[0]=="mov" ):
            if(value[2][0]=="$"):
                value[0]="movI"
            else:
                value[0]="movR"

        if (Opcode[value[0]][1]=="B"):
            x=value[1]
            y=value[2][1:]
            z=bin(int(y))[2:]
            p=Opcode[value[0]][0]+Reg_add[x]+(8-len(z))*"0"+z

        elif (Opcode[value[0]][1]=="A"):
            x=value[1]
            y=value[2]
            z=value[3]
            p=Opcode[value[0]][0]+"00"+Reg_add[x]+Reg_add[y]+Reg_add[z]
    
        elif (Opcode[value[0]][1]=="C"):
            x=value[1]
            y=value[2]
            p=Opcode[value[0]][0]+"00000"+Reg_add[x]+Reg_add[y]

        elif (Opcode[value[0]][1]=="D"):
            x=value[1]
            y=bin(var[value[2]])[2:]
            p=Opcode[value[0]][0]+Reg_add[x]+(8-len(y))*"0"+y

        elif (Opcode[value[0]][1]=="E"):
            x=value[1]
            y=bin(label[x+":"])[2:]
            p=Opcode[value[0]][0]+"000"+(8-len(y))*"0"+y

        elif (Opcode[value[0]][1]=="F"):
            p=Opcode[value[0]][0]+"00000000000"
        print(p)

