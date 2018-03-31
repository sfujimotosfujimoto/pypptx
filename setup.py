from distutils.core import setup

setup(
    name="PyPPTX",
    version="0.1.0",
    author="sf",
    author_email="s-fujimoto@seig-boys.jp",
    packages=["src", "data", "output", "ppt"],
    include_package_data=True,
    url="",
    description="for",
    long_description=open("README.txt").read(),
    install_requires=[
        "python-pptx",
        "pandas"
    ],
)
