#!/usr/bin/env python3

from docx import Document
from docx.shared import Inches

doc = Document()

#This function should add one paragraph at a time to the document including a delete character
def addPar(n):
    paragraph = doc.add_paragraph(n)
    doc.save('demo.docx')

addPar(" ASDFOAS ASFFGONASDF  DA SDF SADF ASD GSADF GA SFH")
addPar("A B C D E F C G D A AS SDF ASFG ASDF ASDF HJ TET AS DFAS DF ASFGHAF AS FD ASDF GA SADF")
addPar(" ASDFOAS ASFFGONASDF  DA SDF SADF ASD GSADF GA SFH")
addPar("A B C D E F C G D A AS SDF ASFG ASDF ASDF HJ TET AS DFAS DF ASFGHAF AS FD ASDF GA SADF")
addPar(" ASDFOAS ASFFGONASDF  DA SDF SADF ASD GSADF GA SFH")
