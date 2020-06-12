import pdfkit,os
from urllib import parse
directory = os.getcwd()
#安装pdfkit
#pip install pdfkit
#install wkhtmltopdf
#https://wkhtmltopdf.org/downloads.html

# listTemp 为列表 平均每份列表的的个数n
def func(listTemp, n):
    for i in range(0, len(listTemp), n):
        yield listTemp[i:i + n]

total_page = 3  #需要修改的对应last_page+1

url_list = []  #所有页面的url
for p in range(1, total_page):
#==============================================需要黏贴的
    params = {
        'id': '192568',
        'extra_path': '',
        'page': p,
        'per_page': '12',
        'total': '14',
        'filter': '',
        'sort': 'newest',
        'base_url': '/gratiahuang/likes/',
        'auto_scroll': 'true',
        'last_page': '2',
        '$container': '.results-container',
        'source': '/ajax/user/likes'
    }
#==============================================	
    url_data = parse.urlencode(params)    #encoder URL
    url = 'https://www.thingiverse.com/ajax/user/likes?' + url_data    #生成URL
    url_list.append(url)
# print(len(url_list))
temp = func(url_list,100)
page = 0   #生成的pdf编号
for t in temp:
    # print(t)
    config = pdfkit.configuration(wkhtmltopdf='D:/Anaconda3/wkhtmltopdf/bin/wkhtmltopdf.exe')   #wkhtmltopdf的安装位置
    options = {'load-error-handling':'ignore'}   #网络问题导致的下载失败选项，option设置成忽略，默认abort
    try:
        pdfkit.from_url(t, directory+'/test_thinkgives_likes_{}.pdf'.format(page), configuration=config,options=options)
    except OSError as e:  #抛出异常到error文件，内包含没有下载成功的URL
        print(e)
        with open(directory+'/error.txt','a+') as f:
            f.write(str(e)+'\n')
    page = page+1


#error.txt里的url可以自己复制到python里，重新建立一个列表，扔给pdfkit下载