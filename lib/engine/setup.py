# setup.py file
import sys
import os
import shutil

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [
        Extension("engine", 
                  sources=["engine.pyx",
                       ],
                  libraries=["checkers"],          
                  language="c++",                   
                  extra_compile_args=["-fopenmp", "-O3", '-std=c++11'],
             )
        ]
)           