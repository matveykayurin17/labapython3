class Queue:
    def __init__(self):
        self.stack=[]

    def __len__(self)->int:
        "Функция возвращает длину очереди"
        return len(self.stack)

    def is_empty(self)->bool:
        "Функция проверяет пуста ли очередь или нет. Если список пустой функция возращает False, иначе функция возвращает True"
        if len(self.stack)>=1:
            return True
        else:
            return False

    def enqueue(self, x: int|str) -> None:
        "Функция добавляет элемент в очередь"
        self.stack.append(x)

    def dequeue(self) -> int:
        "Функция удаляет первый элемент очереди и выводит его"
        if len(self.stack)==0:
            raise IndexError
        else:
            remove = self.stack.pop(0)
            return remove

    def front(self)->int:
        "Функция возвращает первый элемент очереди"
        if len(self.stack)==0:
            raise IndexError
        else:
            return self.stack[0]
