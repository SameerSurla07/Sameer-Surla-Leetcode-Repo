class Solution:

    def findTheWinner(self, n: int, k: int) -> int:
        l = []
        for i in range(1, n + 1):
            l.append(i)
        start_index = 0
        return self.lose(l, k, start_index)[0]


    def lose(self, l , k , start_index):
        if len(l) == 1:
            return l

        start_index  = (start_index + k - 1) % len(l)
        l.pop(start_index) 

        return self.lose( l, k , start_index) 

    

            