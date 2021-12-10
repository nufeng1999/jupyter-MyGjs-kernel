from setuptools import setup

setup(name='jupyter_MyGjs_kernel',
      version='0.0.1',
      description='Minimalistic Python kernel for Jupyter',
      author='nufeng',
      author_email='18478162@qq.com',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
      ],
      url='https://github.com/nufeng1999/jupyter-MyGjs-kernel/',
      download_url='https://github.com/nufeng1999/jupyter-MyGjs-kernel/tarball/0.0.1',
      packages=['jupyter_MyGjs_kernel'],
      scripts=['jupyter_MyGjs_kernel/install_MyGjs_kernel'],
      keywords=['jupyter', 'notebook', 'kernel', 'python','py'],
      include_package_data=True
      )
