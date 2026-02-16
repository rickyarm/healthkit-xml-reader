"""
Setup configuration for healthkit-xml-reader package
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file for long description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="healthkit-xml-reader",
    version="0.1.0",
    author="rickyarm",
    author_email="your.email@example.com",  # Update with your email
    description="A Python package to parse and analyze Apple HealthKit export.xml files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rickyarm/healthkit-xml-reader",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Healthcare Industry",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        # No external dependencies - uses only Python standard library
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.0.0",
            "mypy>=0.950",
        ],
    },
    entry_points={
        "console_scripts": [
            "healthkit-parse=scripts.parse_health_data:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)