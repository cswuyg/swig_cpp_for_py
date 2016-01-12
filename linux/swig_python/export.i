/* File : IExport.i */
%module my_mod 
%{
#include "export.h"
%}

%include "std_string.i"
%include "std_vector.i"
%include "export.h"
namespace std {
   %template(vectori) vector<int>;
    %template(vectorstr) vector<std::string>;
};
