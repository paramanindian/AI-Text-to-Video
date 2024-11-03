from setuptools import setup, find_packages

setup(
    name='ai-video-creator',
    version='0.1.0',
    author='Pramod Saini',
    author_email='task@paidanalyst.com',
    description='A Python project for creating AI-generated videos without APIs and Offline on system',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/paramanindian/AI-Text-to-Video',  # Replace with your repo URL
    packages=find_packages(),
    install_requires=[
        'numpy>=1.21.0',
        'opencv-python>=4.5.0',
        'moviepy>=1.0.0',
        'tensorflow>=2.5.0',
        'scikit-learn>=0.24.0',
        'Flask>=2.0.0',
        'pillow',
        'requests'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)