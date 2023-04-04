class Xoshiro256:
    def __init__(self, seed):
        self.state = [seed & 0xFFFFFFFF for _ in range(4)]
    
    def rotl(self, x, k):
        return ((x << k%32) & 0xFFFFFFFF) | (x >> (32 - k%32))
    
    def next(self):
        result = self.rotl(self.state[0] + self.state[3], 23) + self.state[0]
        t = self.state[1] << 17
        self.state[2] ^= self.state[0]
        self.state[3] ^= self.state[1]
        self.state[1] ^= self.state[2]
        self.state[0] ^= self.state[3]
        self.state[2] ^= t
        self.state[3] = self.rotl(self.state[3], 45)
        return result
rng = Xoshiro256(12345)
text1 = ''
for i in range(100000):
    text1 += str(rng.next()%2)
with open('result.txt','w',encoding="utf-8") as text :
    text.write(text1)