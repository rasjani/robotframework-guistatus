import os
from setuptools import setup, find_packages

version_data = {}
with open(os.path.join("src", "GuiStatus", "version.py")) as f:
    exec(f.read(), version_data)

requirements = []
with open("requirements.txt", "r") as f:
    requirements = list(filter(lambda s: s!="", f.read().split("\n")))


def __path(filename):
    return os.path.join(os.path.dirname(__file__),
                        filename)


version = "{}".format(version_data["VERSION"])

setup(name="robotframework-guistatus",
      version=version,
      description="Simple UI to show the status of currently running robot",
      author="SALabs",
      author_email="to.be.added@noexist89a887.org",
      url="https://github.com/Omenia/robotframework-guistatus",
      install_requires=requirements,
      packages=find_packages("src"),
      package_dir={"GuiStatus": "src/GuiStatus"},
      classifiers=["Programming Language :: Python :: 2",
                   "Programming Language :: Python :: 2.7",
                   "Programming Language :: Python :: 3",
                   "Programming Language :: Python :: 3.5",
                   "Programming Language :: Python :: 3.6"],
                   "Programming Language :: Python :: 3.7"],
      )
