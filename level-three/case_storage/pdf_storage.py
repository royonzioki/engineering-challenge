from case_model.case_judgment import Judgment
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os
import re


class PDFStore:
    def __init__(self, base_dir):
        os.makedirs(base_dir, exist_ok=True)
        self.base_dir = base_dir

        font_path = os.path.join(os.path.dirname(__file__), "DejaVuSans.ttf")
        pdfmetrics.registerFont(TTFont("DejaVu", font_path))

    def store(self, judgment: Judgment):
        safe = re.sub(r"[^\w\-_.]", "_", judgment.case_id)
        path = os.path.join(self.base_dir, f"{safe}.pdf")

        c = canvas.Canvas(path, pagesize=A4)
        width, height = A4
        x, y = 40, height - 40
        lh = 14

        c.setFont("DejaVu", 10)

        # Metadata
        meta = [
            f"Case ID: {judgment.case_id}",
            f"Title: {judgment.title}",
            f"Court: {judgment.court}",
            f"Judges: {judgment.judges}",
            f"Date: {judgment.judgment_date}",
            f"Parties: {judgment.parties}",
        ]

        for line in meta:
            for w in simpleSplit(line, "DejaVu", 10, width - 80):
                c.drawString(x, y, w)
                y -= lh
            y -= 6

        c.drawString(x, y, "---- JUDGMENT TEXT ----")
        y -= lh * 2

        for para in judgment.text.split("\n\n"):
            for line in simpleSplit(para, "DejaVu", 10, width - 80):
                if y < 40:
                    c.showPage()
                    c.setFont("DejaVu", 10)
                    y = height - 40
                c.drawString(x, y, line)
                y -= lh
            y -= lh

        c.save()
        print(f"Saved PDF → {path}")
