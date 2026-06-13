from fpdf import FPDF


class RapportPDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 14)
        self.set_fill_color(31, 73, 125)
        self.set_text_color(255, 255, 255)
        self.cell(0, 12, "RAPPORT DE CONFORMITE PRUDENTIELLE", align="C", fill=True)
        self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(128)
        self.cell(0, 10, f"Page {self.page_no()} - Confidentiel", align="C")


def sauvegarder_pdf(rapport: dict, chemin: str) -> None:
    pdf = RapportPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Infos banque
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(0)
    pdf.cell(0, 8, f"Etablissement : {rapport['banque']}", ln=True)
    pdf.cell(0, 8, f"Periode : {rapport['periode']}", ln=True)
    pdf.cell(0, 8, f"Date : {rapport['date_rapport']}", ln=True)
    pdf.ln(6)

    # Tableau
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_fill_color(31, 73, 125)
    pdf.set_text_color(255, 255, 255)
    col_widths = [80, 30, 40, 35]
    headers = ["Ratio", "Valeur", "Seuil", "Statut"]
    for w, h in zip(col_widths, headers):
        pdf.cell(w, 9, h, border=1, align="C", fill=True)
    pdf.ln()

    pdf.set_font("Helvetica", size=10)
    for i, r in enumerate(rapport["ratios"]):
        fill = i % 2 == 0
        pdf.set_fill_color(242, 242, 242)
        pdf.set_text_color(0)
        pdf.cell(col_widths[0], 9, r["nom"], border=1, fill=fill)
        pdf.cell(col_widths[1], 9, f"{r['valeur'] * 100:.2f}%", border=1, align="C", fill=fill)
        pdf.cell(col_widths[2], 9, f"{r['seuil'] * 100:.2f}%", border=1, align="C", fill=fill)
        if r["conforme"]:
            pdf.set_text_color(0, 176, 80)
            statut = "CONFORME"
        else:
            pdf.set_text_color(255, 0, 0)
            statut = "NON CONFORME"
        pdf.cell(col_widths[3], 9, statut, border=1, align="C", fill=fill)
        pdf.ln()

    pdf.output(chemin)
