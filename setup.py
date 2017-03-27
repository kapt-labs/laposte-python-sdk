from setuptools import setup

setup(
    name='lapostesdk',
    version='0.1.1',
    author='Guillaume Luchet',
    author_email='guillaume@geelweb.org',
    packages=['lapostesdk', 'lapostesdk.apis'],
    url='https://github.com/geelweb/laposte-python-sdk',
    download_url='https://github.com/geelweb/laposte-python-sdk/archive/0.1.1.tar.gz',
    description='La Poste SDK',
    install_requires=[
        'requests>=2.4.3'
    ],
    keywords='api sdk laposte'
)
