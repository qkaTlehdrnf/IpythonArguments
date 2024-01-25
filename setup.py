from setuptools import setup, find_packages

setup(
    name='IPYTHON_ARGPARSE',  # A suitable name for your package
    version='1.0.0',              # Starting with version 1.0.0
    author='Kim, Won-Joong',           # Replace with your name
    author_email='wonjoong11@yonsei.ac.kr',  # Replace with your email
    description='A utility for seamless argument parsing in IPython notebooks and Python scripts.',  # Short description
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/qkaTlehdrnf/IPYTHON_ARGPARSE',  # Replace with your repository URL
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        'easydict',  # The code depends on easydict
        'ipython',   # Assuming IPython is a dependency, given the use of get_ipython
    ],
    classifiers=[
        'Development Status :: 4 - Beta',   # Assuming the project is in a beta stage
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # Assuming MIT License
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Framework :: IPython',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.6',  # Specifying compatible Python versions
)
