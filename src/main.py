from src.fiboandfasctori import fibo, fibo_recursive, factorial, factorial_recursive
from src.sort import bubble_sort,quick_sort,counting_sort,radix_sort,heap_sort,bucket_sort
from src.stack import Stack

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
        print(fibo_recursive(i))
    elif command=='fibbonachi not recursive':
        print('Введите число')
        i=int(input())
        print(fibo(i))
    elif command=='factorial recursive':
        print('Введите число')
        i=int(input())
        print(factorial_recursive(i))
    elif command == "factorial not recursive":
        print('Введите число')
        i=int(input())
        print(factorial(i))
    elif command == "sort":
        print("Выберите что хотите сортировать строки или числа")
        command2=input()
        if command2=="числа":
            print("Введите массив чисел")
            massive=list(map(int,input().split()))
            print('Введите тип сортировки')
            command3=input()
            if command3=='bubble':
                print(bubble_sort(massive))
            elif command3=='quick':
                print(quick_sort(massive))
            elif command3=='counting':
                print(counting_sort(massive))
            elif command3=='radix':
                print(radix_sort(massive))
            elif command3=='heap':
                print(heap_sort(massive))
            elif command3=='bucket':
                print(bucket_sort(massive))
            else:
                print('Такой сортировки не существует')
        elif command2=="строки":
            print("Введите массив строк")
            massive1=list(map(str,input().split()))
            print('Введите тип сортировки')
            command3=input()
            if command3=='bubble':
                print(bubble_sort(massive1))
            elif command3=='quick':
                print(quick_sort(massive1))
            elif command3=='heap':
                print(heap_sort(massive1))
            else:
                print('Такой сортировки не существует или такой сортировкой нельзя сортировать строки')
        else:
            print("Выберите числа или строки")
    if command=="stack":
        while True:
            print("Введите метод")
            metod = input()
            stack = Stack()
            if metod == 'peek':
                print(stack.peek())
            elif metod == 'push':
                print('Выберите, что вы хотите добавить число или строку')
                n = input()
                if n == 'число':
                    print('Введите число')
                    y = int(input())
                    stack.push(y)
                elif n == "строку":
                    print('введите строку')
                    y1 = input()
                    stack.push(y1)
                else:
                    print("Выберите число или строку")
if __name__ == "__main__":
    main()
