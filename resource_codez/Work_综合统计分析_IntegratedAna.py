#########Integrated Statistical Analysis @ 20151119

import pandas
import collections
networkinfo = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_基本信息统计_Basicinformation_Statistics_20151029/ThreeNetworks_Table_1501119_Modified.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')
authorinfo = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_网络分析_Network_Analysis_20151102/Paper_Author_DOI_Year_Tag_20151105V1Ranked_Tmp.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')
output = open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_基本信息统计_Basicinformation_Statistics_20151029/Network_Tag.csv', 'w')

Lenn = len(networkinfo)
Lena = len(authorinfo)
Tag = [-1 for i in range(0,8056)]

for i in range(0,Lenn):
	for w in networkinfo.Investigator_UAN2_Nrep[i].split('|'):
		if w != '':
			Tag[int(w)] = networkinfo.Tag_Online[i]

for i in range(0,Lena):
	print(Tag[authorinfo.UAN2_Modified[i]],file = output)

output.close()

## Rank_Name_UAN_TAG
import pandas
import collections
authorinfo = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_统计分析_Statistical_Analysis_20151119/Paper_Author_DOI_Year_Tag_20151119_TAG_Ranked.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')
output = open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_统计分析_Statistical_Analysis_20151119/Rank_Network_Tag.csv', 'w')

Lena = len(authorinfo)

for i in range(1,Lena):
	if authorinfo.Rank_V1[i] != authorinfo.Rank_V1[i-1]:
		print(authorinfo.Rank_V1[i-1],'|',authorinfo.Full_Name[i-1],'|',authorinfo.UAN2_Modified[i-1],'|',authorinfo.Network_TAG[i-1], file = output)
print(authorinfo.Rank_V1[i],'|',authorinfo.Full_Name[i],'|',authorinfo.UAN2_Modified[i],'|',authorinfo.Network_TAG[i], file = output)

output.close()

##Heatmap
import pandas
import matplotlib.pyplot as plt
import numpy as np
import collections

rankinfo = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_统计分析_Statistical_Analysis_20151119/Rank_Network_Tag_20151119.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')
output = open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_统计分析_Statistical_Analysis_20151119/Tagmatrix.csv', 'w')

data = [[[0 for i in range(30)] for j in range(30)] for k in range(9)]
count = 0

for k in range(0,9):
	for i in range(29,-1,-1):
		for j in range(0,30):
			if count < 7899:
				data[k][i][j] = rankinfo.Network_TAG_Num[count]
				count+= 1


data = np.array(data)

# put the major ticks at the middle of each cell
ax0.set_xticks(np.arange(data.shape[0]), minor=False)
ax0.set_yticks(np.arange(data.shape[1]), minor=False)

# want a more natural, table-like display
ax0.invert_yaxis()
ax0.xaxis.tick_top()

fig, ((ax0,ax1,ax2),(ax3,ax4,ax5),(ax6,ax7,ax8)) = plt.subplots(3,3, sharex=True, sharey=True)

heatmap = ax0.pcolor(data[0], cmap=plt.cm.Blues)
heatmap1 = ax1.pcolor(data[1], cmap=plt.cm.Blues)
heatmap2 = ax2.pcolor(data[2], cmap=plt.cm.Blues)
heatmap3 = ax3.pcolor(data[3], cmap=plt.cm.Blues)
heatmap4 = ax4.pcolor(data[4], cmap=plt.cm.Blues)
heatmap5 = ax5.pcolor(data[5], cmap=plt.cm.Blues)
heatmap6 = ax6.pcolor(data[6], cmap=plt.cm.Blues)
heatmap7 = ax7.pcolor(data[7], cmap=plt.cm.Blues)
heatmap8 = ax8.pcolor(data[8], cmap=plt.cm.Blues)
plt.show()

#Counter
for i in range(0,8):
	print(collections.Counter(rankinfo.Network_TAG[i*900:(i+1)*900]).most_common(4))
print(collections.Counter(rankinfo.Network_TAG[7200:7899]).most_common(4))