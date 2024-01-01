# 自用脚本
<br/>
主要是一些经常用的一些网站的签到什么的，想用的话随便拿去用。<br/>
随缘增加新脚本<br/>


# 推送方式
支持<b><a href = "https://sct.ftqq.com/">server酱</a>和<a href = "http://www.pushplus.plus/">推送plus</a> </b>。
将推送token或者是key填入相应的字段即可。


# 部署方式

<br/>
实现每天定时执行脚本的话，有很多种方法，可自上网找部署教程：<br/>
1.最简单的就是将脚本部署在<a href="https://console.cloud.tencent.com/scf/list?rid=33&ns=default">腾讯云函数</a>上。不过现在云函数收费了😪😪 我之前写过一篇博客，描述了云函数的部署过程，可供参考
<a href ="https://blog.csdn.net/qq_51208442/article/details/128709186">点击这里</a><br/>
2.你如果拥有自己的服务器的话，可以部署在<b><a href="https://github.com/whyour/qinglong">青龙面板</a></b>上或者是<b><a href = "https://github.com/elecV2/elecV2P">elecV2P</a></b>上，作者都在使用的两个工具，推荐青龙面板，比较好操作。<br/>
3.放在GitHub Action上面，这个稍微麻烦一点，而且GitHub抵制 GitHub Action的滥用，不推荐<br/>
4.还有很多种方法，可自行上网查询。<br/>

# 🚀🚀附青龙使用教程：
因为本仓库的脚本没有添加环境变量等设置，所以需要手动到青龙添加脚本，很简单。
示例（以阿里云盘aliyun.py为例）：
脚本管理→新建脚本→文件名：aliyun.py → 复制本仓库aliyun.py的代码到你在青龙创建的脚本中，并在其中填入你的refresh_token和推送方式的key并且保存
→定时任务→新建任务→名称随意，命令：task aliyun.py 定时规则自己决定。→大功告成


## 有问题的话，请提issue。
 
