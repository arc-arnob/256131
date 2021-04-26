# hackerrank.com/challenges/find-second-maximum-number-in-a-list/submissions/code/132872274
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    n_arr = list(arr)
    n_arr.sort(reverse = True)
    #print(n_arr)
    high = n_arr[0]
    find = 0
    for i in range(1,len(n_arr)):
        if n_arr[i]<high:
            high = n_arr[i]
            break
    print(high)