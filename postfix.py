class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

def postFix():
    opn=["*","/","+","-"]
    w=1
    item=input()
    s=Stack()

    for i in item:
        if(i not in opn):
            s.push(i)
        elif(i in opn):
            if(s.isEmpty()== True):
                print("Wrong statement")
                return 
            else:
                temp1=s.pop()
                temp2=s.pop()
                print('LD '+temp2)
                if(i=="+"):
                     print("AD "+temp1)
                     s.push('TEMP'+str(w))
                     w+=1
                elif(i=="-"):
                     print("SB "+temp1)
                     s.push("TEMP"+str(w))
                     w+=1
                elif(i=="*"):
                     print("ML "+temp1)
                     s.push("TEMP"+str(w))
                     w+=1
                elif(i=="/"):
                     print("DV "+temp1)
                     s.push("TEMP"+str(w))
                     w+=1

                print("ST "+s.peek())

header = """
      ********************************************

                    WeLcOmE postFix
                    
             ********************************************

    




"""
help = """
   you have to input
   1. Statement(Ex:ABC*+DE-/)
   
   
    





"""
print("{0}Instructions:{1}\nPlease enter the command...".format(header, help))
print(postFix())
