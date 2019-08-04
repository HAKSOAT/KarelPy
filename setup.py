from setuptools import setup

setup(name='karelpy',
      version='0.1',
      description='Popular educational coding robot',
      classifiers=[
            'License :: OSI Approved :: BSD License',
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
