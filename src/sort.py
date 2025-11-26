def bubble_sort(a:list[int|str])->list[int|str]:
    """На вход функции подаётся список, содержащий целые числа. Функция возвращает отсортированный по возрастанию массив при помощи пузырькового метода"""
    if not a:
        return []
    for j in range(len(a)):
        for i in range(1, len(a)):
            if a[i - 1] > a[i]:
                n = a[i]
                a[i] = a[i - 1]
                a[i - 1] = n
    return a

def quick_sort(a:list[int|str])->list[int|str]:
    """На вход функции подаётся список, содержащий целые числа. Функция возвращает отсортированный по возрастанию массив при помощи быстрой сортировки"""
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
    """На вход функции подаётся список, содержащий целые числа. Функция возвращает отсортированный по возрастанию массив при помощи поразрядной сортировки"""
    if not a:
        return []
    maxi=max([len(str(x)) for x in a])
    sp=[[] for _ in range(base)]
    for i in range(0,maxi):
        for x in a:
            digit=(x//base ** i)%base
            sp[digit].append(x)
        a=[x for i in sp for x in i]
        sp = [[] for _ in range(len(a))]
    return a

def heap_sort(a:list[int|str])->list[int|str]:
    if not a:
        return []
    def heapy(a:list[int|str],n:int,i:int)->None:
        largest=i
        l=2*i+1
        r=2*i+2
        if l<n and a[i]<a[l]:
            largest=l
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
    def sort_bucket(a:list[int])->None:
        for i in range(1,len(a)):
            n=a[i]
            j=i-1
            while j>=0 and a[j]>n:
                a[j+1]=a[j]
                j-=1
            a[j+1]=n
    if len(a)<2 or min(a)==max(a):
        return a
    if bucket is None:
        bucket=len(a)
    sp=[[] for _ in range(bucket)]
    for num in a:
        for i in range(len(sp)):
            sp[i].append(num)
    for i in sp:
        sort_bucket(i)
    index=0
    for bucket1 in sp:
        for num in bucket1:
            a[index]=num
            index+=1
    return a