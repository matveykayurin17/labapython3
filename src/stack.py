import logging                                     # noqa: E402
from src.config import LOGGING_CONFIG              # noqa: E402
logging.config.dictConfig(LOGGING_CONFIG)       #настройка логера
logger = logging.getLogger(__name__)
class Stack:
    def __init__(self):
        self.stack=[]

    def pop(self)->int:
        "Функция возращает последний элемент стека и удаляет его"
        if len(self.stack)==0:
            raise IndexError
        remove=self.stack.pop()
        logger.info('Элемент удалён из стека')
        return remove

    def push(self,x:int|str)->None:
        "Функция добавляет элемент в стек"
        logger.info('элемент добавлен в стек')
        self.stack.append(x)

    def is_empty(self)->bool:
        "Функция проверяет пуст стек или нет. Если список пустой функция вовзращает False, иначе функция возвращает True"
        if len(self.stack)>=1:
            logger.info('Стек не пуст')
            return True
        else:
            logger.info("Стек пуст")
            return False

    def __len__(self)->int:
        "Функция возращает длину стека"
        logger.info('длина стека:')
        return len(self.stack)

    def peek(self)->int:
        "Функция возращает последний элемент стека"
        if len(self.stack)==0:
            logger.info('стек пуст')
            raise IndexError
        else:
            return self.stack[-1]
