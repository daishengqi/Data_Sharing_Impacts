#############################################################################
#############################################################################
#Author DOI conversion @ 20151011
import csv
reader = csv.reader(open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Data_文献元数据_CitationData_20150921/4093_fluxANDeddyVer/Author_DOI_Convension_Notitle.csv', 'r'))
output = open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Data_文献元数据_CitationData_20150921/4093_fluxANDeddyVer/Result.csv', 'w')

for line in reader:
    counter=0
    for w in line[1].split('|'):
        counter+=1
        print(w,'|',line[2],'|',line[5],'|',counter, file = output)

csvfile.close()
output.close()


#First Authro & Corresponding Author Tag @ 20151011
import csv
reader = csv.reader(open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Data_文献元数据_CitationData_20150921/4093_fluxANDeddyVer/Running.csv', 'r'))
output = open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Data_文献元数据_CitationData_20150921/4093_fluxANDeddyVer/Result.csv', 'w')

counter=0
for line in reader:
    print(int(line[4])==1,int(line[4])<=counter, file = output)
	counter=int(line[4])

csvfile.close()
output.close()

#############################################################################
#############################################################################
#Author DOI conversion @ 20151012
import csv
reader = csv.reader(open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Data_文献元数据_CitationData_20150921/4093_fluxANDeddyVer/Author_DOI_Convension_Notitle.csv', 'r'))
output = open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Data_文献元数据_CitationData_20150921/4093_fluxANDeddyVer/Result.txt', 'w')

for line in reader:
    counter=0
    for w in line[3].split('|'):
        counter+=1
        print(w,'|',line[0],'|',line[1],'|',line[4],'|',line[7],'|',line[10],'|',counter, file = output)

#csvfile.close()
output.close()


#############################################################################
#############################################################################
#Paper Citation Calculation @ 20151012
import csv
import pandas
reader = csv.reader(open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Data_文献元数据_CitationData_20150921/4093_fluxANDeddyVer/Paper_Citation_Table_Fixed1309_RdyData_20151012.csv', 'r'))

#Use dtype to turn float into str
data = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Data_文献元数据_CitationData_20150921/4093_fluxANDeddyVer/Paper_Citation_Table_Fixed_Titled1309_RdyData_20151013.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ',dtype={'Cited': str})

output = open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Data_文献元数据_CitationData_20150921/4093_fluxANDeddyVer/Result.txt', 'w')


for line in reader:
	#No \n use end='' in print()
	print(line[0], '|', line[2],'|', line[3], end='', file = output)
	print(line[0])
	#If DOI is empty, try Name and Mag instead
	if line[2]!=line[2]:
		for i in range(0,4092):
			if (data.Cited[i].count(line[2])>0):
				print('|', data.UniqueKey[i], end='', file = output)
	else:
	#search DOI in Cite_Me_As
		for i in range(0,4092):
			if (data.Cited[i].count(line[3])>0):
				print('|', data.UniqueKey[i], end='', file = output)
	print('|END', file = output)
	
#csvfile.close()
output.close()