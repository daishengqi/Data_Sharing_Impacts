#########Country extraction @ 20151116
import pandas
import nltk
import collections

paperinfo = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_基本信息统计_Basicinformation_Statistics_20151029/4093_Unique ISI Records_1310rdRecordFixed_20151116.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')
output = open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_基本信息统计_Basicinformation_Statistics_20151029/Result.csv', 'w')

Lenp = len(paperinfo)

for i in range(0,Lenp):
	print(paperinfo.Address[i].split(' ')[len(paperinfo.Address[i].split(' '))-1], file = output)
output.close()

#Country Counter
Ccount = collections.Counter(paperinfo.Country)
for w in Ccount:
	print(w,'|',Ccount[w], file = output)
output.close()

#Citation Histogram
Citation = collections.Counter(paperinfo.Times_Cited)
for w in Citation:
	print(w,'|',Citation[w], file = output)
output.close()

#Research field coverage
testinfo = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_基本信息统计_Basicinformation_Statistics_20151029/4093_Unique ISI Records_test_20151116.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')
output = open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_基本信息统计_Basicinformation_Statistics_20151029/Result.csv', 'w')

Lent = len(testinfo)

for i in range(0,Lent):
	for w in testinfo.Research_Field[i].split('|'):
		print(w,file = output)
output.close()

countinfo = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_基本信息统计_Basicinformation_Statistics_20151029/Research_field_count_20151117.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')

Rcount = collections.Counter(countinfo.Counts)

for w in Rcount:
	print(w,'|',Rcount[w],file = output)
output.close()

#Contry counter and Paper count
import pandas
import collections
paperinfo = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_基本信息统计_Basicinformation_Statistics_20151029/4093_Unique ISI Records_1310rdRecordFixed_20151117.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')
output = open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_基本信息统计_Basicinformation_Statistics_20151029/Result.csv', 'w')

Lenp = len(paperinfo)
scale = [0]

for i in range(1,Lenp):
	if paperinfo.Publication_Year[i] != paperinfo.Publication_Year[i-1]:
		scale.append(i)

for i in range(1,len(scale)):
	colle = collections.Counter(paperinfo.Zone[scale[i-1]:scale[i]])
	print(paperinfo.Publication_Year[scale[i-1]],file = output)
	for w in colle:
		print(w,'|',colle[w],file = output)
output.close()

#Keyword extraction and rank
import pandas
import collections
paperinfo = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_基本信息统计_Basicinformation_Statistics_20151029/4093_Unique ISI Records_1310rdRecordFixed_20151117.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')
output = open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_基本信息统计_Basicinformation_Statistics_20151029/Result.csv', 'w')

Lenp = len(paperinfo)
dictionary = []

for i in range(0,Lenp):
	for w in paperinfo.Original_Keywords[i].split('|'):
		dictionary.append(w)
Dict = collections.Counter(dictionary)

for w in Dict:
	print(w,'|',Dict[w],file = output)
output.close()