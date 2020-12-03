import pyttsx3
import PyPDF2

pdfBook = open('book.pdf', 'rb')
bookReader = PyPDF2.PdfFileReader(pdfBook)
pageNumber = bookReader.numPages
print('your book has ' + str(pageNumber) + ' pages')

page = bookReader.getPage(0)
textOfPage = page.extractText()
print(textOfPage)

speaker = pyttsx3.init()
speaker.say(textOfPage)
speaker.runAndWait()