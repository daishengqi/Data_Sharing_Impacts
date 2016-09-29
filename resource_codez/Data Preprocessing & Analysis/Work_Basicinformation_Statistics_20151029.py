
#########Basic Information Statistics
#Open Site Author Proportion
import pandas

paperinfo = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_基本信息统计_Basicinformation_Statistics_20151029/Author_DOI_Year_Tag_20151029_Result_tmp.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')

network = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_基本信息统计_Basicinformation_Statistics_20151029/ThreeNetworks_Table_1501029_Nrep_modified.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')

output = open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_全局链接_Paper_Author_SiteLink_20151027/Result.csv', 'w')

#Initializing
Lenn = len(network)
Lenp = len(paperinfo)
Counter = 0
Counterp = 1
#Debug in Oct.30th
Temp = '|'

#Total Author Counter
for i in range(1,Lenp):
	if paperinfo.UAN2_Modified[i] != paperinfo.UAN2_Modified[i-1]:
		Counterp += 1
	
#Open Sited Author Counter
for i in range(0,Lenn):
	#if 'Ameri' not in network.Network[i]:
	#	continue
	for w in network.Investigator_UAN2_Nrep[i].split('|'):
		if w != '':		
		#Debug in Oct.30th
			if ('|' + w + '|') not in Temp:
				Temp += w + '|'
				Counter += 1

print(Counter)
output.close()

################  Result  #########################
Counter = 600
CounterP= 7899
Temp = 3538|5883|7692|454|7168|1261|3078|4199|6671|6146|841|7889|7940|7951|2368|7514|7842|7230|2468|3765|1029|3756|1041|3405|5877|5880|6644|4633|5060|4851|3270|3406|7905|2363|6379|7923|3903|3012|4370|71|7303|6923|4628|217|4950|3321|5056|3538|3437|6652|6211|6602|4861|3873|1008|3593|7204|7728|5112|4260|371|7234|3609|4740|4369|6678|7648|7247|3954|4047|7631|2561|3397|2936|5884|7691|6638|3083|7270|3239|7898|5058|4386|4627|3513|7469|267|2916|1640|1100|4425|6693|3828|3914|7002|2180|3046|924|4773|3076|1376|7105|5771|7064|207|2609|1784|3353|1293|5747|2283|4985|3580|1680|7145|5920|5900|7467|1905|2270|4261|784|7423|193|7047|4059|7479|147|538|2891|3648|4397|4398|1910|2176|113|624|625|4276|340|341|167|1051|5011|850|732|1750|7794|4145|115|2036|5770|6246|7883|7864|7894|7185|6192|7959|7952|7896|996|6174|6153|7576|7853|7629|2817|7187|4115|4153|4025|6819|5518|4065|4066|4706|4575|5262|1252|2568|1631|459|2353|1931|6725|717|6334|2649|2909|2755|6471|5626|3508|1241|4271|3469|6241|4387|1306|3625|3623|6031|1533|1584|2287|6034|7386|1586|6042|3568|2932|3537|5868|5391|5087|6004|4131|6654|3706|6361|7513|6397|3072|4250|3155|4989|5325|1262|1964|862|2194|6103|99|5949|3554|5921|6138|5669|4734|4070|3723|4246|3503|7077|5634|236|4599|5720|6890|1414|921|6650|5089|4289|4104|752|4726|2383|6273|4085|1913|1607|1386|4102|4338|908|2295|589|3052|3463|2115|806|5153|5571|581|4938|6464|5680|6851|5596|5398|4844|2143|2557|321|1224|2061|2697|5135|3696|5970|3188|1320|540|3383|1933|3745|7624|5796|491|4909|2409|5211|301|4203|1510|5318|70|8045|4372|4788|2196|920|2352|1804|4868|1772|2220|4274|2175|6401|4354|7775|2145|5597|420|6124|5412|6416|1599|7788|4293|1962|803|5188|2384|6953|6142|4513|4559|4687|4596|5582|1856|6303|1208|2058|1472|4247|6665|2573|3540|3518|2991|4813|7472|6795|7269|151|888|7033|4666|137|7115|5042|1375|206|7315|2092|849|4712|3045|1525|7006|7267|2647|6053|5240|4349|1055|1571|5603|571|7382|813|2254|6024|4795|1449|7474|5084|3223|5486|6944|1045|5314|3194|5757|5411|308|5405|2217|7034|2606|7438|7771|502|7111|1992|1701|180|3158|3971|2319|3453|5870|4964|2624|7375|3655|3697|4645|3041|1210|4068|1837|6630|5074|2809|6874|7683|2622|6595|4907|133|4679|1095|4747|7420|4931|3834|4058|4446|2512|2740|6364|1628|7373|7832|1597|3750|5746|6161|2708|514|650|1897|6827|521|4534|5690|3327|1720|8036|2225|4005|5584|456|2741|5492|5237|1082|2474|638|1765|5630|5297|5277|1060|982|2329|2173|3064|3541|3343|7388|5064|5065|5014|6507|6453|5027|648|1552|3504|2603|3986|512|3774|4803|4804|2425|4939|5832|5623|4351|1752|674|1871|277|2322|5164|723|4408|5565|7322|1432|5550|1152|6746|578|6098|2449|7084|4306|2492|6748|3630|3734|4215|6560|1569|1570|728|5558|1900|5369|6099|2360|5186|7643|2318|6529|284|2560|7061|3475|4995|2122|1527|3418|6597|6100|545|4685|755|124|570|4742|105|1319|7066|6022|2945|3011|6603|761|2695|3007|188|344|2022|8017|1712|4314|3610|7190|130|4163|7118|2269|4834|1244|1598|5559|5243|1153|1189|503|3633|6054|1783|5987|3205|4539|5803|3431|176|5981|
##################################################

