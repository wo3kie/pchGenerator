## PCHGenerator...

The PCHGenerator is a tool for helping precompiled header generation. It scans all source files in project and selects the most often used headers for putting them into precompiled header.  

## Copyright (C) 2012 Lukasz Czerwinski  

## Requirements
python >2.7

## How to use it...

1. Create precompiled.h file
```
$ pch.py -c="-I d:\boost" main.cpp test.cpp

$ cat precompiled.h
// File generated by : pch.py
// Compilation options: -I d:\boost
// Project path       : /home/project*
// Threshold          : 1
// Exclude pattern    :
// Exclude but pattern:
#include "d:/MinGW/bin/../ ... /include/c++/3.4.5/iostream"
#include "d:/MinGW/bin/../ ... /include/c++/3.4.5/vector"
```

2. Compile precompiled.h into precompiled.gch
```
  $ g++ -I d:\boost precompiled.h
```

3. Compile your project with prcompiled.gch according to the g++ manual  
In every source code at the beginning put '#include "precompiled.h"' line. For details click here [gnu g++](http://gcc.gnu.org/onlinedocs/gcc-4.1.2/gcc/Precompiled-Headers.html) or here [stackowerflow](http://stackoverflow.com/questions/58841/precompiled-headers-with-gcc).

## Bugs...
There are no bugs. There are "features".

## Support and further development...
Maybe some day in the future I will do
* add some support for CLang
* add some support for Microsoft Visual C++

