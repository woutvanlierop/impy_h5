import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="impy",
    version="0.1",
    author="Rodrigo Alejandro Loza Lucero",
    author_email="lozuwaucb@gmail.com",
    description="A library to apply data augmentation to your image datasets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lozuwa/impy",
    packages=['impy'],
    install_requires=[
        'bleach==3.3.0',
        'certifi==2021.10.8',
        'chardet==4.0.0',
        'docutils==0.14',
        'idna==2.10',
        'numpy==1.19.3',
        'opencv-python==4.5.5.62',
        'python-interface==1.4.0',
        'readme-renderer==24.0',
        'Pygments==2.4.1',
        'setuptools==52.0.0',
        'six==1.15.0',
        'tqdm==4.59.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: APACHE",
        "Operating System :: OS Independent",
    ],
)
