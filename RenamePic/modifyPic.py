import os

url = 'C:/Users/Administrator/Desktop/员工名牌/2018年证件照/'
# with open(url, 'rb') as f:
#     print(f)

# 这样子获取文件夹下面的文件，返回的是一个数组
files = os.listdir(url)

for f in files:
    try:
        os.rename(url+f, url + str(files.index(f)+1)+'.jpg')
    except OSError as err:
        print(f + '重命名失败！！！', err)
    else:
        print(f + '成功修改为：' + str(files.index(f)+1)+'.jpg')
