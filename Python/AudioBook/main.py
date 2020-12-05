import pyttsx3
import PyPDF2

pdfBook = open('book.pdf', 'rb')
bookReader = PyPDF2.PdfFileReader(pdfBook)
pageNumber = bookReader.numPages
print('your book has ' + str(pageNumber) + ' pages')
speaker = pyttsx3.init()

for num in range(pageNumber + 1):
    page = bookReader.getPage(num)
    textOfPage = page.extractText()
    speaker.say(textOfPage)
    speaker.runAndWait()