#Author Paper WOS Citation Analysis 20151030
import pandas

paperinfo = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_基本信息统计_Basicinformation_Statistics_20151029/Author_DOI_Year_Tag_20151030_Result_tmp.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')

isitable = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Data_文献元数据_CitationData_20150921/4093_fluxANDeddyVer/Paper_Citation_Transfer_20151030.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')

network = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_基本信息统计_Basicinformation_Statistics_20151029/ThreeNetworks_Table_1501029_Nrep_modified.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')

output = open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_基本信息统计_Basicinformation_Statistics_20151029/Result.txt', 'w')

Lenp = len(paperinfo)
Lenn = len(network)
Loc = 0

#Citation Transfer to Paperinfo
for i in range(0,Lenp):
	if paperinfo.Title_Modified[i] == isitable.Title[Loc]:
		print(isitable.Total_Times_Cited[Loc],file = output)
	else:
		Loc += 1
		print(isitable.Total_Times_Cited[Loc],file = output)

#Network_Categlory Calculation
for i in range(0,Lenn):
	print(i)
	for w in network.Investigator_UAN2_Nrep[i].split('|'):
		if w != '':
			for j in range(int(w),Lenp):
				if int(w) == paperinfo.UAN2_Modified[j]:
					if network.Network[i] not in paperinfo.Network_Tag[j]:
						paperinfo.Network_Tag[j] += network.Network[i] + '|'
				elif int(w) < paperinfo.UAN2_Modified[j]:
					break

CountCitation = [0,0,0,0]
CountAuthor = [0,0,0,0]
Temp = ['','','','']

#Average Citation Count of Three Groups (Paper Ciation Repeated)
for i in range(0,Lenp):
	Tag = paperinfo.Network_Cate[i] 
	print(i)
	if str(paperinfo.UAN2_Modified[i]) not in Temp[Tag]:
		Temp[Tag] += str(paperinfo.UAN2_Modified[i]) + '|'
		CountAuthor[Tag] += 1
	CountCitation[Tag] += paperinfo.Citation_WOS[i]
	
