# Selenium模拟器

标签（空格分隔）： selenium python

---


通过JavaScript获取数据的站点，python对JavaScript支持不太友好，所以唯一的方法就是模拟游览器。
mechanize不支持JavaScript，但selenium支持。

返回元素
```
find_element(self, by = 'id', value =None)
find_element_by_class_name(self, name)
find_element_by_css_selector(self, css_selector)
find_element_by_id(self, id_)
find_element_by_link_text(self,link_text)
find_element_by_name(self, name)
find_element_by_partial_link_text(self, link_text)
find_element_by_tag_name(self, name)
find_element_by_xpath(self, xpath)
```

返回列表
```
find_elements(self, by = 'id', value =None)
find_elements_by_class_name(self, name)
find_elements_by_css_selector(self, css_selector)
find_elements_by_id(self, id_)
find_elements_by_link_text(self,link_text)
find_elements_by_name(self, name)
find_elements_by_partial_link_text(self, link_text)
find_elements_by_tag_name(self, name)
find_elements_by_xpath(self, xpath)
```

获取数据有两种方法
分别是：
1、element.text
2、element.get_attribute(name)

然后eval解析





