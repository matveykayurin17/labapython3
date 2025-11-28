from typing import TypeVar
strandint=TypeVar('strandint',str,int)

def bubble_sort(a:list[strandint])->list[strandint]:
    """На вход функции подаётся список, содержащий целые числа или строки. Функция возвращает отсортированный по возрастанию массив при помощи пузырькового метода"""
    if not a:
        return []
    for j in range(len(a)):
        for i in range(1, len(a)):
            if a[i - 1] > a[i]:
                n = a[i]
                a[i] = a[i - 1]
                a[i - 1] = n
    return a
strandint1=TypeVar('strandint1',str,int)
def quick_sort(a:list[strandint1])->list[strandint1]:
    """На вход функции подаётся список, содержащий целые числа или строки. Функция возвращает отсортированный по возрастанию массив при помощи быстрой сортировки"""
    if not a:
        return []
    else:
        pivot = a[-1]
        sp1 = []
        sp2 = []
        sp3=[]
        for i in a:
            if i < pivot:
                sp1.append(i)
            elif i>pivot:
                sp2.append(i)
            else:
                sp3.append(i)
        return quick_sort(sp1)+sp3+quick_sort(sp2)

def counting_sort(a:list[int])->list[int]:
    """На вход функции подаётся список, содержащий целые числа. Функция возвращает отсортированный по возрастанию массив при помощи count метода"""
    if not a:
        return []
    maxi=max(a)
    mini=min(a)
    distance=maxi-mini+1
    count=[0]*distance
    sp=[0]*len(a)
    for i in range(len(a)):
        count[a[i]-mini]+=1
    for i in range(1,len(count)):
        count[i]+=count[i-1]
    for i in range(len(a)-1,-1,-1):
        sp[count[a[i]-mini]-1]=a[i]
        count[a[i]-mini]-=1
    return sp

def radix_sort(a:list[int],base:int=10)->list[int]:
    """На вход функции система исчисления и подаётся список, содержащий целые числа и система счисления. Функция возвращает отсортированный по возрастанию массив при помощи поразрядной сортировки"""
    if not a:
        return []
    maxi=max([len(str(x)) for x in a])
    sp:list[list[int]]=[[] for _ in range(base)]
    for i in range(0,maxi):
        for x in a:
            digit=(x//base ** i)%base
            sp[digit].append(x)
        a=[x for i in sp for x in i]
        sp = [[] for _ in range(len(a))]
    return a
strandint2=TypeVar('strandint2',str,int)
def heap_sort(a:list[strandint2])->list[strandint2]:
    "На вход функции подаётся список содержащий строки или целые числа, функция возвращает отсортированный по возрастанию массив при помощи метода куч"
    if not a:
        return []
    def heapy(a:list[strandint2],n:int,i:int)->None:
        largest=i
        l1=2*i+1
        r=2*i+2
        if l1<n and a[i]<a[l1]:
            largest=l1
        if r<n and a[largest]<a[r]:
            largest=r
        if largest!=i:
            a[i],a[largest]=a[largest],a[i]
    n=len(a)
    for i in range(n,-1,-1):
        heapy(a,n,i)
    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapy(a, i, 0)
    return a

def bucket_sort(a:list[float],bucket:int|None=None)->list[float]:
    "Функция принимает на вход список с вещественными числами и количество так называемых коробок(количество может быть и не указана). Функция возвращает массив отсортированный по возрастанию при помощи карманного метода"
    if not a:
        return []
    if bucket is None:
        bucket=len(a)
    buckets:list[list[float]]=[[] for _ in range(bucket)]
    for i in range(len(a)):
        bi=int(bucket*(a[i]+10)/20)
        buckets[bi].append(a[i])
    while [] in buckets:
        buckets.remove([])
    for sp in buckets:
        for j in range(len(sp)):
            for i in range(1, len(sp)):
                if sp[i - 1] > sp[i]:
                    n = sp[i]
                    sp[i] = sp[i - 1]
                    sp[i - 1] = n
    sp1:list[float]=[]
    for u in buckets:
        for i in range(len(u)):
            sp1.append(u[i])
    return sp1
