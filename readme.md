### Python Packaging
Creating The Scaffolding
The initial directory structure for funniest should look like this:

```
sample_package/
        tests/
            test_joke.py
            __init__.py
        __init__.py
    setup.py

```
The main setup config file, setup.py, should contain a single call to setuptools.setup(), like so:
```
from setuptools import setup

setup(name='sample_package',
      version='0.1',
      description='The funniest joke in the world',
      url='http://github.com/storborg/funniest',
      author='Flying Circus',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['sample_package'],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)

```

Now we can install the package locally (for use on our system), with:
```
$ pip install .
```

```
$ pip3 freeze
sample-package==0.1
pytest==3.3.2

```
