from setuptools import setup, find_packages
from prov4ml import __version__ as prov4mlversion
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='prov4ml',
    version=prov4mlversion,
    packages=find_packages(),
    install_requires=required,  # Loaded from requirements.txt
    extras_require={
        'apple': [
            # Optional dependencies for Apple/Mac
            'apple_gpu==0.3.0'
        ], 
        'amd': [
            # Optional dependencies for AMD
            'amd_gpu==0.3.0', 
            'pyamdgpuinfo==2.1.6',
        ], 
        'nvidia': [
            # Optional dependencies for NVIDIA
            'nvitop==1.3.2',
        ]
    }
)
