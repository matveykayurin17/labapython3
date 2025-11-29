from src.fiboandfasctori import fibo, fibo_recursive, factorial, factorial_recursive
from src.sort import bubble_sort,quick_sort,counting_sort,radix_sort,heap_sort,bucket_sort
from src.stack import Stack
from src.Queue import Queue
import logging
from src.config import LOGGING_CONFIG
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)
def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    print('Введите команду')
    command=input()
    if command=='fibbonachi recursive':
        print('Введите число')
        i=int(input())
        try:
            print(fibo_recursive(i))
        except Exception as e:
            logger.error(f"Ошибка:{e}")
    elif command=='fibbonachi not recursive':
        print('Введите число')
        i=int(input())
        try:
            print(fibo(i))
        except Exception as e:
            logger.error(f"Ошибка:{e}")
    elif command=='factorial recursive':
        print('Введите число')
        i=int(input())
        try:
            print(factorial_recursive(i))
        except Exception as e:
            logger.error(f"Ошибка:{e}")
    elif command == "factorial not recursive":
        print('Введите число')
        i=int(input())
        try:
            print(factorial(i))
        except Exception as e:
            logger.error(f"Ошибка:{e}")
    elif command == "sort":
        print("Выберите что хотите сортировать строки или числа")
        command2=input()
        if command2=="числа":
            print("Введите массив чисел")
            massive=list(map(int,input().split()))
            massive2=list(map(float,input().split()))
            print('Введите тип сортировки')
            command3=input()
            if command3=='bubble':
                try:
                    print(bubble_sort(massive))
                except Exception as e:
                    logger.error(f"Ошибка:{e}")
            elif command3=='quick':
                try:
                    print(quick_sort(massive))
                except Exception as e:
                    logger.error(f"Ошибка:{e}")
            elif command3=='counting':
                try:
                    print(counting_sort(massive))
                except Exception as e:
                    logger.error(f"Ошибка:{e}")
            elif command3=='radix':
                try:
                    print(radix_sort(massive))
                except Exception as e:
                    logger.error(f"Ошибка:{e}")
            elif command3=='heap':
                try:
                    print(heap_sort(massive))
                except Exception as e:
                    logger.error(f"Ошибка:{e}")
            elif command3=='bucket':
                try:
                    print(bucket_sort(massive2))
                except Exception as e:
                    logger.error(f"Ошибка:{e}")
            else:
                print('Такой сортировки не существует')
        elif command2=="строки":
            print("Введите массив строк")
            massive1=list(map(str,input().split()))
            print('Введите тип сортировки')
            command3=input()
            if command3=='bubble':
                try:
                    print(bubble_sort(massive1))
                except Exception as e:
                    logger.error(f"Ошибка:{e}")
            elif command3=='quick':
                try:
                    print(quick_sort(massive1))
                except Exception as e:
                    logger.error(f"Ошибка:{e}")
            elif command3=='heap':
                try:
                    print(heap_sort(massive1))
                except Exception as e:
                    logger.error(f"Ошибка:{e}")
            else:
                print('Такой сортировки не существует или такой сортировкой нельзя сортировать строки')
        else:
            print("Выберите числа или строки")
    elif command=="stack":
        stack = Stack()
        while True:
            print("Введите метод")
            metod = input()
            if metod == 'peek':
                try:
                    print(stack.peek())
                except Exception as e:
                    logger.error(f"Ошибка:{e}")
            elif metod == 'push':
                print('Выберите, что вы хотите добавить число или строку')
                n = input()
                if n == 'число':
                    print('Введите число')
                    y = int(input())
                    try:
                        stack.push(y)
                    except Exception as e:
                        logger.error(f"Ошибка:{e}")
                elif n == "строку":
                    print('введите строку')
                    y1 = input()
                    try:
                        stack.push(y1)
                    except Exception as e:
                        logger.error(f"Ошибка:{e}")
                else:
                    print("Выберите число или строку")
            elif metod=='pop':
                try:
                    print(stack.pop())
                except Exception as e:
                    logger.error(f"Ошибка:{e}")
            elif metod=='len':
                try:
                    print(stack.__len__())
                except Exception as e:
                    logger.error(f"Ошибка:{e}")
            elif metod=='is_empty':
                try:
                    print(stack.is_empty())
                except Exception as e:
                    logger.error(f"Ошибка:{e}")
            else:
                print('такого метода не существует')
    elif command == 'queue':
        queue=Queue()
        while True:
            print('Введите метод')
            metod1=input()
            if metod1 == 'len':
                try:
                    print(queue.__len__())
                except Exception as e:
                    logger.error(f"Ошибка:{e}")
            elif metod1 == 'is_empty':
                try:
                    print(queue.is_empty())
                except Exception as e:
                    logger.error(f"Ошибка:{e}")
            elif metod1 == 'front':
                try:
                    print(queue.front())
                except Exception as e:
                    logger.error(f"Ошибка:{e}")
            elif metod1 == 'dequeue':
                try:
                    print(queue.dequeue())
                except Exception as e:
                    logger.error(f"Ошибка:{e}")
            elif metod1=='enqueue':
                print('Выберите что хотите добавить число или строку')
                n=input()
                if n=='число':
                    print('Введите число')
                    i=int(input())
                    try:
                        queue.enqueue(i)
                    except Exception as e:
                        logger.error(f"Ошибка:{e}")
                elif n=='строку':
                    print('Введите строку')
                    i1=input()
                    try:
                        queue.enqueue(i1)
                    except Exception as e:
                        logger.error(f"Ошибка:{e}")
                else:
                    print('Введите число или строку')
    else:
        print('Такой команды не существует')
if __name__ == "__main__":
    main()


