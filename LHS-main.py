# 导入所需的库
import numpy as np  # 导入numpy库，用于数学运算和处理数组
from scipy.stats import qmc  # 导入qmc模块，用于生成拉丁超立方样本
import matplotlib.pyplot as plt  # 导入matplotlib的pyplot模块，用于绘图
import pandas as pd  # 导入pandas库，用于数据处理
import openpyxl  # 导入openpyxl库，用于保存Excel文件

# 参数设置
n_samples = 2000  # 设置样本数量为2000
n_dimensions = 3  # 设置维度数量为3

# 使用scipy库的LatinHypercube生成LHS样本点
sampler = qmc.LatinHypercube(d=n_dimensions)  # 创建一个拉丁超立方采样器
lhs_samples = sampler.random(n=n_samples)  # 生成样本点

# 打印LHS样本点，这些点位于[0, 1]的超正方体中
print("LHS Samples in the unit hypercube:")
print(lhs_samples)

#--------------------------------------------------------
# 输出为一个Excel文件
columns = [f'Var{i+1}' for i in range(n_dimensions)]  # 为3个变量创建列名

# 将 numpy 数组转换为 pandas DataFrame
df0 = pd.DataFrame(lhs_samples, columns=columns)

# 要导出的Excel文件名
excel_filename = 'LHS_data.xlsx'

# 导出数据到Excel文件，使用 openpyxl 引擎
df0.to_excel(excel_filename, index=False, engine='openpyxl')

# 要导出的CSV文件名
csv_filename1 = 'LHS_data.csv'

# 导出数据到CSV文件，使用逗号分隔
df0.to_csv(csv_filename1, index=False)

#----------------------------------------------------------
# 定义一个转换函数，将超正方体中的样本点转换到实际参数空间

def transform_sample(sample, range_min, range_max):
    # 将[0, 1]范围内的样本转换到指定的[min, max]范围
    return sample * (range_max - range_min) + range_min

# 定义每个维度的参数范围##十分注意这个地方定义的最大值与最小值
range_min = [0, 0, 0.05]  # 每个维度的最小值
range_max = [1000, 1000, 0.3] # 每个维度的最大值

# 应用转换函数，将LHS样本点转换到实际参数空间
# 使用列表推导式和numpy数组来存储转换后的样本点
transformed_samples = np.array([[transform_sample(sample[dim], range_min[dim], range_max[dim])
                                 for dim in range(n_dimensions)]
                                for sample in lhs_samples])

# 打印转换后的样本点
print("LHS Samples in the original parameter space:")
print(transformed_samples)

#---------------------------------------------------------
# 输出为一个Excel文件
columns = [f'Var{i+1}' for i in range(n_dimensions)]  # 为25个变量创建列名

# 将 numpy 数组转换为 pandas DataFrame
df1 = pd.DataFrame(transformed_samples, columns=columns)

# 要导出的Excel文件名
excel_filename = 'transformed_data.xlsx'

# 导出数据到Excel文件，使用 openpyxl 引擎
df1.to_excel(excel_filename, index=False, engine='openpyxl')

# 要导出的CSV文件名
csv_filename2 = 'transformed_data.csv'

# 导出数据到CSV文件，使用逗号分隔
df1.to_csv(csv_filename2, index=False)

#-----------------------------------------------------------
# 创建第一个图形，展示初始的LHS样本点
plt.figure(figsize=(12, 10))  # 画布展开

# 第一张子图 (行0, 列0)，展示第一和第二列，即第一个NCL的坐标
plt.subplot(2, 2, 2)
plt.scatter(lhs_samples[:, 0], lhs_samples[:, 1], color='red', marker='o', label='Initial LHS Samples')
plt.title('Initial LHS Samples in the Unit Hypercube NO1')
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
plt.xlim(0, 1)
plt.ylim(0, 1)



# 自动调整子图间距
plt.tight_layout()
plt.figlegend()
plt.show()

# 创建第二个图形，展示转换后的LHS样本点
plt.figure(figsize=(12, 10))

plt.subplot(2, 2, 2)  # 放在第一象限该在的位置
plt.scatter(transformed_samples[:, 0], transformed_samples[:, 1], color='red', marker='o', label='Transformed LHS Samples')
plt.title('Transformed LHS Samples in the Original Parameter Space NO1')
plt.xlabel('Parameter x1')
plt.ylabel('Parameter x2')
plt.xlim(range_min[0], range_max[0])
plt.ylim(range_min[1], range_max[1])



# 自动调整子图间距
plt.tight_layout()
plt.legend()
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)  # 调整边距
plt.show()