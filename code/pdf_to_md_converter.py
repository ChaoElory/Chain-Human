#!/usr/bin/env python3
"""
批量转换中外顶刊PDF为Markdown文件
使用PyMuPDF (fitz) 提取文本和表格
"""
import fitz
import os
import re
import sys
import time

# 路径配置
SRC_DIR = r"E:\Obsidian Wiki\Chain-Human\raw\00-仅存档不纳入\学术论文\中外顶刊文献集合"
OUT_DIR = r"E:\Obsidian Wiki\Chain-Human\中外顶刊文献md集合"

os.makedirs(OUT_DIR, exist_ok=True)

def extract_tables_as_md(page):
    """尝试提取表格并转为Markdown格式"""
    tables = page.find_tables()
    md_tables = []
    if tables and tables.tables:
        for t_idx, table in enumerate(tables.tables):
            data = table.extract()
            if not data or len(data) < 1:
                continue
            md = []
            # Header row
            header = data[0]
            md.append("| " + " | ".join([str(c or "").replace("\n", " ") for c in header]) + " |")
            md.append("| " + " | ".join(["---"] * len(header)) + " |")
            # Data rows
            for row in data[1:]:
                md.append("| " + " | ".join([str(c or "").replace("\n", " ") for c in row]) + " |")
            md_tables.append("\n".join(md))
    return md_tables

def clean_text(text):
    """清理提取的文本"""
    # 合并孤立换行（中文语境下）
    lines = text.split("\n")
    cleaned = []
    for line in lines:
        line = line.strip()
        if line:
            cleaned.append(line)
    return "\n".join(cleaned)

def convert_pdf_to_md(pdf_path):
    """将单个PDF转为Markdown文本"""
    filename = os.path.basename(pdf_path)
    stem = os.path.splitext(filename)[0]
    # 仅去除文件名末尾的 (1) 或 (2) 等重复标记（含括号的）
    stem_clean = re.sub(r'\s*\(\d+\)\s*$', '', stem).strip()
    
    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        return None, f"无法打开PDF: {e}"
    
    md_parts = []
    md_parts.append(f"# {stem_clean}")
    md_parts.append(f"")
    md_parts.append(f"> **源文件**: {filename}")
    md_parts.append(f"> **页数**: {len(doc)}")
    md_parts.append(f"")
    md_parts.append("---")
    md_parts.append("")
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        
        # 提取文本
        text = page.get_text("text")
        text_clean = clean_text(text)
        
        # 提取表格
        md_tables = extract_tables_as_md(page)
        
        # 获取图片信息
        images = page.get_images()
        
        # 写入页面内容
        md_parts.append(f"## 第 {page_num+1} 页")
        md_parts.append("")
        
        if text_clean:
            md_parts.append(text_clean)
            md_parts.append("")
        
        # 插入表格（如果表格内容与文本不重复）
        for t_md in md_tables:
            md_parts.append(t_md)
            md_parts.append("")
        
        if images:
            md_parts.append(f"*（本页包含 {len(images)} 张图片，请参阅原PDF）*")
            md_parts.append("")
        
        md_parts.append("---")
        md_parts.append("")
    
    doc.close()
    return "\n".join(md_parts), None

def main():
    # 获取所有PDF文件
    pdf_files = [f for f in os.listdir(SRC_DIR) if f.lower().endswith('.pdf')]
    pdf_files.sort()
    
    if not pdf_files:
        print("未找到PDF文件！")
        return
    
    print(f"共找到 {len(pdf_files)} 个PDF文件")
    print(f"输出目录: {OUT_DIR}")
    print("=" * 60)
    
    success = 0
    failed = 0
    start_time = time.time()
    
    for i, pdf_file in enumerate(pdf_files, 1):
        pdf_path = os.path.join(SRC_DIR, pdf_file)
        stem = os.path.splitext(pdf_file)[0]
        # 仅去除文件名末尾的 (1) 或 (2) 等重复标记
        stem_clean = re.sub(r'\s*\(\d+\)\s*$', '', stem).strip()
        out_path = os.path.join(OUT_DIR, f"{stem_clean}.md")
        
        # 处理同名冲突（如 张涛 和 张涛 (1)）
        if os.path.exists(out_path):
            stem_clean = f"{stem_clean}_{i}"
            out_path = os.path.join(OUT_DIR, f"{stem_clean}.md")
        
        print(f"[{i}/{len(pdf_files)}] {pdf_file} ... ", end="", flush=True)
        
        md_content, error = convert_pdf_to_md(pdf_path)
        
        if error:
            print(f"✗ {error}")
            failed += 1
            continue
        
        try:
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(md_content)
            print(f"✓ -> {os.path.basename(out_path)} ({len(md_content)} chars)")
            success += 1
        except Exception as e:
            print(f"✗ 写入失败: {e}")
            failed += 1
    
    elapsed = time.time() - start_time
    print("=" * 60)
    print(f"完成！成功: {success}, 失败: {failed}, 耗时: {elapsed:.1f}秒")

if __name__ == "__main__":
    main()
