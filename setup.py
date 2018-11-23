# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import os
import re
from io import open

here = os.path.abspath(os.path.dirname(__file__))


def _read(fname):
    if os.path.isfile(fname):
        with open(os.path.join(here, fname), encoding="utf-8") as f:
            return f.read()
    else:
        print('warning: file {} does not exist'.format(fname))
        return ''

def get_version(path):
    src = _read(path)
    pat = re.compile(r"""^version = ['"](.+?)['"]$""", re.MULTILINE)
    result = pat.search(src)
    version = result.group(1)
    return version

long_description = _read("README.md")
install_requires = [
    l
    for l in _read("requirements.txt").split("\n")
    if l.strip() and not l.strip().startswith("#")
]

name = "simple-colors"
gh_repo = "https://github.com/weaming/{}".format(name)

setup(
    name=name,  # Required
    version=get_version('simple_colors.py'),  # Required
    # This is a one-line description or tagline of what your project does.
    description="Colorful output in terminal",  # Required
    long_description=long_description,  # Optional
    long_description_content_type="text/markdown",  # Optional
    install_requires=install_requires,
    # You can use `find_packages()` or the `py_modules` argument which expect a
    # single python file
    # packages=find_packages(exclude=["contrib", "docs", "tests"]),  # Required
    py_modules=["simple_colors"],
    url=gh_repo,  # Optional
    author="weaming",  # Optional
    author_email="garden.yuen@gmail.com",  # Optional
    keywords="terminal",  # Optional
    project_urls={"Bug Reports": gh_repo, "Source": gh_repo},  # Optional
)


