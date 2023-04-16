import os
import sys
from PIL import Image
from pathlib import Path
from PyPDF2 import PdfWriter,PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
file=''
is_start_end=False
start=0
endp=0
logo_file='logo.png'
def split_pdf():
    read_file = PdfReader(open(file,"rb")) #read pdf
    print(len(read_file.pages))
    print(os.path.dirname(file))
    name, ext = os.path.splitext(file)
    if not os.path.exists(name):
        os.mkdir(name)
    
    global endp
    if endp==0:
        endp=len(read_file.pages)
    if endp>len(read_file.pages):
        endp=len(read_file.pages)
    global start
    if start<0:
        start=0
    if start >0:
        start-=1
    
    for i in range(start,endp):
        npdf=PdfWriter()
        page=read_file.pages[i]
        #npdf.pages.append(page)
        npdf.add_page(page)
        npdf.write(os.path.join(name,str(i+1)+".pdf"))

def add_whater_mark():
   
    current_dir=os.path.dirname(file)
    makeWatermark(current_dir)
    print(Path(file).name)
    name, ext = os.path.splitext(Path(file).name)
    print(name)
    logo_image=Image.open(os.path.join(current_dir, logo_file))
   
    logo_image.save(os.path.join(current_dir,"logo.pdf"))
    read_file = PdfReader(open(file,"rb")) #read pdf
    wtermark_file = PdfReader(open(os.path.join(current_dir,"watermark.pdf"),"rb")) #read pdf
    page_mark=wtermark_file.pages[0]
    merged=PdfWriter()
    for i in range(len(read_file.pages)):
        page=read_file.pages[i]
        page.merge_page(page_mark)
        merged.add_page(page)
    merged.write(os.path.join(current_dir,name+"_merged.pdf"))
def makeWatermark(current_dir):
    text = "Mohamed Gamal"
    pdf = canvas.Canvas(os.path.join(current_dir,"watermark.pdf"), pagesize=A4)
    pdf.translate(inch, inch)
    pdf.setFillColor(colors.grey, alpha=0.1)
    pdf.setFont("Helvetica", 50)
    #pdf.rotate(45)
    pdf.drawImage(os.path.join(current_dir, logo_file),0,200,448,350)
    pdf.save()