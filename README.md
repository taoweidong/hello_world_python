# Hello_World_Python


## 1. Overview

My Awesome Project!

## 2. Usage

### 2.1 init project

```
 
# (推荐使用 Poetry ，既包含了虚拟环境管理工具也支持打包发布等功能。)
# (在安装好 Python 环境后，应该在全局环境中安装 Poetry 。python -m pip install -U pip)
pip install -U poetry
#安装 cookiecutter
pip3 install -U cookiecutter
#初始化项目
cd workspace
cookiecutter https://github.com/pyloong/cookiecutter-pythonic-project

# 安装 virtualenv 虚拟环境管理工具
pip install virtualenv
# 使用 virtualenv 创建虚拟环境
virtualenv .venv
# 进入虚拟环境中
source .venv/bin/activate

#使用 poetry 初始化一个虚拟环境。
poetry install -v
#安裝项目依赖
poetry install

# 执行 tox ，验证项目完整性
tox
```

### 2.2 usage

TODO

## 3. Develop

You may need to read the [develop document](./docs/development.md) to use SRC Layout in your IDE.


## 4. FAQ
Python 项目工程化开发指南：https://pyloong.github.io/pythonic-project-guidelines/quick_start/#15
