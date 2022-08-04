class RecentCounter:

    def __init__(self):
        self.vec = [0 for _ in range(10005)]
        self.slowIndex, self.fastIndex = 0, 0
        # self.nums = []
        # self.sz = 0

    def ping(self, t: int) -> int:
        self.vec[self.fastIndex] = t
        self.fastIndex += 1
        while self.vec[self.slowIndex] < t - 3000:
            self.slowIndex += 1
        return self.fastIndex - self.slowIndex;
        # self.nums.append(t)
        # self.sz += 1
        # while self.sz and self.nums[0] < t - 3000:
        #     del self.nums[0]
        #     self.sz -= 1
        # return self.sz


r = RecentCounter()
# ["RecentCounter","ping","ping","ping","ping"],[[],[1],[100],[3001],[3002]]
print(r.ping(1))
print(r.ping(100))
print(r.ping(3001))
print(r.ping(3002))
