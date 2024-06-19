"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="dbmarkenfarben",  # Required
    version="0.6.4",  # Required
    description="Get the html or rgb code of one of the Deutsche Bahn AG brand colours.",  # Optional
    long_description_content_type="text/markdown",  # Optional (see note above)
    url="https://github.com/jbnsn/dbmarkenfarben",  # Optional
    author="Jonas Bunsen",  # Optional
    author_email="jonas.bunsen@deutschebahn.com",  # Optional
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 4 - Beta",
        "Topic :: Deutsche Bahn",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="DeutscheBahn",  # Optional
    package_dir={"": "src"},  # Optional
    packages=find_packages(where="src"),  # Required
    python_requires=">=3.7, <4",
    project_urls={  # Optional
        "Source": "https://github.com/jbnsn/dbmarkenfarben/",
    },
)