from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='pyVIF',
    version='0.0.1',
    description='Drop columns with high Variance Inflation Factor to mitigate multi-collinearity in data that is in Pandas DataFrame format',
    Long_description=open('README.txt').read()+'\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Zhuang Baokun',
    author_email='zhuangbaokun"gmail.com',
    license='MIT',
    classifers=classifiers,
    keywords='Variance Inflation Factor',
    packages=find_packages(),
    install_requires=['pandas','numpy','scipy','statsmodels']
)