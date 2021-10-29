from setuptools import setup
setup(
    # Name of the module
    name='rumble',
    version='1.15.0',
    # Details
    description='IPython wrapper to use the Rumble framework.',
    # The project's main homepage.
    url='https://github.com/RumbleDB/rumble',
    # Author details
    author='Alexandru Meterez',
    author_email='alexandrumeterez@gmail.com',
    # License
    license='Apache License 2.0',
    py_modules=['rumble'],
    keywords='rumble jsoniq IPython jupyter',
    classifiers=[
        # Intended Audience.
        'Intended Audience :: Developers',
        # Operating Systems.
        'Operating System :: OS Independent',
    ],
    install_requires=['requests', 'jupyter'],
)