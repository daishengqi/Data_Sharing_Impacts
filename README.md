# Data Sharing and Scientific Impacts in Ecology
This is the Git repository of paper "Leading scientists are more likely to share data in ecology observation", which was written for supporting better policy making in ecology data communication. This repository contains source codez on two versions of papers.
For paper version 2016, the codes of web crawler, data analysis, LeaderRank algorithm and data visualization are in resource_codez Folder. For paper version 2017, the codes are in root folder and saved in the form of jupyter notebook. Introductions below are updated to v2017.

## Datasets
* **Bibliometric Data**: A total of 5654 research papers were collected in this study. This dataset was collected using formula: `TS = ((eddy covariance OR (flux tower AND ecology)) OR (flux tower AND carbon cycling) OR (flux tower AND land atmosphere interaction) OR fluxnet OR ameriflux OR mexflux OR asiaflux OR japanflux or chinaflux or ozflux) AND (PY = 1985 - 2016)` in the form of utf-8 full record at Web of Science.

* **Webpage Data**: Webpages were fetched by Web crawler [Scrapy](https://github.com/scrapy/scrapy) and parsed by [BeautifulSoup](https://code.launchpad.net/beautifulsoup), the depth and topN (Maximum webpages that fetched on each depth) in Scrapy were set to default project settings. Root webpages for Scrapy was set to site list pages of all public flux networks. Webpages were parsed into text with the text field wanted(e.g. Site Name, Data avaliability, Investigators...) and summarized into Pandas tables.

* **Data Download**: The raw data envolved in this paper can be found at: http://pan.baidu.com/s/1jHYyl3S (For Chinese Users) and (For non-Chinese Users).

## Algorithms
* **LeaderRank**: An up-to-date PageRank-like bibliometric method which can evaluate researchers quantitatively in a specific research field by both cooperation and citation rates, invented by Li et al.(2014) and improved by Deng et al.(2015). In our study, the parameter Wig was changed to mean(sum(Wij)) to make the result more robust.

* **Duplicate Name Detection**: An algorithm that handle different name expressions of one specific author or investigator in this research, which breaks the names into two parts and evaluate respective similarities. Names with same abbreviations will be regarded as duplicates. Each researchers or investigators will be given one unique identifier to replace their multiple name expressions.

## Data Visualization
Most of the data visualization were produced by Python 2.7, package involved: pylab, pandas, collections, numpy, nltk and matplotlib. Stastics was done using both R Ver 3.1.1 and Microsoft Excel 2013. Image mosaicking was proposed by Adobe Illustrator and Photoshop.

## Contact me
You've discovered a bug or something else you want to change - excellent!

You've worked out a way to fix it – even better!

You want to tell us about it – best of all!

The easiest way to contribute is through GitHub, for more information please contact: daishengqi@hotmail.com
