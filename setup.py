from setuptools import setup

setup(
    name='lapostesdk',
    version='0.1',
    author='Guillaume Luchet',
    author_email='guillaume@geelweb.org',
    packages=['lapostesdk', 'lapostesdk.apis'],
    url='http://pypi.python.org/pypi/lapostesdk',
    description='La Poste SDK',
    long_description=open('README.md').read(),
    install_requires=[
        'requests>=2.4.3'
    ],
    keywords='api sdk laposte'
)
