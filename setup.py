import os
from setuptools import setup, find_packages

# For Python 3: use a locals dictionary
# http://stackoverflow.com/a/1463370/6820620
ldict = locals()
# Get version and release info, which is all stored in brainconn/version.py
ver_file = os.path.join('brainconn', 'version.py')
with open(ver_file) as infofile:
    pythoncode = [line for line in infofile.readlines() if not
                  line.strip().startswith('#')]
    exec('\n'.join(pythoncode), globals(), ldict)

opts = dict(name=ldict['NAME'],
            maintainer=ldict['MAINTAINER'],
            description=ldict['DESCRIPTION'],
            long_description=ldict['LONG_DESCRIPTION'],
            url=ldict['URL'],
            download_url=ldict['DOWNLOAD_URL'],
            license=ldict['LICENSE'],
            classifiers=ldict['CLASSIFIERS'],
            author=ldict['AUTHOR'],
            author_email=ldict['AUTHOR_EMAIL'],
            platforms=ldict['PLATFORMS'],
            version=ldict['VERSION'],
            packages=find_packages(exclude=("tests",)),
            install_requires=ldict['REQUIRES'],
            tests_require=ldict['TESTS_REQUIRES'],
            extras_require=ldict['EXTRA_REQUIRES'],
            )


if __name__ == '__main__':
    setup(**opts)
