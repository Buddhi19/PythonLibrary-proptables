from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='Refrigerant R134a Property Table',
  version='0.0.1',
  description='Implementation of R134a property table in a userfriendly manner',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Buddhi Wijenayake',
  author_email='wijenayakebuddhi34802@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='R134propertytable', 
  packages=find_packages(),
  install_requires=[''] 
)