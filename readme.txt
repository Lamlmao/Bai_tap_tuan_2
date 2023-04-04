Thuật toán 
1. Sinh seed : k[4] = [value,value,value,value]
2. Thuật toán dịch bit : rotl(x,k) : dịch giá trị x k lần về bên trái
3. Thuật toán random
while(true)
result  = rotl[k[0]+k[3],23]+k[0] mod 2
temp = k[1]<<17
k[2] ^= k[0]
k[3] ^= k[1]
k[1] ^= k[2]
k[0] ^= k[3]
k[2] ^= t
k[3] = rotl(k[3],45)