Title: 什么是robots.txt  
Date: 2015-11-11 22:51   
Category: Web

John和Jason在新一期的[Robot or Not?](https://itunes.apple.com/us/podcast/robot-or-not/id997930288?mt=2)中提到了robots.txt文件。之前对这个在建站中使用的文件略有印象，记得是用来设置一些屏敝搜索引擎规则的，但具体该怎么设却没用过，于是查了一下[维基百科](https://zh.wikipedia.org/wiki/Robots.txt)，上面是这么说的：
> robots.txt（统一小写）是一种存放于网站根目录下的ASCII编码的文本文件，它通常告诉网络搜索引擎的漫游器（又称网络蜘蛛），此网站中的哪些内容是不应被搜索引擎的漫游器获取的，哪些是可以被漫游器获取的。因为一些系统中的URL是大小写敏感的，所以robots.txt的文件名应统一为小写。robots.txt应放置于网站的根目录下。如果想单独定义搜索引擎的漫游器访问子目录时的行为，那么可以将自定的设置合并到根目录下的robots.txt，或者使用robots元数据（Metadata，又稱元資料）。  

如果要禁止所有搜索机器人访问特定目录，可将文件内容设为：  
> User-agent: *  
> Disallow: /cgi-bin/  
> Disallow: /images/  
> Disallow: /tmp/  
> Disallow: /private/  

另外，如果只是想禁止访问特定文件类型，可将文件内容设为：
> User-agent: *  
> Disallow: /\*.php$  
> Disallow: /\*.js$  
> Disallow: /\*.inc$  
> Disallow: /\*.css$
  
除了robots.txt外，还可以在单个页面的HEAD中加入robots META标签让其实现与txt文件同样的功能：
> \<head>  
> \<meta name="robots" content="noindex,nofollow" />
> \</head>

如果说robots.txt具体有什么用，我想下图比较能够形象的说明  

![Pic](img/robotstxt.jpg "图片来源不详")