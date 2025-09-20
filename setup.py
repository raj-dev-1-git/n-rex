from setuptools import setup, find_packages

setup(
    name="n-rex",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["numpy"],
    description="n-rex: Load, predict, repeat.",
    author="Raj",
    url="https://github.com/raj-dev-1-git/n-rex",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown"
)
