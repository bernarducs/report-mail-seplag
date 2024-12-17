from datetime import datetime

from dotenv import dotenv_values

ENV = dotenv_values('.env')

TODAY_DATE = datetime.now().strftime('%d/%m/%Y')

HEADER_IMG = './src/images/header.png'
FOOTER_IMG = './src/images/footer.png'
