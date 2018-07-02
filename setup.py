from setuptools import setup, find_packages

with open("README.md", 'r') as fh:
    long_description = fh.read()

setup(name='mathgen',
      version='0.0.1',
      description='Generate random maths problems',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='http://github.com/murenei/mathgen',
      author='Richard Murray',
      author_email='rick.j.murray@gmail.com',
      license='MIT',
      packages=find_packages(),
      classifiers=(
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ),
      install_requires=[
          'sympy',
      ],
      # zip_safe=False
      )
