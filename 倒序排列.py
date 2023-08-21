import numpy as np
a=np.loadtxt(r'C:\Users\ghq\Desktop\最终gamma\671nm振幅型gamma.txt')
np.savetxt(r'C:\Users\ghq\Desktop\最终gamma\671nm振幅型gamma-1.txt',a[::-1])