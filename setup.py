from setuptools import setup, find_packages

setup(
    name='shipping-label-processor',
    version='0.1.0',
    author='Andrew Oakes',
    author_email='',
    description='A Python package for processing shipping label PDFs, including cropping, resizing, and rotating.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'PyPDF2',
        'Pillow',
        'reportlab',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)