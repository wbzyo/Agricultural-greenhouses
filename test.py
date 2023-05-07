class Solution:
    # def __init__(self, n , m ):
    #     self.n=n
    #     self.m=m
    def lastRemaining(self , n , m ):
        self.n=n
        self.m=m
        a=0
        while self.n!=1:
            for i in range(self.n):
                if i==m-1 :
                    self.n=self.n-i
                    print(self.n)
                    a=i
                    break
        print(a+1)



s=Solution()
s.lastRemaining(*eval(input()))