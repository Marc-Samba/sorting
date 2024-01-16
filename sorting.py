#region
def merge(L1,L2):
    m=len(L1)
    n=len(L2)
    i=0
    j=0
    L=[]
    while i<m and j<n:
        if L1[i]<L2[j]:
            L.append(L1[i])
            i+=1
        else :
            L.append(L2[i])
            j+=1
    if i>=m:
        L=L+L2[j:]
    else :
        L+=L1[i:]

def merge_sort(L):
    if len(L)<=1:
        return(L)
    else :
        L1=L[:len(L)//2-1]
        L2=L[len(L)//2-1:]

        return(merge(merge_sortmerge_sort(L2)))
#endregion

def quick_sort(L):
    if len(L)<=1:
        return(L)
    else :
        pivot=L[0]
        L.pop(0)
        L1=[]
        L2=[]
        n=len(L)
        for i in range (n):
            if L[i]<pivot:
                L1.append(L[i])
            else:
                L2.append(L[i])

        return(quick_sort(L1)+[pivot]+quick_sort(L2))

