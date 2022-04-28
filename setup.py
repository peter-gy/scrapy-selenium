from setuptools import setup, find_packages

install_requires = open('./requirements/requirements.txt', 'r').readlines()

setup(
    name='scrapy-selenium',
    version='0.0.8',
    author='Clément Denoix, Péter Ferenc Gyarmati',
    author_email=', dev.petergy@gmail.com',
    packages=find_packages(),
    install_requires=install_requires,
    include_package_data=True,
    zip_safe=False,
    url='https://github.com/peter-gy/scrapy-selenium',
)
