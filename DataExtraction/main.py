# This is a sample Python script.
import tabula


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def convert_pdf_to_csv(document_path):
    df = tabula.read_pdf(document_path, pages="all")
    print(len(df))
    df[0]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path = '/home/xanon/Desktop/Projects/Data/ASUNAFO NORTH/H020102_D_A PRM SCH. KWAKU DUAKROM_NRL.pdf'
    convert_pdf_to_csv(path)

