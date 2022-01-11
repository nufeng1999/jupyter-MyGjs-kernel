from ipykernel.kernelapp import IPKernelApp
from .kernel import MyGjsKernel
IPKernelApp.launch_instance(kernel_class=MyGjsKernel)
