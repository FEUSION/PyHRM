from setuptools import setup, find_packages
import os

dir_path = os.path.dirname(os.path.abspath(__file__))

rd_file = os.path.join(dir_path,'README.md')

import io
with io.open(rd_file, encoding="utf-8") as f:
  long_description = f.read()

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='PyHRM',
  version='0.0.2',
  description='A library for processing DNA Melting signal with feature extraction and automatic thresholding.',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/FEUSION/PyHRM',  
  author='RajagopalS',
  author_email='rajag2001416@gmail.com',
  maintainer=['RajagopalS rajag2001416@gmail.com','Vignesh_R mail2vikivignesh06@gmail.com','SenthilKumarN senthilkumarnallendran@gmail.com'],
  license='MIT', 
  classifiers=classifiers,
  keywords=['HRM','Melt','PCR'], 
  packages=find_packages(where='src'),
  package_dir={"":"src"},
  package_data={"PyHRM":["*.py","*.h5","*.md"]},
  include_package_data=True,
  install_requires=[
    'fpdf==1.7.2',
    'kaleido==0.2.1',
    'keras==2.12.0',
    'matplotlib==3.6.3',
    'numpy==1.23.5',
    'openpyxl==3.1.0',
    'packaging==23.1',
    'pandas==1.5.3',
    'Pillow',
    'plotly==5.13.0',
    'Requests==2.28.2',
    'scipy==1.10.1',
    'tensorflow==2.12.0', 
    'tqdm==4.64.1',
    'xlrd==2.0.1'
    ]

)
