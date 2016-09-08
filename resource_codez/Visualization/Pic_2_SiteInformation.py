
#########SiteInfo Transformation @ 20151016
import pandas
import collections
import pylab as pl
siteinfo = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Data_台站网页信息_HtmData_2014/ThreeNetworks_Table_151016_YearCount_Pcal.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')
StartDate = {}
EndDate = {}

counter = collections.Counter(siteinfo.Zone_ID)
#Initializing
for w in counter:
	StartDate[w] = 9999
	EndDate[w] = 0

for i in range(0,833):
	tag = siteinfo.Zone_ID[i]
	if siteinfo.Start[i] == '' or siteinfo.End[i] == '':
		continue
	if StartDate[tag] > int(siteinfo.Start[i]):
		StartDate[tag] = int(siteinfo.Start[i])
	if EndDate[tag] < int(siteinfo.End[i]):
		EndDate[tag] = int(siteinfo.End[i])	

for w in counter:
	print(w,'|',counter[w],StartDate[w],EndDate[w])

pl.show()
output.close()