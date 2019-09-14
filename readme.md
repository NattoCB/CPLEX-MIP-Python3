simple MIP solver with IBM cplex library in Python3
Author: Siyu Fang (jasper.fang@qq.com)
time: 2019-Aug-03 Latest CPLEX library (go to the IBM's official website for downloading)


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

