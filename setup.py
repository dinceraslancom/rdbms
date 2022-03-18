from setuptools import setup, find_packages

requires = [
    'simpleitem'
]

with open("README.rst", "r", encoding="utf8") as f:
    readme = f.read()

setup(
    name='rdbms',
    version='1.0.2',
    package_dir={'rdbms': 'rdbms'},
    author="Dincer Aslan",
    author_email="dinceraslan.com@gmail.com",
    description="Relational Database Management System",
    long_description=readme,
    long_description_content_type='text/x-rst',
    url="https://github.com/dinceraslancom/rdbms",
    project_urls={
        'Source': 'https://github.com/dinceraslancom/rdbms',
    },
    install_requires=requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.3",
)
