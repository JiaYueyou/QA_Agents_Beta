# QA_Agents

QA_Agents 是一个基于多Agent协作的智能问答系统，能够处理用户的各类问题，包括知识库查询、推理分析和闲聊等。系统采用模块化设计，各Agent分工明确，协同工作，提供高质量的回答。

## 核心功能

- **智能问题分类**：自动判断用户问题类型，选择合适的处理流程
- **知识库检索**：基于FAISS向量数据库的高效检索
- **多Agent协作**：Intake、Retrieval、Reasoning、Validation、Output五大Agent协同工作
- **答案验证**：确保回答的准确性和可靠性
- **专业输出格式**：将回答整理为清晰、专业、有结构的企业风格
- **支持多种文档格式**：PDF、Word、Markdown、TXT等

## 技术栈

- **大语言模型**：OpenAI GPT系列
- **框架**：LangChain
- **向量数据库**：FAISS
- **嵌入模型**：OpenAI Embeddings
- **UI框架**：Streamlit (可选)

## 项目结构

```
QA_Agents/
├── agents/                # 各Agent实现
│   ├── intake_agent.py    # 问题分类Agent
│   ├── retrieval_agent.py # 知识库检索Agent
│   ├── reasoning_agent.py # 推理分析Agent
│   ├── validation_agent.py # 答案验证Agent
│   └── output_agent.py    # 输出优化Agent
├── data/                  # 知识库文档
├── rag/                   # RAG相关模块
│   ├── vectorstore/       # 向量数据库存储
│   ├── build_faiss_db.py  # 构建向量数据库脚本
│   ├── loader.py          # 文档加载器
│   ├── splitter.py        # 文本分割器
│   └── vectorstore.py     # 向量数据库操作
├── tools/                 # 工具模块
│   └── rag_tool.py        # RAG工具
├── ui/                    # Web UI界面
│   └── app.py             # Streamlit应用
├── config.py              # 配置文件
└── main.py                # 主程序入口
```

## 部署实现

### 1. 环境要求

- Python 3.8+ 
- pip 20.0+ 

### 2. 安装依赖

```bash
# 安装基础依赖
pip install langchain langchain-openai openai faiss-cpu

# 安装文档处理依赖
pip install pypdf unstructured docx2txt

# 安装UI依赖（可选）
pip install streamlit
```

### 3. 配置设置

修改 `config.py` 文件，配置OpenAI API信息：

```python
# OpenAI API配置
OPENAI_API_KEY = "your-api-key-here"  # 替换为你的OpenAI API密钥
OPENAI_BASE_URL = "https://api.openai-proxy.org/v1"  # 根据需要修改

# 模型配置
MODEL_NAME = "gpt-4o-mini"  # 主模型
EMBEDDING_MODEL_NAME = "text-embedding-3-small"  # 嵌入模型

# 文本分割配置
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# FAISS 向量数据库保存路径
VECTOR_DB_PATH = "rag/vectorstore/faiss_index"
```

### 4. 知识库构建

1. 将需要放入知识库的文档放入 `data/` 目录，支持PDF、Word、Markdown、TXT等格式

2. 运行构建向量数据库脚本：

```bash
python rag/build_faiss_db.py
```

该脚本将：
- 加载 `data/` 目录中的所有文档
- 对文档进行切分
- 构建FAISS向量数据库
- 保存到 `rag/vectorstore/faiss_index` 目录

### 5. 系统启动

#### 命令行REPL模式

```bash
python main.py
```

启动后，你可以在命令行中输入问题，系统将返回回答。

#### Web UI模式（可选）

```bash
streamlit run ui/app.py
```

启动后，在浏览器中访问 `http://localhost:8501` 即可使用Web界面。

## 使用指南

### 命令行REPL模式

1. 启动系统：`python main.py`
2. 在命令行中输入你的问题
3. 系统将显示处理流程，并输出最终回答

示例：

```
请输入你的问题：什么是LangChain？

[1] Intake Agent 判断用户问题类型...
[2] Retrieval Agent 检索知识库中...
[3] Reasoning Agent 推理中...
[4] Validation Agent 校验中...
[5] Output Agent 输出中...

=== 最终回答 ===
LangChain是一个用于构建基于大语言模型的应用程序的框架，它提供了一系列工具、组件和接口，简化了从单一LLM调用到复杂多步骤工作流的开发过程。
```

### Web UI模式

1. 启动Web服务：`streamlit run ui/app.py`
2. 在浏览器中访问 `http://localhost:8501`
3. 在输入框中输入你的问题，点击"提交"按钮
4. 系统将在右侧显示处理流程和最终回答

## 系统工作流程

### 多Agent协作流程

1. **Intake Agent**：接收用户问题，判断问题类型（use_rag / reason / chitchat）
2. **Retrieval Agent**：如果需要查询知识库，调用RAG工具检索相关内容
3. **Reasoning Agent**：根据检索结果（如果有）和用户问题，生成初步回答
4. **Validation Agent**：检查回答是否存在无依据内容、逻辑错误、幻觉等问题
5. **Output Agent**：将回答整理为清晰、专业、有结构的企业风格

### 各Agent职责说明

| Agent名称 | 职责 | 输出 |
|----------|------|------|
| Intake Agent | 判断用户问题类型 | use_rag / reason / chitchat |
| Retrieval Agent | 检索知识库内容 | 检索结果 |
| Reasoning Agent | 推理分析，生成回答 | 初步回答 |
| Validation Agent | 验证回答准确性 | VALID / 问题列表 |
| Output Agent | 优化回答格式 | 最终回答 |

## 扩展与维护

### 添加新文档

1. 将新文档放入 `data/` 目录
2. 重新运行构建向量数据库脚本：`python rag/build_faiss_db.py`

### 修改配置

修改 `config.py` 文件中的相应参数：

- 修改模型：更改 `MODEL_NAME` 和 `EMBEDDING_MODEL_NAME`
- 修改文本分割：调整 `CHUNK_SIZE` 和 `CHUNK_OVERLAP`
- 修改向量数据库路径：更改 `VECTOR_DB_PATH`

### 自定义Agent

1. 在 `agents/` 目录下创建新的Agent文件
2. 实现Agent的核心逻辑
3. 在 `main.py` 中集成该Agent到工作流程中

## 常见问题

### Q: 构建向量数据库时提示"路径不存在"

A: 请检查 `data/` 目录是否存在，以及目录中是否有文档。

### Q: 运行时提示"ModuleNotFoundError"

A: 请确保已安装所有依赖，使用 `pip install` 命令安装缺失的模块。

### Q: 回答不准确或不相关

A: 请检查：
1. 知识库中是否包含相关文档
2. 向量数据库是否已重新构建
3. 问题类型判断是否正确

### Q: Web UI无法启动

A: 请确保已安装streamlit，使用 `pip install streamlit` 命令安装。

## 许可证

MIT License

## 贡献

欢迎提交Issue和Pull Request！

## 联系方式

如有问题或建议，请联系项目维护者。
