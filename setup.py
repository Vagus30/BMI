# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 17:43:28 2022

@author: Tejaswi
"""

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bmi-cal-vagus30",
    version="0.0.1",
    author="Tejaswi",
    author_email="vishwas.tejaswi@gmail.com",
    description="BMI calculator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Vagus30/BMI",
    project_urls={
        "Bug Tracker": "https://github.com/vagus30/BMI/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)