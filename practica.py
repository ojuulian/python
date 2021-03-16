# programa del palindromo
       
# num = input("Escribe un numero: ")

# def square_digits(num):
#     ans = ''
#     for i in str(num):
#         ans += str(int(i)**2)
#     return int(ans)
#     #print(int(ans))
    

# if __name__== '__main__' :
#     square_digits(num)


import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1331)
a, b=np.random.normal(size=2)
answers=[]
for t in range(0,100):
    answer=a*np.cos(np.pi/4*t)+b*np.sin(np.pi/4*t)
    answers.append(answer)

plt.plot(answers)
