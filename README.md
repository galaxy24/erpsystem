# ERPSYSTEM
erp管理系统. 使用PyQt编写.

> 包括对报单的添加, 修改, 删除, 检索等操作;
> 支持对表单的备份;
> 支持导出功能, 目前允许导出为Excel文件.



# 配置
### 文件
         |         |
---------|---------|
init.pyw|程序入口
_mainUI.py|主窗口界面UI
mainUI.py|主窗口封装类, 实现功能
boxUI.py|信息盒封装, 拓展出添加/修改/搜索对话框
student.py|管理类

         |         |
---------|---------|
public.py|存放公共变量
version.py|版本号生成文件, 打包时生成版本号

### 平台及依赖
         |         |
---------|---------|
Python|3.4.x x86
PyQt5|Qt界面库 x86
xlwt|Excel写入模块


