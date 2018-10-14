from setuptools import setup, find_packages

setup(
    name="hangman",
    version="0.0.0",
    author="Alina Glukhonemykh",
    author_email="jivrej@ya.ru",
    url="https://github.com/Kuzaiherba/hangman",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "numpy"
    ],
    setup_requires=[
        "pytest-runner",
        "pytest-pylint",
        "pytest-pycodestyle",
        "pytest-pep257",
        "pytest-cov",
    ],
    tests_require=[
        "pytest",
        "pylint",
        "pycodestyle",
        "pep257",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
    ]
)
