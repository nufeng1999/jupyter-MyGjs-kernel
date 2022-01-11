##//%file:kernel.py
#
#   MyGjs Jupyter Kernel
#
from math import exp
from queue import Queue
from threading import Thread
from ipykernel.kernelbase import Kernel
from pexpect import replwrap, EOF
from jinja2 import Environment, PackageLoader, select_autoescape,Template
from abc import ABCMeta, abstractmethod
from typing import List, Dict, Tuple, Sequence
from shutil import copyfile,move
from urllib.request import urlopen
import socket
import copy
import mmap
import contextlib
import atexit
import platform
import atexit
import base64
import urllib.request
import urllib.parse
import pexpect
import signal
import typing 
import typing as t
import re
import signal
import subprocess
import tempfile
import os
import stat
import sys
import traceback
import os.path as path
import codecs
import time
import importlib
import importlib.util
import inspect
from . import ipynbfile
from plugins import ISpecialID
# from plugins.ISpecialID import IStag,IDtag,IBtag,ITag,ICodePreproc
from plugins._filter2_magics import Magics
from .Mymacroprocessor import Mymacroprocessor
try:
    zerorpc=__import__("zerorpc")
    # import zerorpc
except:
    pass
fcntl = None
msvcrt = None
bLinux = True
if platform.system() != 'Windows':
    fcntl = __import__("fcntl")
    bLinux = True
else:
    msvcrt = __import__('msvcrt')
    bLinux = False
from .MyKernel import MyKernel
class MyGjsKernel(MyKernel):
    implementation = 'jupyter-MyGjs-kernel'
    implementation_version = '1.0'
    language = 'JavaScript'
    language_version = ''
    language_info = {'name': 'javascript',
                     'version': sys.version.split()[0],
                     'mimetype': 'text/javascript',
                     'codemirror_mode': {
                        'name': 'javascript',
                        'version': sys.version_info[0]
                     },
                     'pygments_lexer': 'javascript%d' % 3,
                     'nbconvert_exporter': 'javascript',
                     'file_extension': '.js'}
    runfiletype='script'
    banner = "MyGjs kernel.\n" \
             "Uses gjs, compiles in javascript, and creates source code files and executables in temporary folder.\n"
    kernelinfo="[MyGjs]"
    main_head = "\n" \
            "\n" \
            "int main(List<String> arguments){\n"
    main_foot = "\nreturn 0;\n}"
##//%include:src/comm_attribute.py
    def __init__(self, *args, **kwargs):
        super(MyGjsKernel, self).__init__(*args, **kwargs)
        self.runfiletype='script'
        self.kernelinfo="[MyGjsKernel{0}]".format(time.strftime("%H%M%S", time.localtime()))
        
#################
##do_runcode
    def do_runcode(self,return_code,file_name,magics,code, silent, store_history=True,
                    user_expressions=None, allow_stdin=True):
        return_code=return_code
        file_name=file_name
        bcancel_exec=False
        retinfo=self.mymagics.get_retinfo()
        retstr=''
        ##代码运行前
        p = self.mymagics.create_jupyter_subprocess(['gjs',file_name]+ magics['_st']['args'],cwd=None,shell=False,env=self.mymagics.addkey2dict(magics,'env'),magics=magics)
        #p = self.create_jupyter_subprocess([binary_file.name]+ magics['args'],cwd=None,shell=False)
        #p = self.create_jupyter_subprocess([self.master_path, binary_file.name] + magics['args'],cwd='/tmp',shell=True)
        self.mymagics.g_rtsps[str(p.pid)]=p
        return_code=p.returncode
        ##代码启动后
        bcancel_exec,retstr=self.mymagics.raise_plugin(code,magics,return_code,file_name,3,2)
        # if bcancel_exec:return bcancel_exec,retinfo,magics, code,file_name,retstr
        
        if len(self.mymagics.addkey2dict(magics,'showpid'))>0:
            self.mymagics._write_to_stdout("The process PID:"+str(p.pid)+"\n")
        return_code=p.wait_end(magics)
        # del self.g_rtsps[str(p.pid)]
        # p.write_contents(magics)
        ##
        ##调用接口
        return_code=p.returncode
        ##代码运行结束
        if p.returncode != 0:
            self.mymagics._log("Executable exited with code {}".format(p.returncode),2)
        return bcancel_exec,retinfo,magics, code,file_name,retstr
##do_compile_code
    def do_compile_code(self,return_code,file_name,magics,code, silent, store_history=True,
                    user_expressions=None, allow_stdin=True):
        return_code=0
        file_name=file_name
        sourcefilename=file_name
        bcancel_exec=False
        retinfo=self.mymagics.get_retinfo()
        retstr=''
        return bcancel_exec,retinfo,magics, code,file_name,retstr
##do_create_codefile
    def do_create_codefile(self,magics,code, silent, store_history=True,
                    user_expressions=None, allow_stdin=True):
        return_code=0
        file_name=''
        bcancel_exec=False
        retinfo=self.mymagics.get_retinfo()
        retstr=''
        source_file=self.mymagics.create_codetemp_file(magics,code,suffix='.js')
        newsrcfilename=source_file.name
        file_name=newsrcfilename
        return_code=True
        return bcancel_exec,self.mymagics.get_retinfo(),magics, code,file_name,retstr
##do_preexecute
    def do_preexecute(self,code,magics,silent, store_history=True,
                user_expressions=None, allow_stdin=False):
        bcancel_exec=False
        retinfo=self.mymagics.get_retinfo()
        
        return bcancel_exec,retinfo,magics, code
