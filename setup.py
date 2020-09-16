import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="pytorch_object_detection_utils",
    version="0.0.1",
    author="Grzegorz Gwardys",
    author_email="grzegorz.gwardys@promity.pl",
    description="plug-able utils for Deep Learning practitioners for object detection tasks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hrehory/pytorch-object-detection-utils",
    packages=setuptools.find_packages(),
    classifiers=[],
    install_requires=['torch', 'torchvision', 'cython', 'pycocotools', 'matplotlib']
)
