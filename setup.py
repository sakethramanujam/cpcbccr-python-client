try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.md','r') as f:
    readme = f.read()

setup(
    name="cpcbccr",
    include_package_data=True,
    packages=['cpcbccr',],
    description="An unofficial python client to obtain cpcb ccr data",
    long_description=readme,
    long_description_content_type='text/markdown',
    version="0.3",
    python_requires='>=3.6',
    install_requires=['requests', 'pandas'],
    author='Saketha Ramanujam',
    author_email="saketh.ramanujam98@gmail.com",
    url="https://github.com/sakethramanujam/cpcbccr-python-client",
    classifiers=[
         "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
