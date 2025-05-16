from fpdf import FPDF


class Shirtificate(FPDF):
    def __init__(self, name):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.name = name
        self.add_page()
        self.set_auto_page_break(auto=False)
        self.create_shirtificate()

    def header(self):
        self.set_font("Helvetica", size=40)
        self.cell(w=0, h=60, txt="CS50 Shirtificate", align="C", ln=True)

    def create_shirtificate(self):
        self.image("shirtificate.png", x=15, y=70, w=180)

        self.set_font("Helvetica", size=24)
        self.set_text_color(255, 255, 255)
        self.set_xy(0, 130)
        self.cell(w=210, h=10, txt=f"{self.name} took CS50", align="C")


def main():
    name = input("Name: ")
    pdf = Shirtificate(name)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
