# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from fpdf import FPDF

driver = webdriver.Chrome()
forum_link = input("Link to the discussion? ")
size = int(input("Number of pages to scrap? "))
exam_name = input("Exam name? Format example: exam-101-500: ")
wanted_link = []

file_name = input("Choose a file name to export the links to: ")

f = open(file_name, 'w')

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=15)

for i in range(1, size + 1):
    driver.get(forum_link + str(i))
    liste = driver.find_elements(By.CLASS_NAME, "discussion-link")
    for l in liste:
        link = l.get_attribute("href")
        if exam_name in link:
            f.write(f"{link}\n\n")
            pdf.cell(200, 10, txt=link,
                     ln=2, align='C')

# save the pdf with name .pdf
pdf.output(f"{file_name}.pdf")
