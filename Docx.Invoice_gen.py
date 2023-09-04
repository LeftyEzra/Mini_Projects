from docxtpl import DocxTemplate
document = DocxTemplate("Lefty_Ezra_template.docx")
invoice_list =[[2, "pen", 0.5, 1]]

document.render({"name":"Lefty","telephone":"08125363010",
                 "phone":"09053509607",
                 "invoice_list":invoice_list,
                 "Company":"Tinnaze Foot"})
#document.add_picture("Tinanzze.PNG")

document.save("my_invoice.docx")