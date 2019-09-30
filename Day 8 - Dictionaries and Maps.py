# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
d = dict()

for i in range(0, N):
    name, number = input().split()
    d[name] = number

for i in range(0, N):
    try:
        name = input()
        if name in d:
            print("{}={}".format(name, d[name]))
        else:
            print("Not found")
    except:
        break
//you may get runtime error at test case 1, to remove that you must use try except.