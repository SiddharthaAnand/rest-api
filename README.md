# REST-API to get information on Computer Science Researchers

A rest-api for obtaining information about the computer science researchers,
their co-authorship network, their list of papers, the years that they published 
those papers and many more.

## Where did the data come from ?
The data came from https://dblp.uni-trier.de/. For more information, you can 
refer to this site.

## What kind of data is available from the api ?
Publicly available data present on the aforementioned site is 
readily available from our side.

## How to get the data ?
You do not need to write crawlers to scrape data from those sites.
The hard job has been done already by us. You can simply get the
data by using our api endpoints to get information. 

## Are there any rate-limits ?
WIP

## How did you collect the data ?
In order to get the data, I used scrapy framework to collect information from
this database. It is a publicly available data and it has been scraped 
according to the robots.txt file.

## Where can we use this data ?
It can be used to create a social-network of researchers to better 
understand the communities present among them. It can be used to 
know the areas of research being done in the field of Computer Science.
It can be used to infer the different areas of research that is 
gaining traction or those areas which are slowly losing traction in 
the academic world. It can be used to find the relation between different 
areas of Computer Science fields. It can also  be used to learn about 
the strength of the relationship between authors. 

## Understanding the structure of the rest-api
It will have the following operations:
```
/api/v1/<author_name>/
```
This will return the author information based on the author name sent 
in the api endpoint. 
```
/api/v1/<author_name>/coauthors/
``` 
This will return the list of co-authors of the specified author sent 
in the api endpoint.

## Things left to do
WIP

## How to contribute ?
You can definitely help us make this api better with your suggestions,
pull requests, issues or bug-fixes. We welcome any and every suggestion 
to improve this api for all.
