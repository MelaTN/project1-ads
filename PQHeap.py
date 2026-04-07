## PROJECT DEL 1 ##
## Af Lasse Banke Rasmussen (lrasm24@student.sdu.dk) og Melanie Toudahl Nielsen (melni24@student.sdu.dk) ##

def createEmptyPQ() -> list:
    "Returns an empty heap."
    return []

## extractMin and minHeapify ##

def extractMin(A:list) -> float:
    "Returns and removes the minimum of the min-priority-queue A. "
    "Assumed that A is non-empty. " 

    min = A[0] # Saves the min (root)
    
    # Replaces root with the last leave
    A[0] = A[-1]
    A.pop() 

    minHeapify(A,0) # Restores heap-order
   
    return min

def minHeapify(A:list,i:int) -> None:
    "Restores heap-order under the assumption that the subtrees of node i are min-heaps."
    
    l = left(i) # The left child of node i
    r = right(i) # The right child of node i

    # Finding the smallest of node i and its children
    if l < len(A) and A[l] < A[i]:
        smallest = l
    else:
        smallest = i
    if r < len(A) and A[r] < A[smallest]:
        smallest = r
    
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i] # Exchange A[i] and A[smallest]
        minHeapify(A,smallest)


## insert  ##

def insert(A:list,e:float) -> None:
    "Inserts key e into priority-queue A and restores min-heaporder."
    A.append(e)
    i = len(A)-1
    while i > 0 and A[parent(i)] > A[i]:
        A[i], A[parent(i)] = A[parent(i)], A[i] # Exchange A[i] and A[smallest]
        i = parent(i)


## Parent and children of node i ##

def left(i:int) -> int:
    "Returns the index of the left child of node i."
    return 2*i + 1

def right(i:int) -> int:
    "Returns the index of the right child of node i."
    return 2*i + 2

def parent(i:int) -> int:
    "Returns the index of the parent of node i."
    return (i-1)//2

