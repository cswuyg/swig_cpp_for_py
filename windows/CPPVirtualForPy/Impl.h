#pragma once

#include "IExport.h"

class ExportImpl : public IExport
{
public:
	ExportImpl(){}
	virtual int Add(int a, int b);
	virtual int Sub(int a, int b);
};