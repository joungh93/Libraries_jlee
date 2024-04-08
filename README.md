# Libraries_jlee
(updated on 2024. 4. 8.)


## Description
A default library of useful Python codes that can be imported into any paths


## Prerequisites
* Retrieving this library to the Python path (i.e. /home/jlee/anaconda3/bin/)
```
$ cd /your_python_path/
$ git clone https://github.com/joungh93/Lib_jlee.git
```
* Writing ``.pythonrc`` file
```
$ vi /your_home_directory/.pythonrc
import sys
sys.path.append("/your_python_path/Lib_jlee/")
:wq
```
* Adding the Python path to the system
```
$ vi ~/.bashrc
export PYTHONSTARTUP="/your_home_directory/.pythonrc"
$ source ~/.bashrc
```


## :snail:
