
#########Information Link
#SiteID_AuthorID Link
import pandas
import collections

namelist = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_全局链接_Paper_Author_SiteLink_20151027/ThreeNetworks_NameList_151028.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')

network = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_全局链接_Paper_Author_SiteLink_20151027/ThreeNetworks_Table_150928_modified.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')

output = open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_全局链接_Paper_Author_SiteLink_20151027/Result.csv', 'w')

#Initializing
Lenname = len(namelist)
Lennetwork = len(network)
Temp = network.Investigator
for i in range(0,Lennetwork):
	Temp[i] = ''
	
	
for i in range(0,Lennetwork):
	for j in range(0,Lenname):
		if namelist.Original_Site_Author[j] in network.Investigator_All[i]:
			print('In!')
			Temp[i] += namelist.Author_Ukey_Macraft[j]

for i in range(0,Lennetwork):
	print(Temp[i], file = output)

output.close()

#AuthorID PaperID Link
import pandas
import collections

Paperinfo = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_全局链接_Paper_Author_SiteLink_20151027/Author_DOI_Year_Tag_20151028.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')

Authorinfo = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_全局链接_Paper_Author_SiteLink_20151027/PaperAuthor_Name_Universal_Transform_20151028.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')

output = open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_全局链接_Paper_Author_SiteLink_20151027/Result.csv', 'w')

Lenp = len(Paperinfo)
Lena = len(Authorinfo)
Loc = 0

for i in range(0,Lenp):
	for j in range(Loc,Lena):
		if Paperinfo.Full_Name[i].title() == Authorinfo.Full_Name_Original[j].title():
			print(Authorinfo.Ukey[j],Authorinfo.UAN2_Modified[j], file = output)
			print(i,Paperinfo.Full_Name[i])
			break
		else:
			Loc += 1
output.close()

#Investigator Ukey to UAM2
import pandas
import collections

network = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_全局链接_Paper_Author_SiteLink_20151027/ThreeNetworks_Table_150928_modified.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')

keyinfo = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_全局链接_Paper_Author_SiteLink_20151027/UKey_Info.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')

output = open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_全局链接_Paper_Author_SiteLink_20151027/Result.csv', 'w')

Lenn = len(network)

for i in range(0,Lenn):
	Temp = ''
	for w in network.Investigator_Ukey[i].split('|'):
		if w != '':
			if str(keyinfo.UAN2_Modified[int(w)-1]) not in Temp:
				Temp += str(keyinfo.UAN2_Modified[int(w)-1]) + '|'
	print(Temp)
	print(Temp, file = output)

output.close()

#Investigator UAM2 to Paper_UniqKey @151029
import pandas
import collections

network = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_全局链接_Paper_Author_SiteLink_20151027/ThreeNetworks_Table_1501029_Nrep_modified.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')

paperinfo = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_全局链接_Paper_Author_SiteLink_20151027/Author_DOI_Year_Tag_20151029_Result_tmp.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')

output = open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_全局链接_Paper_Author_SiteLink_20151027/Result.csv', 'w')

Lenn = len(network)
Lenp = len(paperinfo)

for i in range(0,Lenn):
	Temp = ''
	for w in network.Investigator_UAN2_Nrep[i].split('|'):
		if w != '':
			for j in range(int(w),Lenp):
				if int(w) == paperinfo.UAN2_Modified[j] and str(paperinfo.Paper_UniqueKey[j]) not in Temp:
					Temp += str(paperinfo.Paper_UniqueKey[j]) + '|'
	print(Temp)
	print(Temp, file = output)

output.close()




