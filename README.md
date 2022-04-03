# wenjuanxing-auto-fill
## 说明
* 此自动填写只适合三种题型：单选题、单项填空和矩阵单选题，单项填空只能统一填同样的内容（因为懒）
## 使用前的准备工作
* 请先下载本机chrome对应版本的chromedriver.exe
* 网址输入chrome://version/查看对应版本
* 下载对应的版本https://registry.npmmirror.com/binary.html?path=chromedriver/
* 记得修改py文件中chromedriver.exe的路径为你下载对应的路径
## wjx-init.py 随机进行选择填写
* 修改chromedriver.exe的路径及问卷星问卷网址即可使用
## wjx.py 可以设置选择比例
* 修改chromedriver.exe的路径及问卷星问卷网址
* 修改提供选择比例的txt的地址
* txt使用说明——一行为一个题目，矩阵单选题的一行也算一个题目。每个题目的每个选项对应[0:100]的一个数字，代表比例，同一题的所有数字和为100，数字之间以空格区分。
* 例如
> 50 50两个选择各占50%
> 
> 100 0
> 
> 30 70
> 
> 0 100
> 
> 70 30
> 
> 填空题空着不填
> 
> 0 0 0 0 100
> 
> 0 0 0 100 0
> 
> 0 0 30 30 40
> 
> 100 0 0 0 0

![image](https://user-images.githubusercontent.com/57900078/161407743-1fd00ac4-b7d9-4ea0-86c2-f1b0e4e2daf9.png)

## 提供一种循环命令
* cmd输入，循环执行100次
* for /l %x in (1,1,100) do python wjx.py %x
