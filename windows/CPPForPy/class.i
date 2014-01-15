/* File : class.i */
%module class_module 

%{
#include "class.h"
%}

/* Let's just grab the original header file here */
%include "class.h"

	