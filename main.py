# coding=UTF-8
#
#
import pymysql
import pandas as pd
from sqlalchemy import create_engine
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from work import db


pymysql . install_as_MySQLdb()
engine = create_engine(db, encoding='ascii')
info = pd.read_sql_query(f"SELECT * FROM log_doс;", engine)

info_data = []
for i in range(len(info)):
    doc_id = str(info.loc[i, 'doc_id'])
    text = str(info.loc[i, 'text'])
    user_name = str(info.loc[i, 'user_name'])
    date_time = str(info.loc[i, 'date_time'])
    info_data_row = [i+1, date_time, text, user_name, doc_id]
    info_data.append(info_data_row)

pdfmetrics.registerFont(TTFont('bold', 'Lora-Bold.ttf'))
pdfmetrics.registerFont(TTFont('regular', 'Lora-Regular.ttf'))

doc = SimpleDocTemplate("log_doc.pdf", pagesize=letter)
elements = []
styleSheet = getSampleStyleSheet()
t=Table(info_data)
t.setStyle(TableStyle([('ALIGN',(1,1),(-2,-2),'RIGHT'),
('VALIGN',(0,0),(0,-1),'TOP'),
('ALIGN',(0,-1),(-1,-1),'CENTER'),
('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
('BOX', (0,0), (-1,-1), 0.25, colors.black),
('FONT', (0,0), (-1,-1), 'regular')
]))
elements.append(t)
# write the document to disk
doc.build(elements)
