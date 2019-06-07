#############################################################################
#############################################################################
#Paper_Year_Count & Site_Year_Count @ 20151015
import pandas
import collections
import pylab as pl

#Use dtype to turn float into str
data = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Data_文献元数据_CitationData_20150921/4093_fluxANDeddyVer/Author_DOI_Convension_Titled.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')
siteinfo = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Data_台站网页信息_HtmData_2014/ThreeNetworks_Table_151016_YearCount.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')

output = open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Data_文献元数据_CitationData_20150921/4093_fluxANDeddyVer/Result.txt', 'w')


for i in range(0,912):
	if siteinfo.Data_Availability_F[i] == 'NA':
		siteinfo.Data_Availability_F[i] = siteinfo.Data_Availability_A[i]

#save to csv files
siteinfo.to_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Data_台站网页信息_HtmData_2014/ThreeNetworks_Table_151016_YearCount_Pcal.csv")



ycount = collections.Counter(data.Year)
pub = []

#data.append for array connection & Data preparation
for i in range(1982,2016):
	pub.append(ycount[i])
year=range(1982,2016)

#Figure initialization and double Y settings
fig,Pfig = pl.subplots()
Sfig = Pfig.twinx()

#Draw Figure
Fone = Pfig.hist(data.Year,bins = 34, label='Publication')
#Fone = Pfig.bar(year, data, label='Publication')
Ftwo = Sfig.plot(year, data.sites, label='Site counts')

#Label settings and Title
Pfig.set_xlabel('Year', fontsize=15)
Pfig.set_ylabel('Papers per Year', fontsize=15)
Sfig.set_ylabel('Sites built Per Year', fontsize=15)
pl.title('Publications per Year in Flux Study Area', fontsize=18)
pl.legend(loc='best')

############publication hist bar only#################
fig,Pfig = pl.subplots()
Fone = Pfig.hist(data.Year,bins = 34, label='Publication')
Pfig.set_xlabel('Year', fontsize=15)
Pfig.set_ylabel('Annual publications', fontsize=15)
#pl.title('Publication per Year in Flux Study Area', fontsize=18)
pl.legend(loc='best')
pl.show()

