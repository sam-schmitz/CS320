# dp_traceback.py
#By: Sam Schmitz and Ryan Neubauer(starter code provided by John Zelle)
#   A couple examples showing how to implement tracing back to
#   read solutions from dynamic programming algorithms.

import functools
memoize = functools.lru_cache(maxsize=None)

import sys
sys.setrecursionlimit(10000)


class CoinRow:

    def __init__(self, coins):
        self.coins = list(coins)
        self.F = memoize(self.F)

    def F(self, n):
        c = self.coins
        if n == 0:
            return 0
        if n == 1:
            return c[0]
        return max(c[n-1] + self.F(n-2), self.F(n-1))

    def solution(self):
        n = len(self.coins)
        num_coins = self.F(n)
        taken = []
        i = n
        while i > 0:
            if self.F(i) > self.F(i-1):
                taken.append(i)
                i -= 2
            else:
                i -= 1
        taken.reverse()
        return num_coins, taken


class ChangeMaking:

    def __init__(self, denoms):
        self.coinvals = denoms
        self.F = memoize(self.F)

    def F(self, n):
        if n == 0:
            return 0
        else:
            return 1 + min(self.F(n - dj)
                           for dj in self.coinvals if n >= dj)

    def solution(self, amt):
        n = len(self.coinvals)
        mincoins = self.F(amt)
        coins_used = {d: 0 for d in self.coinvals}
        while amt > 0:
            poss_prev_amts = [amt-d for d in self.coinvals if d <= amt]
            prev_amt = min(poss_prev_amts, key=self.F)
            coins_used[amt - prev_amt] += 1
            amt = prev_amt
        return coins_used

class Knapsack:

    def __init__(self, items, w):
        self.items = list(items)
        self.maxW = w
        self.F = memoize(self.F)

    def F(self, i, j):
        #print(self.items[i], j)
        if j < 0:   #if the remaining weight is less than 0 it shouldn't take that item
            return -1
        if i <= 0:  #base case if there is only one item left
            if self.items[i][0] > j:    #no room for the last item
                return -1
            return self.items[i][1] #return the last item's value
        return max(self.F(i-1, j), self.items[i][1] + self.F(i-1, j-self.items[i][0]))

    def solution(self):
        n = len(self.items) - 1
        maxVal = self.F(n, self.maxW)
        items_used = []
        weight  = self.maxW
        while n > -1:
            #print(self.items[n], self.F(n, weight), self.F(n-1, weight))
            if self.F(n, weight) != self.F(n-1, weight):    #if the value changes the item must have been used
                items_used.append(self.items[n])    #add the item to the list of used
                weight -= self.items[n][0]  #remove the weight of the item from the remaing weight
            n -= 1
        return maxVal, items_used

if __name__ == "__main__":
    ksack = Knapsack([[5, 10], [2, 1], [7, 2], [5, 5], [12, 1]], 12)
    print(ksack.solution())
