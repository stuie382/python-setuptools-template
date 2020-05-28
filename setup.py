"""Setup

File that manages the configuration of the virtual environment,
ensuring that all required dependencies are present.
"""
import setuptools

with open("README.md", "r") as full_desc:
    LONG_DESC = full_desc.read()

with open("requirements.txt", "r") as reqs:
    REQUIREMENTS = reqs.read().split('\n')

setuptools.setup(
    name="projectname",
    version="0.0.0",
    author="your-name-here",
    description="short-description-here",
    long_description=LONG_DESC,
    long_description_content_type="text/markdown",
    packages=["your-package-name-here"],
    install_requires=REQUIREMENTS,
    python_requires='>=3.6'
)