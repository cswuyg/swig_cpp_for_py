#!/home/work/install/bin/python
#-*-coding:utf-8-*-
import my_mod

# test int add(int a, int b)
print(my_mod.add(1, 2))

# test std::string append(const std::string&, const std::string&)
print(my_mod.append('a', 'bcd'))

# test return std::vector<int>
vec = my_mod.test(1)
for k in vec:
    print(k)

# test return std::vector<std::string>
vec = my_mod.test("a");
for k in vec:
    print(k)

# test one point int output
sub_ret = my_mod.sub2(10, 20)
print(sub_ret)

# test one std::string point output
str_ret = my_mod.point_ret();
print(str_ret);

# test point int and point std::string output
ret = my_mod.two_ret(10, 'hello world')
print(ret[0])
print(ret[1])

# test reference return
ret = my_mod.ref_ret()
print(ret)

print(my_mod.get(10))

x = my_mod.gg();
for k in x:
    print(k);
"""
output:
3
abcd
1
10
20
a
start
end
"""
