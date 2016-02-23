Title: 利用Python+Justcast(Dropbox)定制个人专属的播客频道  
Date: 2016-02-23 21:51   
Category: Python


本文稍微有些标题党的嫌疑。事情是这样的，由于本人一向对收听Podcast(播客)情有独钟，并从早期用喜马拉雅App过渡到使用泛用型播客客户端如[Castro](http://castro.fm)进行收听。在众多中文Podcast中，高晓松老师的‘晓松奇谈’一向是不二之选。但进入2016年后，由于高晓松老师被阿里招安，所以‘晓松奇谈’也就变成了爱奇艺的独家视频节目，在网上几乎已经找不到哪家播客服务商提供‘晓松奇谈’的节目。至于荔枝fm，虽然在网站的隐敝位置还在更新‘晓松奇谈’，但不知什么原因其iOS版却已经从AppStore下架，于是想通过荔枝fm的App听节目的愿望也泡汤。

在缺少现成资源的情况下，我决定不做伸手党，而是求教于Google大神，自己Hack一个播客频道。于是乎，我在V2EX上找到[这篇文章](https://www.v2ex.com/t/239246)。其基本实现思路是利用Python脚本，在荔枝FM上抓到原始音频文件 -> 将文件自动上传到Dropbox的文件夹 -> 利用Justcast将频道的RSS文件输出 -> 最后用手机上的泛用型播客客户端订阅即可。

说起来简单，但在参考该文章思路后，结合搜索网上各类资料，发现中间还是有些坑儿。现将相关过程(包括Python脚本的实现)记录如下：

1.需要注意，如果不具备以下条件，后面相关步骤是无法继续下去。首先你需要有：
> [Dropbox](http://dropbox.com)的账号和足够的空间
> 
> VPS空间,该VPS最好是Linux，且能够访问Dropbox.com
> 
> 基本的Python编程能力

2.接下来，你可以去[Justcast](http://justcast.herokuapp.com)上申请账号，在此过程中网站会提供相应向导，让你将dropbox账号与其关联，并进行相应的App授权。之后，在dropbox的个人文件夹中，会在Apps目录下产生一个justcast的目录，你可以在其中创建多个子目录对应不同的播客频道，并在后面Python脚本中将生成的音频文件(mp3)指定上传到相应目录下即可。

3.在Github中已经有对荔枝FM进行爬虫以获取mp3文件的[Python源代码](https://github.com/yxjxx/DownloadLizhiFMPodcast/blob/master/getPodcast.py)。我们所需要做的是在其基础上，需要添加利用Dropbox Core API接口，实现音频文件自动上传的功能。

4.为了实现Python调用Dropbox Core API，需要在Dropbox中创建一个App，并产生相应的TOKEN以用于Python脚本的连接。具体实现过程可[参考这里](http://www.ibuyopenwrt.com/index.php/8-yun-compatible/54-upload-files-to-dropbox)。

5.接下来就是编写Python脚本的过程，具体过程不再详述，原文件我放在Github上，有兴趣的同学可以[点击这里](https://github.com/kingqiu/PythonPractice/blob/master/lizhiPodcast.py)下载来用。因为只是为了实现功能，没做太多优化，大家可以凑合着用。凑合不了的自己改改也行。

6.当测试Python脚本没问题后，可将其上传到自己的VPS里，做进一步的功能验证。一旦通过，可以用crontab让Python脚本定期执行。在命令行状态下键入crontab -e，之后选择编辑器，进入到crontab编辑状态。crontab的基本语法：
> \# m h dom mon dow command
> 30 7 * * * python 'your python file name' \>\> 'your python log file name' 2>&1

具体意思我就不在这里啰嗦了，大家可以上网搜，或者[参考这里](http://blog.csdn.net/babydavic/article/details/8446886)。

7.最后，当Python脚本能够定期自动从荔枝FM下载音频，并上传到dropbox目录后，唯一所需的就是把justcast中创建的播客频道Share出来，得到一条类似http://justcast.herokuapp.com/shows/jim-qiu-chinesepodcasts/audioposts.rss的文件，在泛用型播客客户端中订阅即可。

前面提到实现过程中有几个坑，这里简单说一下：

1.国外的VPS的OS是以英文为默认，且不支持双字节文件名。因此如果所抓音频文件包含了中文字符等双字节字符，Python脚本会出错。所以首先需要设置操作系统，让OS支持文件名和文件内容为双字节，再在Python脚本中生成文件名时，利用encode()函数对将名字转换为utf8。

2.Dropbox的Core API有v1、v2两个版本，建议采用后者。Dropbox在[github](https://github.com/dropbox/dropbox-sdk-python)上提供了python sdk的使用example，可以参考一下。

3.[Justcast](http://justcast.herokuapp.com)是收费服务，其免费试用只支持发布最新的三条音频文件。如果你只是像我一样只听某个节目，且每周就一次更新，免费够用了，如果超过三个，可以考虑付费。