# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from fpdf import FPDF


def scrap_exam(forum_linkf: str, sizef: int, exam_namef: str, file_namef: str, export_txt: bool = True,
               export_pdf: bool = True) -> list:
    """Create a text and pdf of all found links, then return a list of them

    :param export_txt: Wants to export to pdf
    :param export_pdf: wants to export to txt
    :param forum_linkf: link to the discussion
    :param sizef: number of pages
    :param exam_namef: key string to search in link
    :param file_namef: name of the text file and pdf
    :return: a str list of all found links
    """
    driver = webdriver.Chrome()

    wanted_link = []

    for i in range(1, sizef + 1):
        driver.get(forum_linkf + str(i))
        list_possible_links_html = driver.find_elements(By.CLASS_NAME, "discussion-link")
        for possible_link_html in list_possible_links_html:
            link = possible_link_html.get_attribute("href")
            if exam_namef in link:
                wanted_link.append(link)

    wanted_link.sort()

    if export_pdf:
        pdf: FPDF = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)
        for link in wanted_link:
            pdf.cell(200, 10, txt=link, ln=2, align='C')
        pdf.output(f"{file_namef}.pdf")

    if export_txt:
        f = open(f"{file_namef}.txt", 'w')
        for link in wanted_link:
            f.write(f"{link}\n\n")
        f.close()

    return wanted_link


if __name__ == "__main__":
    forum_link = input("Link to the discussion? ")
    size = int(input("Number of pages to scrap? "))
    exam_name = input("Exam name? Format example: exam-101-500: ")

    file_name = input("Choose a file name to export the links to: ")
    liste = scrap_exam(forum_link, size, exam_name, file_name)
    print(len(liste))
