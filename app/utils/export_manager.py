"""Export manager for exporting memories to different formats."""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from datetime import datetime
import os


def export_to_pdf(memories, filename='EBATHENJINI_Export.pdf'):
    """Export memories to PDF format.
    
    Args:
        memories: List of memory tuples from database
        filename: Output PDF filename
    """
    doc = SimpleDocTemplate(filename, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()
    
    # Title
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#0080FF'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    title = Paragraph('EBATHENJINI<br/>Memories of Zenande', title_style)
    story.append(title)
    story.append(Spacer(1, 0.3*inch))
    
    # Export date
    date_text = f"Exported on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    date_para = Paragraph(date_text, styles['Normal'])
    story.append(date_para)
    story.append(Spacer(1, 0.5*inch))
    
    # Memories
    for i, memory in enumerate(memories, 1):
        memory_id, title, description, date_created, date_memory, image_path, tags = memory
        
        # Memory title
        memory_title = Paragraph(
            f"<b>Memory #{i}: {title}</b>",
            styles['Heading2']
        )
        story.append(memory_title)
        
        # Date
        memory_date = Paragraph(
            f"<b>Date:</b> {date_memory}",
            styles['Normal']
        )
        story.append(memory_date)
        
        # Tags
        if tags:
            tags_para = Paragraph(
                f"<b>Tags:</b> {tags}",
                styles['Normal']
            )
            story.append(tags_para)
        
        # Image
        if image_path and os.path.exists(image_path):
            try:
                img = Image(image_path, width=4*inch, height=3*inch)
                story.append(img)
            except:
                pass
        
        # Description
        if description:
            desc_para = Paragraph(
                f"<b>Description:</b><br/>{description.replace(chr(10), '<br/>')}",
                styles['Normal']
            )
            story.append(desc_para)
        
        story.append(Spacer(1, 0.3*inch))
        story.append(PageBreak())
    
    # Build PDF
    doc.build(story)
    return filename


def export_to_csv(memories, filename='EBATHENJINI_Export.csv'):
    """Export memories to CSV format.
    
    Args:
        memories: List of memory tuples from database
        filename: Output CSV filename
    """
    import csv
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['ID', 'Title', 'Description', 'Date Created', 'Memory Date', 'Image', 'Tags']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for memory in memories:
            writer.writerow({
                'ID': memory[0],
                'Title': memory[1],
                'Description': memory[2],
                'Date Created': memory[3],
                'Memory Date': memory[4],
                'Image': memory[5],
                'Tags': memory[6]
            })
    
    return filename
