# Data Sharing and its Scientific Impacts  
This is the Git for paper "Leading scientists are more likely to share data in ecology observation" which was written for supporting better policy solution in ecology data communication. This repository contains the source codez of web crawler, data analysis, LeaderRank algorithm and data visualization used in paper, codesz are all put in their respective folders under resource_codez.

## Datasets
* **Bibliometric Data**: A total of 4274 research papers were collected in this study. This dataset was collected using formula: `TS = ((flux AND eddy covariance) OR fluxnet OR ameriflux OR asiaflux OR chinaflux OR japanflux OR euroflux OR ozflux OR mexflux) PY = (1982-2015)` in the form of utf-8 full record at Thomson Reuters Web of Science.

* **Webpage Data**: Webpages were fetched by Web crawler [Apache Nutch](https://archive.apache.org/dist/nutch/1.9/) and indexed by [Apache Solr](http://lucene.apache.org/solr/), the depth and topN (Maximum webpages that fetched on each depth) in Nutch were set to 10 and 50000 respectively. Root webpages for Nutch was set to index pages of all flux networks.

* **Data Download**: The raw data envolved in this paper can be found at: http://pan.baidu.com/s/1jHYyl3S, this cloud disk may be slow to users outside China.

## Algorithms
* **LeaderRank**: An up-to-date PageRank-like bibliometric method which can evaluate researchers quantitatively in a specific research field by both cooperation and citation rates, invented by Li et al.(2014) and improved by Deng et al.(2015). In our study, the parameter Wig was changed to mean(sum(Wij)) to make the result more robust.

* **DOM Parser**: A simple HTML DOM parser written in PHP5+ by [john_schlick]() and [me578022]() which can parse HTML or XML files into text data, source code can be found at: https://sourceforge.net/projects/simplehtmldom/.

* **Duplicate Name Detection**: An algorithm that handle different name expressions of one specific author or investigator in this research, which breaks the names into two parts and evaluate the similarities. Names with the same abbreviation will also be regarded as duplicates. Each researchers or investigators will be given one unique identifier to replace their multiple name expressions.

## Data Visualization
Most of the data visualization were produced by Python 2.7, the package involved: pylab, pandas, collections, numpy, nltk and matplotlib. Stastics was done using both R Ver 3.1.1 and Microsoft Excel 2013. Image mosaicking was done mostly by Adobe Illustrator and Photoshop.

## Contact
You've discovered a bug or something else you want to change - excellent!

You've worked out a way to fix it – even better!

You want to tell us about it – best of all!

The easiest way to contribute is through GitHub, for more information please contact: daishengqi@hotmail.com
