# Python-Selenium

https://www.byhy.net/tut/auto/selenium/01/

## 原理

安装selenium库以及浏览器驱动

简化代码可以在系统环境变量加上驱动的文件目录

## WebDriver

创建WebDriver 实例对象 指明使用哪个浏览器的驱动

通过get 方法 让浏览器打开指定网站

```python
from selenium import webdriver
wd = webdriver.Edge()
# 或者 wd = webdriver.Edge(r"D:\apps\edgedriver_win64")
wd.get ("https://www.baidu.com")
```



## 选择网页元素

1. *通过元素**ID***

   ```python
   element = wd.find_element(By.ID, 'su')
   ```

2. *通过元素**class**名*

   ```python
   elements = wd.find_elements(By.CLASS_NAME, 'foot-async-script')
   ```

   注意 (find_element 和 find_elements的区别)

   |          | find_element                                       | find_elements                |
   | -------- | -------------------------------------------------- | ---------------------------- |
   | 返回对象 | 如果有多个符合条件的元素返回第一个                 | 返回所有符合条件的元素的列表 |
   | 异常处理 | 没有符合的元素*抛出* *NoSuchElementException* 异常 | 返回空列表                   |

> ```python
> for element in elements:
>     print(element.text)
> ```
>
> 可以输出元素对应文本内容

3. *通过标签名字*

```python
element = wd.find_elements(By.TAG_NAME, "div")
```

4. *通过WebElement对象*(find_element方法返回的就是webelement对象)

   - WebDriver对象选择元素范围是整个网页

   - WebElement对象选择元素则是在元素内寻找


```python
element = wd.find_elements(By.ID,'container')
spans = element.find_elements(By.TAG_NAME, 'span')
```



## 等待元素出现

程序执行速度远大于网页响应的速度，所以执行的时候往往会因为网页速度慢而导致找不到接下来的元素

解决办法：

1. ```python
   import time
   time.sleep(1) #等1秒 但可能还是有问题
   ```

2. ```python
   while True:
       try:
           element = wd.find_element(By.ID, '1')
           print (element.text)
           break
       except:
           sleep(1)
   ```

