import setuptools 

with open("README.md","r",encoding = "utf-8") as f:
    long_description = f.read()


_version_= "0.0.0"

REPO_NAME = "DsThakurRawat-AIML-IN-PRODUCTION-1-.-teXti"
AUTHOR_USER_NAME = "DsThakurRawat"
SRC_REPO = "textsummarizer"
AUTHOR_EMAIL =  "divyanshrawatofficial@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Python package for NLP-based text summarization using Hugging Face Transformers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[]  # or list your dependencies here
)