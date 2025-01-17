from distutils.core import setup

setup(
    name="cc3200tool",
    version="1.0.0",
    description="A tool to upload files to TI CC32xx",
    author="Kiril Zyapkov",
    author_email="k.zyapkov@allterco.com",
    url="http://github.com/AlexLisnitski/cc3200tool",
    packages=['cc3200tool'],
    package_data={'cc3200tool': ['dll/*.dll', 'dll/gen2/*.ptc']},
    entry_points = {
        'console_scripts': ['cc3200tool=cc3200tool.cc:main'],
    },
    install_requires=['pyserial'],
)
