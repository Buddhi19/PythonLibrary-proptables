from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='PTable',
  version='0.1',
  description='Implementation of R134a property table in a userfriendly manner',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/Buddhi19/PropertyTables_Python.git',  
  author='Buddhi Wijenayake',
  author_email='wijenayakebuddhi34802@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='R134propertytable', 
  packages=["Lib"],
  package_data={
        'Lib': ['R134a_TempSat.csv', 'R134a_SupPreSat.csv','R134a_Super.csv',
                    'R134a_PresSat.csv'],
    },
  python_requires=">=3.7",
  install_requires=['pandas'] 
)