from setuptools import setup

description = 'crnn_pytorch'
setup(
    name="crnn_pytorch",
    version="0.1",
    author_email="mehdicherti@gmail.com",
    description=description,
    zip_safe=False,  # the package can run out of an .egg file
    classifiers=['Intended Audience :: Science/Research',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved',
                 'Programming Language :: Python',
                 'Topic :: Software Development',
                 'Topic :: Scientific/Engineering',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: POSIX',
                 'Operating System :: Unix',
                 'Operating System :: MacOS'],
    platforms='any',
)
