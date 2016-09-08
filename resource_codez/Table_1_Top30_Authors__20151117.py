
#########table1 top 30 authors @ 20151117
import pandas

leaderinfo = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_引用量变化_Citation_20151105/Paper_Author_DOI_Year_Tag_20151105V1Ranked.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')
output = open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_统计分析_Statistical_Analysis_20151119/Result.csv', 'w')

#Initializing
Len = len(leaderinfo)
Rank = 1
Pub = 0
Citation = 0
	
#Citation Analysis
for i in range(0,1605):
	if leaderinfo.Rank_V1[i] == Rank:
		Pub += 1
		Citation += leaderinfo.Citation_WOS[i]
	else:
		print(Rank,leaderinfo.Citation_Full_Name[i-1],Pub,Citation,leaderinfo.Citation_Score[i-1],leaderinfo.Leaderrank_Score_V1[i-1])
		Pub = 1
		Citation = leaderinfo.Citation_WOS[i]
		Rank = leaderinfo.Rank_V1[i]

#All authors rank for average
import pandas

leaderinfo = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_引用量变化_Citation_20151105/Paper_Author_DOI_Year_Tag_20151105V1Ranked.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')
output = open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_统计分析_Statistical_Analysis_20151119/Allrank.txt', 'w')

#Initializing
Len = len(leaderinfo)
Rank = 1
Pub = 0
Citation = 0
	
#Citation Analysis
for i in range(0,Len):
	if leaderinfo.Rank_V1[i] == Rank:
		Pub += 1
		Citation += leaderinfo.Citation_WOS[i]
	else:
		print(Rank,Pub,Citation,leaderinfo.Citation_Score[i-1],leaderinfo.Leaderrank_Score_V1[i-1], file = output)
		Pub = 1
		Citation = leaderinfo.Citation_WOS[i]
		Rank = leaderinfo.Rank_V1[i]
print(Rank,Pub,Citation,leaderinfo.Citation_Score[i],leaderinfo.Leaderrank_Score_V1[i], file = output)
output.close()