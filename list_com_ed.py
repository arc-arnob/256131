#Ques: https://hackerrank-challenge-pdfs.s3.amazonaws.com/1572-list-comprehensions-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1619404525&Signature=Utat4tnWy1%2BgAGA4Vgl%2Bh5VwC%2BU%3D&response-content-disposition=inline%3B%20filename%3Dlist-comprehensions-English.pdf&response-content-type=application%2Fpdf

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    arr = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k !=n:
                    arr.append([i,j,k])
    print(arr)