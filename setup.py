from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(
    name='PycklePi',
    version='1.4', # Stable Release
    description="PycklePi is a small, in-dev module for controlling buttons, LED's, buzzers and more on the Raspberry Pi.",
    url='https://github.com/filip-school/PycklePi',
    download_url="https://github.com/filip-school/PycklePi",
    author='Filip',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email='filip.herle@gmail.com', # Please don't email me lol
    keywords='raspberry-pi development python GPIO', # Tags
    python_requires='~=3.3',
    install_requires=[
        "RPi.GPIO>=0.6.3",
        "docutils>=0.3",
        "wheel",
    ],
    classifiers=[
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          "Operating System :: OS Independent",
          'License :: OSI Approved :: Python Software Foundation License',
    ]
)
