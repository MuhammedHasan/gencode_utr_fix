from setuptools import setup, find_packages


requirements = [
    'setuptools',
    'tqdm',
    'click',
    'pyranges'
]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest']

setup(
    author="M. Hasan Çelik",
    author_email='muhammedhasancelik@gmail.com',
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    description="Fix UTR of Gencode",
    install_requires=requirements,
    license="MIT license",
    keywords=['Gencode', 'UTR'],
    name='gencode_utr_fix',
    packages=find_packages(include=['gencode_utr_fix']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/MuhammedHasan/gencode_utr_fix',
    version='1.0.0',
)
