import yagmail

#链接邮箱服务器
yag = yagmail.SMTP(user="1512500241@qq.com",password="wmqtqbtnmyamhfjd",host="smtp.qq.com")

#邮箱正文
contents = ["您好,Gjs自动化执行情况请查看附件"]

#邮件发送

# yag.send("1512500241@qq.com","Gjs自动化测试",contents)

yag.send("1512500241@qq.com","Gjs自动化测试",contents,r"D:\Project\TestCase\Gjs_Po\report\2019-10-19 17_00_04report_test.html")
