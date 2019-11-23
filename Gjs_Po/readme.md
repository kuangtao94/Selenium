Selenium 自动化测试框架设计的实现思路
    1.构造版本的po设计模式 --基本方法
    2.对单元测试框架中的测试固件分离
    3.对测试用例中的测试数据进行分离
    4.增加截图功能，保证每个用例在执行时pass failed保存本地
    5.引入logging日志来跟踪记录我们整个自动化测试过程
    6.runallcase.py 总执行文件的实现
    7.引入邮件的发送测试报告
    8.整合CI(jenkins)持续集成
        jenkins安装
        双击Jenkins安装，一路next到最后
        安装完自动弹出 http://localhost:8080
        推荐插件 -->建议把推荐插件都安装
        jenkins + allure 生成可视化测试报告