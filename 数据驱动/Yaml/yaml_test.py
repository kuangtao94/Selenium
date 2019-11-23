import yaml

#yaml简介 https://www.ibm.com/developerworks/cn/xml/x-cn-yamlintro/index.html

#安装:pip install yaml

#读取yaml的值
yamlindex = open('example.yaml','r',encoding='utf-8')
#把文件内容读取出来
data = yaml.load(yamlindex)

#读取student1 name
s1 = data['student1']['name']
s2 = data['student2']['name']
s3 = data['student3']['name']
print('读取student下面的name值:',s1)
print('读取student下面的name值:',s2)
print('读取student下面的name值:',s3)