"""OCR批量处理第10-12章图片型PDF - 150DPI加速版"""
import fitz, os, sys, time, numpy as np
from PIL import Image
import easyocr

BASE_DIR = "E:/Obsidian Wiki/供应链重建研究-Human/raw/papers/2025年世界开放报告"
CHAPTER_NAMES = {10: "全球开放合作与经济安全", 11: "中国制度型开放", 12: "专题分析与展望"}

def ocr_page(reader, img):
    result = reader.readtext(img, paragraph=False)
    lines = []
    for item in result:
        if len(item) == 3:
            lines.append(item[1])
        else:
            lines.append(item[1])
    return "\n".join(lines)

def process_chapter(ch, reader):
    pdf_path = os.path.join(BASE_DIR, f"第{ch}章.pdf")
    md_path = os.path.join(BASE_DIR, f"第{ch}章.md")
    doc = fitz.open(pdf_path)
    total = len(doc)
    print(f"\n开始处理 第{ch}章 ({CHAPTER_NAMES[ch]}) — 共{total}页")
    
    md = []
    md.append("---")
    md.append(f"title: 第{ch}章 {CHAPTER_NAMES[ch]}")
    md.append("source: 《2025年世界开放报告》")
    md.append("type: raw-material")
    md.append("status: unverified")
    md.append("ocr: easyocr(ch_sim+en)")
    md.append("---")
    md.append("")
    md.append(f"> **来源**: 《2025年世界开放报告》第{ch}章（共{total}页）")
    md.append("> **提取日期**: 2026-07-19 | **方式**: EasyOCR 图片识别 | **状态**: ⚠️ OCR未校对，以PDF原件为准")
    md.append("")
    
    start = time.time()
    for p in range(total):
        t0 = time.time()
        page = doc[p]
        pix = page.get_pixmap(dpi=150)  # 150DPI加速
        img = np.array(Image.frombytes("RGB", [pix.width, pix.height], pix.samples))
        text = ocr_page(reader, img)
        md.append(f"\n## 第{p+1}页\n")
        md.append(text)
        elapsed = time.time() - t0
        total_t = time.time() - start
        remaining = (total_t / (p+1)) * (total - p - 1)
        print(f"  第{p+1}/{total}页 — {elapsed:.0f}s — 累计{total_t:.0f}s — 剩余{remaining:.0f}s")
        sys.stdout.flush()
    
    doc.close()
    content = "\n".join(md)
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(content)
    total_t = time.time() - start
    print(f"✅ 第{ch}章完成 — {total_t:.0f}s ({total_t/60:.1f}min) — {len(content)}字符")

def main():
    reader = easyocr.Reader(['ch_sim', 'en'], gpu=False)
    for ch in [10, 11, 12]:
        process_chapter(ch, reader)
    print("\n全部完成！")

if __name__ == "__main__":
    main()
