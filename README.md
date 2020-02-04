# StudentsManager
学生学籍管理系统. 使用PyQt编写.

> 包括对学生学籍的添加, 修改, 删除, 检索等操作;
> 支持对学籍表的备份;
> 支持导出功能, 目前允许导出为Excel文件.

学习交流使用, 禁止用于商业用途

# 配置
### 文件
         |         |
---------|---------|
init.pyw|程序入口
_mainUI.py|主窗口界面UI
mainUI.py|主窗口封装类, 实现功能
_studentBox.py|学生信息盒UI
boxUI.py|信息盒封装, 拓展出添加/修改/搜索对话框
student.py|学生类及学生管理类

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

# 使用
#### 新建档案
在主界面右下方点击"新建档案..."按钮, 弹出新建对话框, 输入新的学籍信息, 输入完毕后, 按下"新建"按钮, 完成创建

通过"菜单栏->学籍->新建档案"也可以创建档案

学生的各属性不得为空, 同时会检测学号是否重复

### 检索档案
#### 快速检索
在学籍列表上方有文本输入框, 用于对单个属性进行快速搜索

在右侧选择要检索的类型并在文本框内输入关键词, 系统会动态匹配学生信息并实时显示结果

支持同时搜索多个关键词, 用空格分隔即可

如果不输入关键词则显示所有学生信息
#### 高级检索
高级检索用于对多个属性同时进行检索

在快速搜索框右侧点击"高级搜索"按钮, 弹出高级检索对话框

在需要检索的属性下输入关键词, 输入完成后点击"搜索"按钮, 系统会匹配学生信息并显示结果

通过"菜单栏->学籍->搜索"也可以进行高级检索
#### 属性过滤
> 通过"菜单栏->视图", 可以选择要显示的学生属性

### 修改/删除档案
在列表中点击要管理的学生, 右侧信息框会显示学生信息, 在信息框下方点击"修改..."/"删除"按钮即可进行修改/删除操作

注意:学生档案一旦删除不可恢复.

### 保存/备份/导出档案表
#### 保存
菜单栏->系统->保存学籍表

每次系统关闭时会自动保存学生学籍表

学生学籍表数据会保存到程序目录下data.stu中

#### 备份
菜单栏->系统->另存学籍表

选择位置后, 会生成一份.stu文件

> 手动恢复学籍表数据:
> 关闭程序, 将备份的学籍表文件更名并替换程序目录下的data.stu文件, 启动程序即可恢复

#### 导出
为方便数据分析, 加入导出功能, 目前支持导出为Excel文件

菜单栏->系统->导出至Excel->选中档案/所有档案

选中档案即列表中的检索结果, 所有档案即导出整个学籍表

选择保存位置后会生成一份.xls文件

# TODO - 下一步要添加的功能
添加照片属性, 可以添加并显示学生的照片

增加对导出SQL文件的支持, 方便MySQL等主流数据库的导入

利用PyQt的特点, 增加对Linux系统的支持
