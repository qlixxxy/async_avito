from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="async_avito",
    version="0.0.1",
    author="Anton Sarhan",
    author_email="sqlixor@gmail.com",
    description=long_description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/qlixxxy/async_avito",
    project_urls={
        
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    install_requires=[
        'aiohttp==3.8.1',
        'asyncio==3.4.3',
        'requests-html==0.10.0',
        'tortoise-orm==0.18.1'
    ],
    packages=find_packages(where="src"),
    python_requires=">=3.10",
)