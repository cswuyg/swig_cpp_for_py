/**
C++ for Python 
cswuyg@gmail.com
2014.1.14
*/
#pragma once

class BaseClass 
{
public:
	BaseClass();
	virtual ~BaseClass();
	virtual int Calc(int a, int b);
	int result;
};