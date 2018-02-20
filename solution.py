class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        temp1 = 0
        for num in range(L,R):
            temp = str(bin(num)).split('b')[1]
            count = self.count(temp)
            if self.jugde(count):
                temp1 = temp1+1
        return temp1
    
    def count(self,s:str):
        temp = 0
        for each in s:
            if each == 1:
                temp = temp+1
        return temp
    
    def jugde(self,num:int):
        if num > 1:
            for i in range(2,num):
                if not num%i == 0:
                    continue
                else:
                    return False
            return True


