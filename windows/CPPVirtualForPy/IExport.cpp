#include "IExport.h"
#include "Impl.h"


IExport* GetExport()
{
	return new ExportImpl;
}

void DestroyExport(IExport* pExport)
{
	delete pExport;
}
