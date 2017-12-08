import finsymbols
import json
import datetime

class SP500Service():
    company_objects = []

    def fetch_company_info(self):
        self.company_objects = finsymbols.get_sp500_symbols()

    def save_company_history(self):
        date = datetime.datetime.today().strftime('%m-%d-%Y')
        filename = 'archives/SP500_list_' + date + '.json'
        with open(filename, 'w') as outfile:
            json.dump(self.company_objects, outfile)


service = SP500Service()
service.fetch_company_info()
service.save_company_history()
COMPANY_NAMES = [company['company'] for company in service.company_objects]
