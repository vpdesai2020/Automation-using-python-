#Author : Vasanth Kumar Desai

#Requirements
#pip install fpdf

#---------------------------------------------------------------------#



from fpdf import FPDF

def pdf_conv():
    pdf=FPDF()
    #Page 1
    pdf.add_page()
    pdf.Bookmark('Page 1')#add Bookmark to the page
    pdf.set_font('Times','B',14)
    pdf.cell(200,10,txt="Page 1 ", ln=1, align="C")
    pdf.cell(200,10,txt="This is the second line", ln=2, align="C")

    #Page 2
    pdf.add_page()
    pdf.Bookmark('Page 2')
    pdf.set_font('Arial','B',14)
    pdf.cell(200,10,txt="Page 2", ln=1, align="C")
    pdf.cell(200,10,txt="This is the second line", ln=2, align="C")

    pdf.output("text_to_pdf.pdf",'F')

pdf_conv()
