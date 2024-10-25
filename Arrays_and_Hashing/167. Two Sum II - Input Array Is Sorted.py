

numbers = [-5,-3,0,2,4,6,8]
target = 5


for i in range(len(numbers)):

    val = target - numbers[i] 
    print( i , val , numbers)

    for j in range( i+1 , len(numbers)+1):
        print(i ,j)

        if numbers[j-1] == val:
            print ("answer",i+1 , j+1)
            break
        if numbers[j-1] > target:
            break


