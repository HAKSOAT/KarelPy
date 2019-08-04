from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='karel',
      version='0.1',
      description='Popular educational coding robot',
      long_description=readme(),
      classifiers=[
            'License :: OSI Approved :: MIT License',
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python :: 3.6',
            'Topic :: Education :: Computer Aided Instruction (CAI)'
      ],
      keywords='karel robot education',
      url='http://github.com/haksoat/karelpy',
      author='Habeeb Shopeju',
      author_email='shopejuh@gmail.com',
      license='MIT',
      packages=['karelpy'],
      install_requires=[
                'pygame',
            ],
      include_package_data=True,
      zip_safe=False)
