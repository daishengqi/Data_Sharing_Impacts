
#########Universal Citation Per Year @ 20151106
import pandas
from numpy import *

citation = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_引用量变化_Citation_20151105/PUnique_CitedList_Inner_20151106.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')
output = open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_引用量变化_Citation_20151105/Result.csv', 'w')

def MakeGraph(Cols,Rows,Initial):
	graph = [[Initial for col in range(Cols)] for row in range(Rows)]
	return graph
	
#Initializing
Lenc = len(citation)
Citetimes = MakeGraph(25,4094,0)

#Citation Analysis
for i in range(0,Lenc):
	print(i)
	for w in citation.Be_Cited_By[i].split(', '):
		if w != '':
			PaperU = int(w) - 1
			for year in range(2014,1989,-1):
				if citation.Pub_Year[PaperU] <= year:
					Citetimes[i][abs(year - 2014)] += 1
				else:
					break
					
for i in range(0,Lenc):
	print(Citetimes[i], file = output)

output.close()

#Author Citation Per Year With Formula
import pandas
from numpy import *
papercitation = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_引用量变化_Citation_20151105/PUnique_CitedList_Inner_20151106.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')
Authorinfo = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_引用量变化_Citation_20151105/Paper_Author_DOI_Year_Tag_20151105V1Ranked.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')
output = open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_引用量变化_Citation_20151105/Result.txt', 'w')

def MakeGraph(Cols,Rows,Initial):
	graph = [[Initial for col in range(Cols)] for row in range(Rows)]
	return graph
	
Authorscores = MakeGraph(27,8056,0)
Lenp = len(papercitation)
Lena = len(Authorinfo)

#Man-craft year change from (2015 to 1990)
for i in range(0,Lena):
	if Authorinfo.Authority_Rank[i] == 1:
		Authorscores[Authorinfo.UAN2_Modified[i]][2016-1990] += papercitation.ICT_1990[Authorinfo.Paper_UniqueKey[i]-1]
	else:
		Authorscores[Authorinfo.UAN2_Modified[i]][2016-1990] += papercitation.ICT_1990[Authorinfo.Paper_UniqueKey[i]-1] / Authorinfo.Total_Author[i]
			
for i in range(1,8056):
	print(i,'|',Authorscores[i][1:27],file = output)
output.close()




