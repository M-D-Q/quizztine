# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from fpdf import FPDF


def scrap_exam(forum_linkf: str, sizef: int, exam_namef: str, file_namef: str) -> list:
    """Create a text and pdf of all found links, then return a list of them

    :param forum_linkf: link to the discussion
    :param sizef: number of pages
    :param exam_namef: key string to search in link
    :param file_namef: name of the text file and pdf
    :return: a str list of all found links
    """
    driver = webdriver.Chrome()

    f = open(f"{file_namef}.txt", 'w')

    pdf: FPDF = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)

    wanted_link = []

    for i in range(1, sizef + 1):
        driver.get(forum_linkf + str(i))
        list_possible_links_html = driver.find_elements(By.CLASS_NAME, "discussion-link")
        for possible_link_html in list_possible_links_html:
            link = possible_link_html.get_attribute("href")
            if exam_namef in link:
                wanted_link.append(link)
                f.write(f"{link}\n\n")
                pdf.cell(200, 10, txt=link,
                         ln=2, align='C')

    # save the pdf with name .pdf
    pdf.output(f"{file_namef}.pdf")

    return wanted_link


if __name__ == "__main__":
    forum_link = input("Link to the discussion? ")
    size = int(input("Number of pages to scrap? "))
    exam_name = input("Exam name? Format example: exam-101-500: ")

    file_name = input("Choose a file name to export the links to: ")
    liste = scrap_exam(forum_link, size, exam_name, file_name)
    print(len(liste))
