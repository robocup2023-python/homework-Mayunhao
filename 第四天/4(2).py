i=1
a=int(input("input a number:"))
array=[1,5,10,15,20,25,30,35,40,45,55,60,65,70]
n=len(array)
array.append(a)
while (array[n-i]>array[n-i+1]):
    t=array[n-i+1]
    array[n-i+1]=array[n-i]
    array[n-i]=t
    i+=1
print(array)
