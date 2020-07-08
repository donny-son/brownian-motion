import numpy

class BrownianMotion:

    def __init__(self, n_times):
        self.n_times = n_times
        self.array = numpy.empty([self.n_times,4])
        self.time = 0
        self.res = 0
        self.x = 0
        self.y = 0
        self.array

    def result(self):
        for i in range(self.n_times):
            if i == 0:
                self.array[i,] = self.time, self.res, self.x, self.y
                continue
            self.time = i
            self.res = numpy.random.binomial(1,0.5)
            if self.res == 1:
                self.x += 1
                self.y += 1

            else:
                self.x += 1
                self.y -= 1

            self.array[i,] = self.time, self.res, self.x, self.y

        return self.array


if __name__ == '__main__':
    res = BrownianMotion(1000).result()
    print(res)