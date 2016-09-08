
#########Universal Name Transformation @ 20151024
import pandas
import collections

nameinfo = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_姓名统一化_UniversalName_20151023/PaperAuthor_Name_Universal_Transform_20151024_v3.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')
output = open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_姓名统一化_UniversalName_20151023/Result.csv', 'w')

#Initializing
Len = len(nameinfo)
Uniqkey = 1

#Empty value handling
#	if nameinfo.Slong[i] == '':
#		nameinfo.Slong[i] = nameinfo.Flong[i].split(' ')[1]
#		nameinfo.Flong[i] = nameinfo.Flong[i].split(' ')[0]

#Name Comparison
for i in range(1,Len):
	if ((nameinfo.Full_Name_Second[i][0] == nameinfo.Full_Name_Second[i-1][0]) and (float(nameinfo.Full_Name_Sim[i]) > 90)) or (float(nameinfo.Short_Name_Sim[i]) == 100):
		print(Uniqkey, file = output)
	else:
		Uniqkey += 1
		print(Uniqkey, file = output)

output.close()

#########Universal Name Transformation 2nd Transformation
nameinfo = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_姓名统一化_UniversalName_20151023/PaperAuthor_Name_Universal_Transform_20151024_2ndresult.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')
output = open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_姓名统一化_UniversalName_20151023/Result.csv', 'w')

#Initializing
Len = len(nameinfo)

#Name Comparison & TAG1
for i in range(1,Len):
	if (nameinfo.Full_Name_Universal[i-1] in nameinfo.Full_Name_Universal[i]) and (nameinfo.Unique_Author_Number[i-1] != nameinfo.Unique_Author_Number[i]):
		print('*', file = output)
	else:
		print('', file = output)
		
#TAG1 Correction
output = open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_姓名统一化_UniversalName_20151023/Result.csv', 'w')
Key = 1
for i in range(1,Len):
	if nameinfo.TAG1[i] == '*':
		print(Key, file = output)
	else:
		if nameinfo.Unique_Author_Number[i] == nameinfo.Unique_Author_Number[i-1]:
			print(Key, file = output)
		else:
			Key += 1
			print(Key, file = output)

output.close()

#########Site Name Search in Universal Names of Papers
import difflib as dif
import pandas
import collections

nameinfo = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_姓名统一化_UniversalName_20151023/PaperAuthor_Name_Universal_Transform_20151025_Result.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')

siteinfo = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_姓名统一化_UniversalName_20151023/ThreeNetworks_NameList_151025.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')

output = open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_姓名统一化_UniversalName_20151023/Result.txt', 'w')

def Get_Match(x,y):
	return dif.SequenceMatcher(None,x,y).quick_ratio()

#Initializing
Lenn = len(nameinfo)
Lens = len(siteinfo)
temp = ''

for i in range(0,Lens):
	temp = siteinfo.Universal_Site_Author[i] + '__'
	sshort = siteinfo.Site_Author_First[i] + ',' + siteinfo.Site_Author_Second[i][0]
	fshort = siteinfo.Site_Author_Second[i] + ',' + siteinfo.Site_Author_First[i][0]
	
	for j in range(0,Lenn):
		if (Get_Match(nameinfo.Full_Name_Universal[j],siteinfo.Universal_Site_Author[i]) > 0.9) or (Get_Match(nameinfo.Short_Name_Universal[j],siteinfo.Universal_Site_Author[i]) > 0.9) or (Get_Match(nameinfo.Full_Name_Universal[j],sshort) > 0.95) or (Get_Match(nameinfo.Full_Name_Universal[j],fshort) > 0.95):
			temp += str(nameinfo.Ukey[j]) + '|'
	print(temp)
	print(temp, file = output)

	
output.close()

#########Nameinfo Self-transformation
import difflib as dif
import pandas
import collections

nameinfo = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_姓名统一化_UniversalName_20151023/PaperAuthor_Name_Universal_Transform_20151027_Result.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')

output = open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_姓名统一化_UniversalName_20151023/Result.txt', 'w')

def Get_Match(x,y):
	return dif.SequenceMatcher(None,x,y).quick_ratio()

#Initializing
Lenn = len(nameinfo)

for i in range(0,Lenn):
	temp = ''
	for j in range(i,Lenn):
		if (Get_Match(nameinfo.Full_Name_Universal[i],nameinfo.Full_Name_Universal[j]) > 0.95):
			temp += str(nameinfo.Ukey[j]) + '|'
	print(temp)
	print(temp, file = output)
output.close()

#Accuracy detection
for i in range(0,Lenn):
	temp=''
	for w in nameinfo.Self_Trans[i].split('|'):
		if w == '':
			break
		if nameinfo.UAN2[int(w)-1] != nameinfo.UAN2[i]:
			print(i,'#########')
			#temp += str(nameinfo.UAN2[i]) + '<=' + str(nameinfo.UAN2[int(w)-1]) + ' && ' + nameinfo.Full_Name_Original[i] + '<-->' + nameinfo.Full_Name_Original[int(w)-1] + ' | '
			temp += str(nameinfo.UAN2[i]) + ',' + str(nameinfo.UAN2[int(w)-1]) + '|'
		else:
			print(i)
	print(temp,file = output)
output.close()

#Name correction based on Rule
Rule = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_姓名统一化_UniversalName_20151023/Rule_Nameinfo.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')

output = open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_姓名统一化_UniversalName_20151023/Result.txt', 'w')

LenR = len(Rule)
UAN3 = nameinfo.UAN2

for i in range(0,LenR):
	for j in (0,Lenn-1):
		print(i)
		if Rule.From[i] == UAN3[j]:
			UAN3[j] = Rule.To[i]
			print(i)
			
for w in UAN3:
	print(w, file = output)
output.close()






