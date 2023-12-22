from setuptools import setup, find_packages

with open('requirements.txt', encoding='utf-8') as f_obj:
    requirements = f_obj.read().splitlines()

setup(
    name='SPMMT',
    version='0.1.0',
    author='Kevin Hoffschlag',
    description='Transcribe information from educational module manual to pandas dataframe (and xlxs) with SPMMT.',
    url='https://github.com/khoffschlag/SPMMT',
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.9',
)
