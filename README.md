# Python 从入门到精通学习项目

## 1. 概述

这是一个系统化的 Python 学习项目，旨在帮助学习者从基础语法逐步掌握到高级编程技能。项目按照难度级别组织学习内容，让学习过程更有序、高效。

## 2. 使用方法

### 2.1 初始化项目

```
# 使用 uv 安装依赖
uv sync

# 或者使用 pip 安装
pip install -e .
```

### 2.2 运行测试

```
# 使用 uv 运行测试
uv run python -m pytest

# 使用 uv 运行测试并生成覆盖率报告
uv run python -m pytest --cov

# 使用 uv 运行测试并生成详细覆盖率报告
uv run python -m pytest --cov --cov-report=html
```

### 2.2 学习路径

项目按以下顺序组织学习内容：

1. `01_basics` - Python 基础语法
2. `02_oop` - 面向对象编程
3. `03_data_processing` - 数据处理与分析
4. `04_advanced` - Python 高级特性
5. `05_concurrency` - 并发编程
6. `06_testing_debugging` - 测试和调试

建议按照上述顺序逐步学习各个模块。

## 3. 开发说明

如需进行开发，建议阅读 [开发文档](./docs/development.md) 了解如何在 IDE 中使用 SRC 布局。

推荐使用 uv 进行依赖管理：
- 安装依赖: `uv sync`
- 添加依赖: `uv add <package>`
- 添加开发依赖: `uv add --dev <package>`
- 运行测试: `uv run python -m pytest`
- 运行带覆盖率的测试: `uv run python -m pytest --cov`
- 构建项目: `uv build`
- 发布项目: `uv publish`

## 4. 学习建议

建议按照以下步骤进行学习：

1. 先运行项目确保环境配置正确
2. 按照目录编号顺序学习各模块内容
3. 每个模块都配有示例代码，建议动手实践
4. 遇到问题时参考对应模块的注释和文档

Python 项目工程化开发指南：https://pyloong.github.io/pythonic-project-guidelines/quick_start/#15