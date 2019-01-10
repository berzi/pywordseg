import setuptools


setuptools.setup(
  name="pywordseg",
  version="0.0.1",
  author="Jexus Chuang",
  description="Open-source state-of-the-art Chinese word segmentation toolkit",
  url="https://github.com/voidism/pywordseg",
  packages=setuptools.find_packages(),
  license='MIT',
  install_requires=[
    "torch",
    "h5py",
    "numpy",
    "overrides",
  ],
  classifiers=[
    "Development Status :: 2 - Pre-Alpha",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.6",
  ],
  include_package_data=True
)