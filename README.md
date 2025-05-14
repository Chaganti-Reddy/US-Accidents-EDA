<h1 align="center">US Accidents EDA</h1>

<div align= "center"><img src="assets/cover.jpg" width="400" height="250"/>
  <h4>Doing Exploratory Analysis is most important thing for a Machine Learning Engineer or a Data Scientist. In this Porject we did EDA on US Accidents from 2016-2022 over 2.8 million data.</h4>
</div>

<br/>

<div align="center">
    <!-- Python version -->
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-v3.8-blue?style=flat-square"/></a>
    <!-- Last commit -->
    <img src="https://img.shields.io/github/last-commit/Chaganti-Reddy/US-Accidents-EDA"/>
    <!-- Stars -->
    <img src="https://img.shields.io/github/stars/Chaganti-Reddy/US-Accidents-EDA?style=social"/>
    <!-- Forks -->
    <img src="https://img.shields.io/github/forks/Chaganti-Reddy/US-Accidents-EDA?style=social"/>
    <!-- Open Issues -->
    <a href="https://github.com/Chaganti-Reddy/US-Accidents-EDA/issues"><img src="https://img.shields.io/github/issues/Chaganti-Reddy/US-Accidents-EDA"/></a>
</div>

<br/>

# Table of Contents 

- [Table of Contents](#table-of-contents)
- [:warning: Frameworks and Libraries](#warning-frameworks-and-libraries)
- [:file_folder: Datasets](#file_folder-datasets)
  - [🔄 Source](#-source)
  - [📈 Visualising data](#-visualising-data)
- [:book: Data Preprocessing](#book-data-preprocessing)
- [:link: Download](#link-download)
- [:key: Prerequisites](#key-prerequisites)
- [🚀&nbsp; Installation](#-installation)
- [:bulb: How to Run](#bulb-how-to-run)
- [📂 Directory Tree](#-directory-tree)
- [:key: Results](#key-results)
- [:clap: And it's done!](#clap-and-its-done)
- [:raising_hand: Citation](#raising_hand-citation)
- [:heart: Owner](#heart-owner)
- [:eyes: License](#eyes-license)

<br/>

# :warning: Frameworks and Libraries

- **[Pytorch](https://pytorch.org/):** An open source machine learning framework that accelerates the path from research prototyping to production deployment.
- **[Matplotlib](https://matplotlib.org/) :** Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.
- **[Numpy](https://numpy.org/):**
  Caffe-based Single Shot-Multibox Detector (SSD) model used to detect faces
- **[Pandas](https://pandas.pydata.org/):**
  pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.

<br/>

# :file_folder: Datasets

## 🔄 Source

This Dataset is downloaded from the kaggle repository.

Link to the kaggle repository: https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents

<br/>

## 📈 Visualising data

<br/>

<p align="center">
  <img src="./assets/2.png" />
</p>

<br/>

# :book: Data Preprocessing

Data pre-processing is an important step for the creation of a machine learning
model. Initially, data may not be clean or in the required format for the model which
can cause misleading outcomes. In pre-processing of data, we transform data into our
required format. It is used to deal with noises, duplicates, and missing values of the
dataset. Data pre-processing has the activities like importing datasets, splitting
datasets, attribute scaling, etc. Preprocessing of data is required for improving the
accuracy of the model.

<br/>

# :link: Download

The dataset is now available [here](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents) !

<br/>

# :key: Prerequisites

All the dependencies and required libraries are included in the file <code>requirements.txt</code> [See here](requirements.txt)

<br/>

# 🚀&nbsp; Installation

The Code is written in Python 3.7. If you don&rsquo;t have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:

1. Clone the repo

```bash
git clone https://github.com/Chaganti-Reddy/US-Accidents-EDA.git
```

2. Change your directory to the cloned repo

```bash
cd US-Accidents-EDA
```

Before running the command copy the downloaded dataset folder to face-mask-detector folder...

3. Now, run the following command in your Terminal/Command Prompt to install the libraries required

```bash
python3 -m virtualenv my_env

source my_env/bin/activate

pip3 install -r requirements.txt

```

<br/>

# :bulb: How to Run

1. Open terminal. Go into the cloned project directory and type the following command:

```bash
jupyter notebook
```

2. And then open the .ipynb file and run them in jupyter notebook.

<br/>

# 📂 Directory Tree

```
├── assets
│   ├── 2.png
│   ├── cover.jpg
│   └── results.png
├── LICENSE
├── README.md
├── requirements.txt
├── US_Accidents_EDA.ipynb
└── US_Accidents_EDA.py
```

<br/>

# :key: Results

<br/>

<p align="center">
  <img src="./assets/results.png" />
</p>

<br/>

# :clap: And it's done!

Feel free to mail me for any doubts/query
:email: chagantivenkataramireddy1@gmail.com

---

# :raising_hand: Citation

You are allowed to cite any part of the code or our dataset. You can use it in your Research Work or Project. Remember to provide credit to the Maintainer Chaganti Reddy by mentioning a link to this repository and his GitHub Profile.

Follow this format:

- Author's name - Chaganti Reddy
- Date of publication or update in parentheses.
- Title or description of document.
- URL.

# :heart: Owner

Made with :heart:&nbsp; by [Chaganti Reddy](https://github.com/Chaganti-Reddy/)

# :eyes: License

MIT © [Chaganti Reddy](https://github.com/Chaganti-Reddy/US-Accidents-EDA/blob/main/LICENSE)
