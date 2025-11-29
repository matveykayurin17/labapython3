import logging                                     # noqa: E402
from src.config import LOGGING_CONFIG              # noqa: E402
logging.config.dictConfig(LOGGING_CONFIG)       #настройка логера
logger = logging.getLogger(__name__)
class Queue:
    def __init__(self):
        self.stack=[]

    def __len__(self)->int:
        "Функция возвращает длину очереди"
        logger.info('длина очереди:')
        return len(self.stack)

    def is_empty(self)->bool:
        "Функция проверяет пуста ли очередь или нет. Если список пустой функция возращает False, иначе функция возвращает True"
        if len(self.stack)>=1:
            logger.info('очередь не пуста')
            return True
        else:
            logger.info('очередь пуста')
            return False

    def enqueue(self, x: int|str) -> None:
        "Функция добавляет элемент в очередь"
        logger.info('элемент добавлен в очередь')
        self.stack.append(x)

    def dequeue(self) -> int:
        "Функция удаляет первый элемент очереди и выводит его"
        logger.info('первый элемент удалён')
        if len(self.stack)==0:
            raise IndexError
        else:
            remove = self.stack.pop(0)
            return remove

    def front(self)->int:
        "Функция возвращает первый элемент очереди"
        logger.info('первый элемент очереди:')
        if len(self.stack)==0:
            raise IndexError
        else:
            return self.stack[0]
