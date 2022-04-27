red,blue = map(int, input().split())
print(min(red,blue),max(blue-min(red,blue),red-min(red,blue))//2)