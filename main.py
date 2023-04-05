from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    # RGB colour
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="Left",
             ln=1)
    # x1=10, y1=21, x2=200, y2=21 -> length of A4 size paper(210)
    pdf.line(10, 21, 200, 21)

    for i in range(row["Pages"] - 1):
        pdf.add_page()

pdf.output("output.pdf")
