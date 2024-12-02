from setuptools import setup, find_packages

setup(
    name="WurlyCVEs",
    version="0.0.1",
    author="KcanCurly",
    description="Working cve scripts i have found while pentesting.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/KcanCurly/WurlyCVEs",
    packages=find_packages(),
    install_requires=[
        "requests",
        "urllib3"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "cve-2020-14882=CVE.cve-2020-14882:main",  
        ],
    },
)