from setuptools import find_packages, setup

setup(
    name='BMI_IDAP',
    packages=find_packages(),
    version='0.1.0',
    description="BMI interday analysis pipeline",
    author='Rich Hakim',
    license='MIT',
    install_requires=['numpy==1.18.3',
                      'jupyterlab',
                      'opencv-python',
                      'imageio==2.9.0',
                      'matplotlib',
                      'scikit-learn',
                      'scikit-image',
                      'librosa',
                      'pyyaml',
                      'imageio-ffmpeg',
                      'tqdm',
                      'h5py==2.10.0',
                      'pynwb',
                      'ipywidgets',
                      'pytest',
                      'Pillow==9.3.0'
                      ]
)

# from distutils.core import setup

# setup(
#     name='BMI_IDAP',
#     version='0.1.0',
#     packages=['bmi_idap',],
#     license='MIT',
#     long_description=open('README.md').read(),
# )