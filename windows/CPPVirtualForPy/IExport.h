/**
C++ has virtual function for Python 
cswuyg@gmail.com
2014.1.14
*/
#pragma once

class IExport
{
public:
	IExport(){}
	~IExport(){}
	virtual int Add(int a, int b) = 0;
	virtual int Sub(int a, int b) = 0;
};


IExport* GetExport();
void DestroyExport(IExport* pExport);