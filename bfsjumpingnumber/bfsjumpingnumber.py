

class Queue: 
    def __init__(self): 
        self.lst = [] 
  
    def is_empty(self): 
        return self.lst == [] 
  
    def enqueue(self, elem): 
        self.lst.append(elem) 
  
    def dequeue(self): 
        return self.lst.pop(0) 
#Prints all jumping numbers smaller than or equal to x starting with 'num'. It mainly does BFS starting from 'num'.
def bfs(x, num): 
    #Create a queue and enqueue 'num' to it 
    q = Queue() 
    q.enqueue(num) 
    #Do BFS starting from num
    while (not q.is_empty()): 
        num = q.dequeue() 
        if num<= x: 
            print(str(num), end =' ') 
            last_dig = num % 10
            #If last digit is 0, append next digit only
            if last_dig == 0: 
                q.enqueue((num * 10) + (last_dig + 1)) 
            #If last digit is 9, append previous digit only 
            elif last_dig == 9: 
                q.enqueue((num * 10) + (last_dig - 1)) 
                #If last digit is neighter 0 nor 9, append both previous and next digits
            else: 
                q.enqueue((num * 10) + (last_dig - 1)) 
                q.enqueue((num * 10) + (last_dig + 1)) 

def printJumping(x): 
    print (str(0), end =' ') 
    for i in range(1, 10): 
        bfs(x, i)
x = 105

printJumping(x)