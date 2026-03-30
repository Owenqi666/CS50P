from fpdf import FPDF

name = input("Name: ")

pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=False)

pdf.set_font("Helvetica", "B", 36)
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 50, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")

pdf.image("shirtificate.png", x=25, y=60, w=160)

pdf.set_font("Helvetica", "B", 24)
pdf.set_text_color(255, 255, 255)
pdf.set_y(140)
pdf.cell(0, 10, f"{name} took CS50", align="C")

pdf.output("shirtificate.pdf")