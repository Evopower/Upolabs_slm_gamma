import pandas as pd
import numpy as np

# 读取Excel文件中的两列数据
filename = r'C:\Users\ghq\PycharmProjects\Upolabs_slm_gamma\671nm.xlsx'  # 输入的Excel文件名
sheet = 'Sheet1'  # Excel文件中的工作表名

# 读取数据
df = pd.read_excel(filename, sheet_name=sheet)
column1 = df.iloc[:, 0]  # 第一列数据
column2 = df.iloc[:, 1]  # 第二列数据

# 进行线性插值
x = np.linspace(min(column1), max(column1), 1024)  # 插值后的x值
y = np.interp(x, column1, column2)  # 线性插值后的y值
print(y)
# 取整
y = np.round(y)

# 创建插值后的数据DataFrame
interpolated_data = pd.DataFrame({'Column1': x, 'Column2': y})

# 将插值后的数据保存到Excel文件中
output_filename = 'output671.xlsx'  # 输出的Excel文件名
interpolated_data.to_excel(output_filename, index=False, sheet_name='Sheet1')
