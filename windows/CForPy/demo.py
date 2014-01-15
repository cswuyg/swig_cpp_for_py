#-*-coding:utf-8-*-
#测试py调用C编写的DLL
from add_module import Add

def test_add():
	print(Add(10, 20))

test_add()