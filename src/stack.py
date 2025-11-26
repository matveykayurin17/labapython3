class Stack:
    def __init__(self):
        self.stack=[]

    def pop(self)->int:
        if len(self.stack)==0:
            raise IndexError
        remove=self.stack.pop()
        return remove

    def push(self,x:int|str)->None:
        self.stack.append(x)

    def is_empty(self)->bool:
        if len(self.stack)>=1:
            return True
        else:
            return False

    def __len__(self)->int:
        return len(self.stack)

    def peek(self)->int:
        if len(self.stack)==0:
            raise IndexError
        else:
            return self.stack[-1]


