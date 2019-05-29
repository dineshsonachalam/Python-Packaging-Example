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
