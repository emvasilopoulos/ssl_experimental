import setuptools

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="ssl_lib",
    version="0.0.1",
    author="Manos Vasilopoulos",
    author_email="emmanouilvasilopoulos@gmail.com",
    requires=required,
    # include everything under ssl_lib/src only
    packages=setuptools.find_packages(where="ssl_lib/src"),
    package_dir={"": "ssl_lib/src"},
)
