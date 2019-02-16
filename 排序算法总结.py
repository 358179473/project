def bubble_sort(data):
    "冒泡排序,最外层决定排序多少次"
    for i in range(len(data)-1):
        "里层决定从头到尾排序"
        flag=0
        for j in range(len(data)-i-1):
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
                flag+=1
        if flag==0:
            break
        
    return data

data=[546,56,67,789,234,5,5,657,68,6796,79780,234,23422]
print("冒泡排序后结果",bubble_sort(data))
print("最优时间复杂度是O(n)")
print("最坏时间复杂度是O(n平方)")
print("稳定\n")



def select_sort(data):
    "选择排序,最外层决定排序多少次"
    for i in range(len(data)-1):
        # 里层决定从头到尾排序（下标）
        for j in range(i+1,len(data)):
            if data[i]> data[j]:
                data[i],data[j]=data[j],data[i]
            else:
                break
            
    return data

data=[34,346,7,68,232,354,64,64,7568,80,9892,345]
print("选择排序后结果",select_sort(data))
print("最优时间复杂度是O(n平方)")
print("最坏时间复杂度是O(n平方)")
print("不稳定\n")




def insert_sort(data):
    "插入排序,和选择排序思路相似，外层排序次数"
    for i in range(1,len(data)):
        "i代表内层循环的起始位置，从右边无序部分选择第一个元素插入到左边有序部分的正确位置"
        for j in range(i,0,-1):
            "如果选择的元素比左边有序部分选择的元素小，就交换位置"
            if data[j]<data[j-1]:
                data[j],data[j-1]=data[j-1],data[j]
            else:
                break

    return data

data=[342,457,768,8,234,456,68]
print("插入排序结果是",insert_sort(data))
print("最优时间复杂度是O(n)")
print("最坏时间复杂度是O(n平方)")
print("稳定\n")



def shell_sort(data):
    "希尔排序,是在插入排序的基础上升级"
    "设置步长gap为这个集合的一半分成两部分集合"
    gap=len(data)//2
    "直到步长分到为1，也就是分到这个集合正好执行一次插入排序为至"
    while gap >=1:
        for i in range(gap,len(data)):
            """此处可以写成插入排序那样
            j=i
            while j>0:
                if data[j]<data[j-gap]:
                    data[j],data[j-gap]=data[j-gap],data[j]
                    j -= gap
                else:
                    break"""
            for j in range(i,0,-gap):
                if data[j]<data[j-gap]:
                    data[j],data[j-gap]=data[j-gap],data[j]
                else:
                    break
        gap //=2
        
    return data

data=[123,23,43,54,653,23,54,565,778,9,45,23433]
print("希尔排序后结果",shell_sort(data))
print("最优时间复杂度是O(根据gap来定，不好准确得出结论)")
print("最坏时间复杂度是O(n平方)")
print("不稳定\n")



def quick_sort(data,first,last):
    "快速排序,用递归实现，左下标大于等于右下标就不排序，当然左下标永远不可能大于右下标"
    if first>=last:
        return None
    "左下标小于右下标就排序"
    mid=data[first]
    left=first
    right=last
    
    "左右下标没有相遇的情况"
    while left<right:
        while left<right and data[right]>=mid:
            right-=1
        data[left]=data[right]
        while left<right and data[left]<mid:
            left+=1
        data[right]=data[left]
        
    "两边下标相遇的情况"
    data[left]=mid
    "左边部分快速排序"
    quick_sort(data,first,left-1)
    "右边部分快速排序"
    quick_sort(data,left+1,last)
    
    return data


data=[235,2346,34,67,87,8912,123,234,456,876,9]
print("快速排序后的结果",quick_sort(data,0,len(data)-1))
print("最优时间复杂度是O(nlog*n)")
print("最坏时间复杂度是O(n平方)")
print("不稳定\n")



def merget_sort(data):
    "归并排序,先拆分后合并"
    n=len(data)
    "列表没有元素或者是只有一个元素的情况,就不用排序"
    if n<=1:
        return data
    "列表元素不至一个的情况，找一个中间元素把列表对半拆分"
    mid=n//2
    "左边部分对半拆分"
    left_list=merget_sort(data[:mid])
    "右边部分对半拆分"
    right_list=merget_sort(data[mid:])
    "定义左边指针和右边指针初始都指向两边列表的第一个元素"
    left_p,right_p=0,0
    "定义一个存放排序后的空有序列表"
    result=[]
    "左右指针都没有指到最后位置"
    while left_p<len(left_list) and right_p < len(right_list):
        if left_list[left_p]<right_list[right_p]:
            result.append(left_list[left_p])
            left_p +=1
        else:
            result.append(right_list[right_p])
            right_p +=1
    "只要有一边指针位置没有元素了，就把另一边剩下的元素放入排序好的列表中"
    result += left_list[left_p:]
    result += right_list[right_p:]

    return result

data=[235,465,567,78,9,89,789]
print("归并排序结果",merget_sort(data))
print("最优时间复杂度是O(n*logn)")
print("最坏时间复杂度是O(n*logn)")
print("稳定")









