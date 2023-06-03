from setuptools import setup, find_packages

setup(
    name='FYSPYAPISDK',
    version='1.0.0',
    author='Find Your Spirit',
    author_email='opensource@fysapp.co',
    description='Your SDK description',
    long_description='Long description of your SDK',
    url='https://github.com/FindYourSpirit/fys-sdk-py',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='your, sdk, keywords',
    install_requires=[
        'dependency1',
        'dependency2',
        # Specify any other dependencies your SDK requires
    ],
    python_requires='>=3.7',
)
