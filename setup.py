from setuptools import setup

setup(
    name='blog',
    packages=['blog'],
    entry_points={
        'console_scripts': [
            'blog = blog.__main__:main',
        ]
    },
)
