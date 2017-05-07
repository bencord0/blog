from setuptools import find_packages, setup

setup(
    name='blog',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={"blog": [
        "static/*/*",
        "templates/*",
    ]},
    install_requires=[
        'klein',
        'pyasn1',
        'treq',
        'twisted[tls]',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest-asyncio',
    ],
    entry_points={
        'console_scripts': [
            'blog = blog.__main__:main',
        ]
    },
    zip_safe=False,
)
