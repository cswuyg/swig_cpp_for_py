#-*-coding:utf-8-*-
#测试python跟C++多态的结合，swig太帅了！
import vir_mod
def test_virtual():
	operator = vir_mod.GetExport()
	print("Add", operator.Add(10, 20))
	print("Sub", operator.Sub(20, 10))


test_virtual()
