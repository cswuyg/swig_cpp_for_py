#-*-coding:utf-8-*-
#测试python调用C++
import class_module
def test_cpp_class():
	obj = class_module.BaseClass()
	obj2 = class_module.BaseClass()
	obj3 = obj2
	del obj2  #C++模块会打日志，实验对象真正的析构时机

	print(obj.Calc(10, 20))
	print(obj.result)	


test_cpp_class()