3.  **隐式等待  (全局等待) **

   ```python
   wd.implicitly_wait(10)
   ```

   加入以上代码后，那么后续所有的 `find_element` 或者 `find_elements` 之类的方法调用 都会采用下面的策略：

   若**找不到该元素**并不立即返回错误，而是每隔半秒钟重新寻找该元素，直到元素找到

   如果超出了最长时间（括号内规定，上述代码为10秒）,则报出错误
   
   > implicitly ： 隐式地，含蓄地
   >
   > 但有时就只能依靠方法一`sleep(1)`，因为点击某元素的特定文本内容可能才会更新下一个元素的内容
   >
   > [bilibili 有implicitwait, sleep就没有用了吗](https://www.bilibili.com/video/BV1Z4411o7TA/?p=35&vd_source=65c0b265ff4f8014de15e5f690699b25)

## 操控元素

### 点击元素 

.click         (默认点击正中间)

### 输入内容

 .send_keys ("输入内容")

### 清空内容 

.clear 方法

处理有时候输入框已经有默认文本的情况

### 获取元素信息

- 获取文本内容

  - element .text     (尖括号内的文本)

  - 对于input的输入框, 如果要获得已经输入的文本, 用.get_attribute ('value')

  - .text 出了些问题时

    ```html
    .get_attribute('innerText')
    .get_attribute('textContent')
    ```

> 有时候，元素的文本内容没有展示在界面上，或者没有完全完全展示在界面上。 这时，用WebElement对象的text属性，获取文本内容，就会有问题。
>
> 使用 innerText 和 textContent 的区别是，前者只显示元素可见文本内容，后者显示所有内容（包括display属性为none的部分）

- 获取元素属性 .get_attribute('class')
- 获取整个元素对应的HTML
  - .get_attribute('outerHTML') 可以获得整个元素的所有内容
  - .get_attribute('innerHTML') 可以获得元素内部的内容
- 



## CSS表达式选择元素

最强大的元素选择器

1. 基本用法

```python
css = wd.find_elements(By.CSS_SELECTOR, 'CSS Selector参数')
```

|          | CSS Selector                                                 | 其他方式                                |
| :------- | ------------------------------------------------------------ | --------------------------------------- |
| class    | wd.find_elements(By.CSS_SELECTOR, '**.**类名')               | wd.find_elements(By.CLASS_NAME, '类名') |
| id       | wd.find_elements(By.CSS_SELECTOR, '**#**ID名')               | wd.find_elements(By.ID, 'ID名')         |
| tag名    | wd.find_elements(By.CSS_SELECTOR, 'tag名')                   | wd.find_elements(By.TAG_NAME, "tag名")  |
| 其他属性 | wd.find_elements(By.CSS_SELECTOR, '[属性]')  (如链接等其他属性值) |                                         |

- 选择语法联合使用

也可以进行混用，如 .plant[name = 'SKnet'] 表示class属性是plant**且**name为SKnet的元素，注意中间不能加空格，原因看第二点

- 组选择：

加上 **,**表示两个属性之间是或关系，如  `#t1 span,p` 表示 t1中的span 和外面所有的p；如果是要 t1中的span和p  只能 `#t1 span, #t2 p`

>  属性值不一定要完全等于，写法如下
>
> - 包含什么字符串 *=
> - 以什么开头 ^=
> - 以什么结尾 $=
>
> 另外注意：组选择结果列表中，选中元素排序， 不是 组表达式的次序， 而是符合这些表达式的元素，在HTML文档中的出现的次序。


2. 选择子元素和后代元素

```python
元素1 > 元素2  #表示元素1中的元素2, 严格符合2是1的子元素
元素1 > 元素2 > 元素3 > 元素4  #表示1中的2中的3中的4元素 一层层严格符合

元素1 元素2  #元素2不一定是1的子元素,也可以是后代元素
元素1 元素2 元素3 元素4 

两者可以混用`
```

 其中每一个元素的表示方式都符合上述基本用法里的规则



3. 验证CSS Selector

​	可以在浏览器中ctrl + f， 在输入框中输入所写的代码，检查是否正确选择到所需的元素



4. 按次序选择子节点  **nth-child**

   - span:nth-child(2) 表示是span标签且是父元素的第二个子节点
   - 倒数 **nth-last-child()** 

   指定类型 **nth-of-type**  同样的倒数加last

   - span:nth-of-type(1)表示第一个span类型的节点  与上面做区别
   - 括号内还可以 even(偶数) 或者 odd(奇数) 



5. 兄弟节点的选择

   如 h3 + span 表示选择跟h3同级且紧跟h3的span

   h3 ~ span 表示跟 h3同级且在其后面所有的span



## frame切换

html语法中 iframe元素或者 frame元素可以包含一个被嵌入的html文档

在我们使用selenium打开一个网页时， 我们的操作范围缺省是当前的 html ， 并不包含被嵌入的html文档里面的内容。

方法 : `wd.switch_to.frame(frame_reference)`

> 其中， frame_reference 可以是 
>
> frame 元素的 id ，name属性值 
>
> 或者frame 所对应的 WebElement 对象 ，例如 `wd.switch_to.frame(wd.find_element(By.TAG_NAME, "iframe"))`

tips： 我们把最外部的html称之为主html

返回主html: `wd.switch_to.default_content()`



## 窗口切换

点击一个新窗口的链接后，程序仍在操作原来的窗口



方法 ：**wd.switch_to.window(handle)**

handle即句柄，类似于网页窗口的ID。而WebDriver对象中有一个window_handles的属性，存放当前浏览器中所有的窗口句柄，故而可以通过类似下面的代码进行窗口切换

```python
for handle in wd.window_handles:
    # 先切换到该窗口
    wd.switch_to.window(handle)
    # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
    if 'Bing' in wd.title:
        # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
        break
```

同时可以使用下列代码回到主窗口

```python
# mainWindow变量保存当前窗口的句柄
mainWindow = wd.current_window_handle
#...
#通过前面保存的老窗口的句柄，自己切换到老窗口
wd.switch_to.window(mainWindow)
```



## 选择框



1. **radio** (input type = "radio" 单选框)

   根据value等属性通过 css的选择方式进行选择

2. checkbox (input type = "checkbox" 多选框)

   为了保证所选的是自己想要的，思路是

   - 先把所有选中的全部点击，确保都是未点击状态
   - 在选择所想选的

   通过 [checked = "checked"] 锁定所有已选的

3. select （select标签，每一项为option， 多选在select中有一个multiple属性)

   Selenium中有专门Select类

   ```python
   from selenium.webdriver.support.ui import Select
   select = Select(wd.find_elements(By.ID, "sss")) #创建Select对象 
   ```

   

   - 选择元素
     - 根据value选择对应option     select.select_by_value()
     - 根据选项的可见文本              select.select_by_visible_text()
     - 根据次序 select                      select.select_by_index()
   - 取消选择 deselect





## 其他技巧



1. 更多操作，如鼠标右键 双击 移动鼠标到某个元素 鼠标拖拽等

   在ActionChains类中有更多操作



 2. 冻结界面

    有些网页鼠标移到某个元素上出来其他元素，但是移开就消失，为了查看其对应的源码，故而就要冻结住动态显示的元素

    在Console中执行 setTimeout(function(){debugger}, 5000)

    表示过5000毫秒后进行debug，debug模式会冻住整个界面



3. 弹出框

   - alert 

     - 通知信息，只有确认

     - ```python
       driver.switch_to.alert.accept() #确认信息
       driver.switch_to.alert.text() #获取信息
       ```

   - confirm 

     - 需要用户进行某个操作，有确认或者取消
     - 代码和alert一样 (.alert也一样)， 取消是  .dismiss()

   - prompt

     - 需要提供其他信息才能继续，需要输入一些信息 
     - 发送信心 .send_keys()





## Xpath选择器



根节点用 **/** 表示，表示方式跟linux一样，和CSS中的 > 类似, 表示直接子节点



1. 基本语法

   - 从根节点写下来的叫做绝对路径

   - //div 表示所有的div标签

   - //div//p  表示div后面的所有p元素

   - 通配符 *  (和linux一模一样)



 	2. 根据属性选择
 	 - 格式 [@属性名= '属性值']  (属性值一定要有引号)
 	 - 例如  //*[@id = 'west'] 表示选择所有id值为west的标签
 	 - 如果一个元素的class有多个， 必须完全一致才能选中这个元素
 	   - 如 <div class = 'captial huge-city'>
 	   - 需要 //div[@class = "captial huge-city"] 才能选中这个标签，css中选择一个class就可以选择到它
 	 - 包含关系 [contains(@style, ' color')]  表示style属性里面包含color
 	 - 开头关系 [starts-with(@style, 'color')] 表示style属性以color开头
 	 - ends-with是xpath2.0的语法，但是大多数浏览器不支持



3. 按次序选择
   - 父元素的某类型的第某个元素
     - //p[2] 表示父元素中第二个p类型的子元素
     - 等价于 p:nth-of-type(2)
   - 父元素的第某个子元素
     - //*[2]
   - 倒数第某个
     - //*[last()] 表示倒数第一个
     - //*[last()-1]表示倒数第二个
   - 范围选择
     - 选择option类型的前两个节点
       - //option[position() <= 2]



 	4. 组选择和兄弟节点
 	 - //option | //h4表示选择所有的option和h4
 	 - **选择父节点**
 	   - /..
 	   - //*[@id='china']/..   表示id为china元素的父节点
 	   - 适用于本身没特征但子节点有id等属性的标签
 	 - following-sibling:: 选择后续兄弟节点
 	   - following-sibling::* 表示所有
 	   - following-sibling::select 表示后续的所有select
 	 - preceding-sibling:: 选择前面的兄弟节点



5. 注意点

   通过WebElement对象来选择其内部的元素，必须 './/p'加一个点才能表示是这个对象的子元素，否则搜索范围仍然为整个网页 

## 关闭



wd.quit()
