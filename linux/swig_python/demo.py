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
