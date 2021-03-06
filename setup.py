import os
import re

from setuptools import find_packages, setup


REGEXP = re.compile(r"^__version__\W*=\W*'([\d.abrc]+)'")


def read_version():

    init_py = os.path.join(
        os.path.dirname(__file__), 'delivery_pdf', '__init__.py'
    )

    with open(init_py) as f:
        for line in f:
            match = REGEXP.match(line)
            if match is not None:
                return match.group(1)
        else:
            msg = f'Cannot find version in ${init_py}'
            raise RuntimeError(msg)


install_requires = [
    'aiohttp==3.5.4',
    'python-dotenv',
    'toml',
    'requests',
    'gunicorn',
]



setup(
    name='delivery_pdf',
    version=read_version(),
    description='Async server for convert pdf from athena',
    platforms=['POSIX'],
    author="Sergey Ivanov",
    author_email="djapy@yandex.ru",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    zip_safe=False,
)