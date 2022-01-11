#!/usr/bin/env python
# coding: utf-8
with open("README.md", "r") as f:
	long_description = f.read()
import setuptools
setuptools.setup(name='jupyter_MyGjs_kernel',
      version='0.0.1',
      description='Minimalistic Gjs kernel for Jupyter',
    long_description=long_description,
    long_description_content_type="text/markdown",
      author='nufeng',
      author_email='18478162@qq.com',
      license='MIT',
      url='https://github.com/nufeng1999/jupyter-MyGjs-kernel/',
      download_url='https://github.com/nufeng1999/jupyter-MyGjs-kernel/releases/tag/0.0.1',
    packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
      scripts=['jupyter_MyGjs_kernel/install_MyGjs_kernel'],
      keywords=['jupyter', 'notebook', 'kernel', 'python','javascript','gjs'],
      include_package_data=True
      )
