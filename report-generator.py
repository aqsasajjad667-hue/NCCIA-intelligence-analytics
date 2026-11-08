import os
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def generate_pdf_report(data: dict, filename="NCCIA_Daily_Report.pdf"):
    """Generates a professional PDF intelligence report."""
    doc = SimpleDocTemplate(filename, pagesize=letter,
                            rightMargin=40, leftMargin=40,
                            topMargin=40, bottomMargin=40)
    elements = []
    styles = getSampleStyleSheet()

    # Custom Styles
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=colors.HexColor("#1A365D"),
        alignment=1, # Center
        spaceAfter=10
    )
    
    subtitle_style = ParagraphStyle(
        'SubtitleStyle',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor("#4A5568"),
        alignment=1,
        spaceAfter=20
    )

    # Header Elements
    elements.append(Paragraph("NCCIA DAILY INTELLIGENCE REPORT", title_style))
    elements.append(Paragraph(f"Date: {datetime.now().strftime('%0d %B %Y')}", subtitle_style))
    elements.append(Spacer(1, 10))

    # Table Data Construction
    table_data = [
        [Paragraph("<b>Indicator</b>", styles['Normal']), 
         Paragraph("<b>Today's Data</b>", styles['Normal']), 
         Paragraph("<b>Previous Day</b>", styles['Normal'])]
    ]

    indicators = [
        ("Raids", data.get("Raids", "Not Reported")),
        ("Arrests", data.get("Arrests", "Not Reported")),
        ("FIRs", data.get("FIRs", "Not Reported")),
        ("Complaints", data.get("Complaints", "Not Reported")),
        ("Cases Registered", data.get("Cases Registered", "Not Reported")),
        ("Financial Recoveries", data.get("Financial Recoveries", "Not Reported"))
    ]

    for ind, val in indicators:
        table_data.append([
            Paragraph(ind, styles['Normal']),
            Paragraph(str(val), styles['Normal']),
            Paragraph("Not Reported", styles['Normal']) # Placeholder for previous day comparison
        ])

    # Table Styling
    t = Table(table_data, colWidths=[200, 150, 150])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2B6CB0")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('BOTTOMPADDING', (0,0), (-1,0), 8),
        ('BACKGROUND', (0,1), (-1,-1), colors.HexColor("#F7FAFC")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F7FAFC")]),
    ]))

    elements.append(t)
    doc.build(elements)
    print(f"PDF Report successfully generated: {filename}")

if _name_ == "_main_":
    sample_data = {
        "Raids": "Not Reported",
        "Arrests": "Not Reported",
        "FIRs": "Not Reported",
        "Complaints": "Not Reported",
        "Cases Registered": "Not Reported",
        "Financial Recoveries": "Not Reported"
    }
    generate_pdf_report(sample_data)
