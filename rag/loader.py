# loader.py
"""
文档加载模块：
自动加载 data/ 目录下多类型文档（PDF/Word/Markdown/TXT）
优化日志打印和空文档过滤
支持相对路径（相对于项目根目录）
"""

from pathlib import Path
from langchain_community.document_loaders import (
    PyPDFLoader,
    UnstructuredWordDocumentLoader,
    UnstructuredMarkdownLoader,
    TextLoader
)


def load_documents(path="data"):
    """
    根据文件类型自动选择 Loader，返回 Document 列表
    参数：
        path (str): 数据目录路径，相对路径会自动相对于项目根目录
    返回：
        docs (list[Document]): 已加载文档块列表
    """
    docs = []

    project_root = Path(__file__).parent.parent  # Enterprise_Agents/
    data_path = (project_root / path).resolve()  # 转为绝对路径
    print(f"[Loader] 加载文档目录：{data_path}")

    if not data_path.exists():
        print(f"[Error] 路径不存在：{data_path}")
        return docs

    # 遍历文件并加载
    for file_path in data_path.rglob("*.*"):
        suffix = file_path.suffix.lower()
        loader = None

        if suffix == ".pdf":
            loader = PyPDFLoader(str(file_path))
        elif suffix in [".docx", ".doc"]:
            loader = UnstructuredWordDocumentLoader(str(file_path))
        elif suffix == ".md":
            loader = UnstructuredMarkdownLoader(str(file_path))
        elif suffix == ".txt":
            loader = TextLoader(str(file_path), encoding="utf-8")
        else:
            print(f"[Warning] 未识别文件类型，跳过: {file_path}")
            continue

        loaded_docs = loader.load()
        if len(loaded_docs) == 0:
            print(f"[Warning] 文件加载为空: {file_path}")
        else:
            docs.extend(loaded_docs)
            print(f"[Loader] 文件加载成功: {file_path} → {len(loaded_docs)} 块文档")

    print(f"[Loader] 总共加载 {len(docs)} 个文档块")
    return docs
