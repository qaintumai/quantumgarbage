# Copyright 2024 The qAIntum.ai Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from setuptools import setup, find_packages

# Read the README file for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="quantum",
    version="0.1.0",
    author="Sophie Choe, Alexander Olivas, Arjun Subedi, Max Ivry, Nikilesh B R",
    author_email="contact@qaintum.ai",
    description="A project containing Quantum Neural Networks and Quantum Transformers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/qaintumai/quantum",  # Updated with your project's URL
    packages=find_packages(include=["src", "src.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Quantum Artificial Intelligence",
    ],
    python_requires=">=3.7",
    install_requires=[
        "annotated-types==0.7.0",
        "antlr4-python3-runtime==4.9.2",
        "appdirs==1.4.4",
        "autograd==1.6.2",
        "autoray==0.6.12",
        "cachetools==5.3.3",
        "certifi==2024.7.4",
        "charset-normalizer==3.3.2",
        "click==8.1.7",
        "cloudpickle==3.0.0",
        "dask==2024.5.2",
        "filelock==3.14.0",
        "fire==0.6.0",
        "fsspec==2024.6.0",
        "future==1.0.0",
        "idna==3.7",
        "importlib_metadata==7.1.0",
        "Jinja2==3.1.5",
        "joblib==1.4.2",
        "lark-parser==0.12.0",
        "llvmlite==0.42.0",
        "locket==1.0.0",
        "MarkupSafe==2.1.5",
        "mpmath==1.3.0",
        "networkx==3.3",
        "numba==0.59.1",
        "numpy==1.23.5",
        "nvidia-cublas-cu12==12.1.3.1",
        "nvidia-cuda-cupti-cu12==12.1.105",
        "nvidia-cuda-nvrtc-cu12==12.1.105",
        "nvidia-cuda-runtime-cu12==12.1.105",
        "nvidia-cudnn-cu12==8.9.2.26",
        "nvidia-cufft-cu12==11.0.2.54",
        "nvidia-curand-cu12==10.3.2.106",
        "nvidia-cusolver-cu12==11.4.5.107",
        "nvidia-cusparse-cu12==12.1.0.106",
        "nvidia-nccl-cu12==2.20.5",
        "nvidia-nvjitlink-cu12==12.5.40",
        "nvidia-nvtx-cu12==12.1.105",
        "packaging==24.0",
        "pandas==2.2.2",
        "partd==1.4.2",
        "PennyLane==0.29.1",
        "PennyLane-Lightning==0.30.0",
        "PennyLane-SF==0.29.1",
        "pillow==10.3.0",
        "pydantic==2.7.3",
        "pydantic-settings==2.3.0",
        "pydantic_core==2.18.4",
        "python-dateutil==2.9.0.post0",
        "python-dotenv==1.0.1",
        "pytz==2024.1",
        "PyYAML==6.0.1",
        "quantum-blackbird==0.5.0",
        "quantum-xir==0.2.2",
        "requests==2.32.3",
        "retworkx==0.14.2",
        "rustworkx==0.14.2",
        "scikit-learn==1.5.0",
        "scipy==1.13.1",
        "semantic-version==2.10.0",
        "six==1.16.0",
        "StrawberryFields==0.23.0",
        "sympy==1.12.1",
        "termcolor==2.4.0",
        "thewalrus==0.21.0",
        "threadpoolctl==3.5.0",
        "toml==0.10.2",
        "toolz==0.12.1",
        "torch==2.3.0",
        "torchvision==0.18.0",
        "triton==2.3.0",
        "typing_extensions==4.12.1",
        "tzdata==2024.1",
        "urllib3==2.2.2",
        "xanadu-cloud-client==0.3.2",
        "zipp==3.19.2"
    ],
    extras_require={
        "dev": [
            "pytest>=6.2.0",
            "flake8>=3.9.0",
            "black>=21.5b0",
            "jupyter>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "train_qnn=scripts.train_qnn:main",
            "train_qtransformer=scripts.train_qtransformer:main",
            "evaluate_model=scripts.evaluate_model:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