#Result
CountCitation: [0, 566796, 234717, 179749]
CountAuthor: [0, 7300, 428, 171]
Temp[3]: 105|113|124|130|147|167|188|277|284|340|341|344|456|503|512|514|521|538|545|570|578|624|625|638|648|650|674|723|728|755|761|982|1060|1082|1152|1153|1189|1244|1319|1432|1449|1527|1552|1569|1570|1571|1597|1598|1628|1712|1752|1765|1783|1804|1897|1900|1910|2022|2122|2173|2176|2217|2225|2269|2270|2318|2322|2360|2425|2492|2560|2603|2708|2740|2741|2891|2945|3011|3064|3327|3343|3418|3475|3504|3541|3610|3630|3633|3648|3734|3750|3774|3986|4005|4065|4066|4163|4215|4276|4306|4314|4351|4397|4398|4408|4534|4575|4685|4706|4742|4795|4803|4804|4834|4939|4995|5014|5027|5042|5064|5065|5164|5186|5237|5243|5277|5297|5369|5492|5550|5558|5559|5565|5584|5623|5630|5690|5746|5832|5900|5987|6022|6031|6054|6098|6099|6100|6161|6364|6453|6507|6529|6560|6597|6603|6746|6748|6827|7061|7066|7084|7118|7190|7322|7373|7388|7467|7643|7832|8017|8036|
Temp[2]: 70|71|99|115|133|137|151|176|180|193|206|207|217|236|267|301|308|321|371|420|454|459|491|502|540|571|581|589|717|732|752|784|803|806|813|841|849|850|862|888|908|920|921|924|996|1008|1029|1041|1045|1051|1055|1095|1100|1208|1210|1224|1241|1252|1261|1262|1293|1306|1320|1375|1376|1386|1414|1472|1510|1525|1533|1584|1586|1599|1607|1631|1640|1680|1701|1720|1750|1772|1784|1837|1856|1871|1905|1913|1931|1933|1962|1964|1992|2036|2058|2061|2092|2115|2143|2145|2175|2180|2194|2196|2220|2254|2283|2287|2295|2319|2329|2352|2353|2363|2368|2383|2384|2409|2449|2468|2474|2512|2557|2561|2568|2573|2606|2609|2622|2624|2647|2649|2695|2697|2755|2809|2817|2909|2916|2932|2936|2991|3007|3012|3041|3045|3046|3052|3072|3076|3078|3083|3155|3158|3188|3194|3205|3223|3239|3270|3321|3353|3383|3397|3405|3406|3431|3437|3453|3463|3469|3503|3508|3513|3518|3537|3538|3540|3554|3568|3580|3593|3609|3623|3625|3655|3696|3697|3706|3723|3745|3756|3765|3828|3834|3873|3903|3914|3954|3971|4025|4047|4058|4059|4068|4070|4085|4102|4104|4115|4131|4145|4153|4199|4203|4246|4247|4250|4260|4261|4271|4274|4289|4293|4338|4349|4354|4369|4370|4372|4386|4387|4425|4446|4513|4539|4559|4596|4599|4627|4628|4633|4645|4666|4679|4687|4712|4726|4734|4740|4747|4773|4788|4813|4844|4851|4861|4868|4907|4909|4931|4938|4950|4964|4985|4989|5011|5056|5058|5060|5074|5084|5087|5089|5112|5135|5153|5188|5211|5240|5262|5314|5318|5325|5391|5398|5405|5411|5412|5486|5518|5571|5582|5596|5597|5603|5626|5634|5669|5680|5720|5747|5757|5770|5771|5796|5803|5868|5870|5877|5880|5883|5884|5920|5921|5949|5970|5981|6004|6024|6034|6042|6053|6103|6124|6138|6142|6146|6153|6174|6192|6211|6241|6246|6273|6303|6334|6361|6379|6397|6401|6416|6464|6471|6595|6602|6630|6638|6644|6650|6652|6654|6665|6671|6678|6693|6725|6795|6819|6851|6874|6890|6923|6944|6953|7002|7006|7033|7034|7047|7064|7077|7105|7111|7115|7145|7168|7185|7187|7204|7230|7234|7247|7267|7269|7270|7303|7315|7375|7382|7386|7420|7423|7438|7469|7472|7474|7479|7513|7514|7576|7624|7629|7631|7648|7683|7691|7692|7728|7771|7775|7788|7794|7842|7853|7864|7883|7889|7894|7896|7898|7905|7923|7940|7951|7952|7959|8045|

#Debug
Counter = 0
Temp = ''
for i in range(0,Lenp):
	#if 'Ameri' not in network.Network[i]:
	#	continue
	if str(paperinfo.UAN2_Modified[i]) not in Temp:
		Temp += str(paperinfo.UAN2_Modified[i]) + '|'
		Counter += 1
output.close()


#Data sharing, public and private proportion in different citation Groups (Paper Ciation Repeated)
import pandas
paperinfo = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_基本信息统计_Basicinformation_Statistics_20151029/Paper_Author_DOI_Year_Tag_20151101.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')
output = open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_基本信息统计_Basicinformation_Statistics_20151029/Result.txt', 'w')
#Initialization
Lenp = len(paperinfo)
Counter = 0

for i in range(0,Lenp-1):
	if paperinfo.UAN2_Modified[i] == paperinfo.UAN2_Modified[i+1]:
		Counter += paperinfo.Citation_WOS[i]
	else:
		print(paperinfo.UAN2_Modified[i],Counter,paperinfo.Network_Cate[i],file = output)
		Counter = 0
		
print(paperinfo.UAN2_Modified[Lenp-1],paperinfo.Citation_WOS[Lenp-1],paperinfo.Network_Cate[Lenp-1],file = output)
output.close()

#DDS, PDS and SIP Counts, site-person rank and average site-person.
import pandas
network = pandas.read_csv("C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_基本信息统计_Basicinformation_Statistics_20151029/ThreeNetworks_Table_1501114.csv", sep=',', encoding='gbk', keep_default_na= False, na_values=' ')
output = open('C:/Users/XiaoX/Desktop/Project _科学合作与科学影响力/Work_基本信息统计_Basicinformation_Statistics_20151029/Result.txt', 'w')

#Initializing
Lenn = len(network)
CountPub = [0,0,0,0]
CountAuthor = ['','','']

for i in range(0,Lenn):
	for w in network.Investigator_All[i].split('|'):
		if w != '':
			type = network.Tag_Online[i]
			if w not in CountAuthor[type]:
				CountPub[type] += 1
				CountAuthor[type] += w + '|'
#Site-Person Rank for recorded person, for only those person are on rank,XD.
CountAuthor = [0 for col in range(9000)]
for i in range(0,Lenn):
	for w in network.Investigator_UAN2_Nrep[i].split('|'):
		if w != '':
			CountAuthor[int(w)] += 1

for i in range(0,9000):
	print(i,CountAuthor[i],file = output)
output.close()