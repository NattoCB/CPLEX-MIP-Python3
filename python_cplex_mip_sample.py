# simple MIP solver with IBM cplex library in Python3
# Author: Siyu Fang (i493052739) jasper.fang@qq.com
# time: 2019-Aug-03 Latest CPLEX library (go to the IBM's official website for downloading)

'''
 - 问题： (Mixed Integer Linear Programming)
	 - 公司于7个地点选址投资，令地点集合为A，每个地点i有不同的投资数额b(i)，和不同的年利润c(i)，对应下表：
		 i   1     2     3     4     5     6     7   
		 A   0     1     2     3     4     5     6  
		 b   10    8     20    5     13    22    10
		 c   11    9     29    9     21    31    22

 - 规定:
	(1) 1,2,3 这三个点属于建设区C1  公司在其中  至 多 选 两个 投资
	(2) 4,5   这两个点属于建设区C2  公司在其中  至 少 选 一个 投资
	(3) 6,7   这两个点属于建设区C3  公司在其中  至 少 选 一个 投资
	(4) 总投资 不超过 60万元

 - 目标：
	 - 最大化利润

'''

from docplex.mp.model import Model  #调用cplex solver

mdl = Model(name='a sample MIP model') # 初始化模型

A = [i for i in range(0, 7)] # 初始化 投资地点(A) 列表
X = mdl.binary_var_list(A, lb=0, name='X') # 在cplex中初始化 0-1变量X （隶属于A列表的所有地点）0-1代表投资与否
										   # lb = lower bound, ub = upper bound

# 设定目标函数
b = [10,8,20,5,13,22,10] # 各地A(i) 的 设备投资 （万元）
c = [11,9,29,9,21,31,22] # 各地A(i) 的 可获利润 （万元）
C1 = [0,1,2] # 建设区C1的index索引集
C2 = [3,4]   # 建设区C2的index索引集
C3 = [5,6]   # 建设区C3的index索引集

mdl.maximize(mdl.sum(c[i]*X[i] for i in A))  # 目标函数：最大化利润

# 添加约束条件
mdl.add_constraint(mdl.sum(X[i] for i in C1) <= 2) # 1,2,3 三个点中至多选两个
mdl.add_constraint(mdl.sum(X[i] for i in C2) >= 1) # 4,5 两个点中至少选一个	 
mdl.add_constraint(mdl.sum(X[i] for i in C3) >= 1) # 6,7 两个点中至少选一个
mdl.add_constraint(mdl.sum(b[i] * X[i] for i in A) <= 60) # 总投资<=60万

sol = mdl.solve() # 求解模型
print(sol)  # 看结果


