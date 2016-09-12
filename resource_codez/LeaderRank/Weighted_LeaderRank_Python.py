
#########Network Analysis
#Directed Graph Creation
import pandas

citationinfo = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_网络分析_Network_Analysis_20151102/PUnique_CitedList_Times_20151013.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')

output = open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_网络分析_Network_Analysis_20151102/Result.txt', 'w')

#Initializing
Lenc = len(citationinfo)
def MakeGraph(Cols,Rows,Initial):
	graph = [[Initial for col in range(Cols)] for row in range(Rows)]
	return graph

graph = MakeGraph(4094,4094,0)

for i in range(0,Lenc):
	graph[0][i+1] = i+1
	graph[i+1][0] = i+1
	for w in citationinfo.Be_Cited_By[i].split(','):
		if w != '':
			graph[i+1][int(w)] = 1

for i in range(0,Lenc+1):
	print(graph[i],file = output)

output.close()

################  Result  #########################
Directed_CNetwork_20151102.net

#Inner Citation Counts
for i in range(1,4094):
	print (sum(graph[i][1:4094]),file = output)
	

############### LeaderRank Function Definition  #########################
def InitialGraph(Graph):
	for i in range(1,len(Graph)):
		Graph[0][i] = 1 #Citation Power Change
		Graph[i][0] = 1
	return Graph
	
def MakeStochastic(Graph):
	for i in range(0,len(Graph)):
		k_out = 1 / sum(Graph[i])
		for j in range(0,len(Graph)):
			if Graph[i][j] != 0:
				Graph[i][j] = Graph[i][j] * k_out
	return Graph

#Test Run Initialization
graph = MakeGraph(7,7,0)
graph[1][2] = 1
graph[1][5] = 1
graph[2][3] = 1
graph[3][1] = 1
graph[3][4] = 1
graph[3][5] = 1
graph[4][6] = 1
graph[4][2] = 1
graph[5][2] = 1
graph[5][6] = 1
graph[5][4] = 1
graph[6][1] = 1

graph = InitialGraph(graph)
graph = MakeStochastic(graph)

score = [1 for col in range(len(graph))]
score[0] = 0
error = 10000
error_threshold = 0.0002
step =1

graph = mat(graph)
score = mat(score)

#Diffusion to stable state
while error > error_threshold:
	temp = score
	score = score * graph
	error = sum(abs(score - temp)) / sum(temp) #In case no inf appear
	print(step,error)
	step += 1
	
#Background score average 
scoreg = score[0,0] / (len(graph)-1)
score += scoreg
score[0,0] = 0


###################  Data preparation #######################
#Total Authors
import pandas
from numpy import *
import pylab as pl

paperinfo = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_网络分析_Network_Analysis_20151102/Paper_Author_DOI_Year_Tag_20151104.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')

output = open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_网络分析_Network_Analysis_20151102/Result.txt', 'w')

Lenp = len(paperinfo)
temp = paperinfo.Authority_Rank[0]
print(paperinfo.Authority_Rank[0],file = output)

#Need UAN2_Modified sorted and paper title sorted
for i in range(1,Lenp):
	if paperinfo.Authority_Rank[i] < paperinfo.Authority_Rank[i-1]:
		print(temp,file = output)
	else:
		temp = paperinfo.Authority_Rank[i]
		print(temp,file = output)
output.close()

#Citation Score Counter
citationscore = [0 for col in range(8056)]
for i in range(0,Lenp):
	if paperinfo.Authority_Rank[i] == 1:
		citationscore[paperinfo.UAN2_Modified[i]] += paperinfo.Citation_WOS[i]
	else:
		citationscore[paperinfo.UAN2_Modified[i]] += paperinfo.Citation_WOS[i] / paperinfo.Total_Author[i]
for i in range(0,Lenp):
	print(citationscore[paperinfo.UAN2_Modified[i]],file = output)
output.close()

#Co-author Counts
#Need Paper_ID sorted
def MakeGraph(Cols,Rows,Initial):
	graph = [[Initial for col in range(Cols)] for row in range(Rows)]
	return graph
	
def MakeCooperation(Authors):
	Count = 0
	List = []
	for w in Authors.split('|'):
		if w != '':
			List.append(int(w))
			Count += 1
	if Count > 1:
		Prvalue = 1 / (Count * (Count - 1))
		print(Count,Prvalue)
		for i in range(0,len(List)-1):
			for j in range(i+1,len(List)):
				col = List[i]
				row = List[j]
				#Double direction cooperation
				Graph[col][row] += Prvalue
				Graph[row][col] += Prvalue

			
paper = ['' for col in range(4094)]
for i in range(0,Lenp):
	paper[paperinfo.Paper_UniqueKey[i]] += str(paperinfo.UAN2_Modified[i]) + '|'
	
#Make Graph
Graph = MakeGraph(8056,8056,0)
for i in range(1,len(paper)):
	MakeCooperation(paper[i])
	
for i in range(0,8056):
	print(Graph[i],file = output)
output.close()

#Make Stochastic Graph
def InitialGraph(Graph):
	for i in range(1,len(Graph)):
		Graph[0][i] = citationscore[i] #Citation Power Change
		Graph[i][0] = 1                #Normal to Background node, equals to half of total data
	return Graph
	
def MakeStochastic(Graph):
	for i in range(0,len(Graph)):
		k_out = 1 / sum(Graph[i])
		print(i)
		for j in range(0,len(Graph)):
				Graph[i][j] = Graph[i][j] * k_out
	return Graph

Graph = InitialGraph(Graph)
Graph = MakeStochastic(Graph)

#Leader Rank Application
#Initialization Parameters
score = [1 for col in range(len(Graph))]
score[0] = 0
error = 10000
error_threshold = 0.0002
step =1

Graph = mat(Graph)
score = mat(score)

#Diffusion to stable state
while error > error_threshold:
	temp = score
	score = score * Graph
	error = sum(abs(score - temp)) / sum(temp) #In case no inf appear
	print(step,error)
	step += 1
	
#Background score average 
scoreg = score[0,0] / (len(Graph)-1)
score += scoreg
score[0,0] = 0

for i in range(1,8056):
    print(i,score[0,i],file = output)
output.close()

############### LeaderRank Result Combination ######################
paperinfo = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_网络分析_Network_Analysis_20151102/Paper_Author_DOI_Year_Tag_20151104.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')

leaderrank = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_网络分析_Network_Analysis_20151102/LeaerRank_20151105V1.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')

output = open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_网络分析_Network_Analysis_20151102/Result.txt', 'w')

Lenp = len(paperinfo)

for i in range(0,Lenp):
	print(leaderrank.LeaderRank_Score[paperinfo.UAN2_Modified[i]-1],file = output)
output.close()
#Final Result in Paper_Author_DOI_Year_Tag_20151105V1.csv
