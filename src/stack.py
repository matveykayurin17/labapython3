class Stack:
    def __init__(self):
        self.stack=[]

    def pop(self)->int:
        "Функция возращает последний элемент стека и удаляет его"
        if len(self.stack)==0:
            raise IndexError
        remove=self.stack.pop()
        return remove

    def push(self,x:int|str)->None:
        "Функция добавляет элемент в стек"
        self.stack.append(x)

    def is_empty(self)->bool:
        "Функция проверяет пуст стек или нет. Если список пустой функция вовзращает False, иначе функция возвращает True"
        if len(self.stack)>=1:
            return True
        else:
            return False

    def __len__(self)->int:
        "Функция возращает длину стека"
        return len(self.stack)

    def peek(self)->int:
        "Функция возращает последний элемент стека"
        if len(self.stack)==0:
            raise IndexError
        else:
            return self.stack[-1]
