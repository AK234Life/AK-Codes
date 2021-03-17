def result(rem,count):
    for i,value in enumerate(num):
        if rem < value:
            if rem==1:
             return count
            elif rem==num[i-1]:
                count+=1
                return count
            else:
             rem = rem%num[i-1]
             count+=1
            return result(rem,count)
        elif rem == value:
            count+=1
            return count
        elif rem==1:
            count+=1
            return count
        def result1(rem,count):

          if rem % value == 0:
              value1 = rem // value
              return value1
          else:
              while (rem > num[11]):
                  rem = rem % num[11]
                  count += 1
              return result(rem, count)

    return result1(rem,count)
num = [1,2,4,8,16,32,64,128,256,512,1024,2048]
count = 0
t = int(input())
for i in range(t):
    rem = int(input())
    answer=result(rem,count)
    print(answer)
