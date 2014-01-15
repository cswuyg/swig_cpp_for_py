#include "class.h"
#include "utility/tick_log.h"
using namespace utility;
using namespace WYGTickLog;
BaseClass::BaseClass()
{
	LogInfo(__WFUNC__);
}

BaseClass::~BaseClass()
{
	LogInfo(__WFUNC__);
}

int BaseClass::Calc( int a, int b )
{
	LogInfo(__WFUNC__);
	result = a + b;
	return result;
}

