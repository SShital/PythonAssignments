import logging, requests, sys, json
import csv
import xlwt
from xlwt import Workbook

with open('combine.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    list1 = list(reader)

Dict = {}
stocks_dict = {}
for row in list1:
    share_name = row[0]

    url = 'https://www.quandl.com/api/v3/datasets/BSE/{}.json?api_key=88zuHyM9xTtsbtCNRUcW'.format(share_name)

    logging.basicConfig(format="%(levelname)-10s: %(message)s",
                        filename="webApi.log", filemode='w',
                        level=logging.DEBUG)

    response = requests.get(url)
    if response.status_code != 200:
        logging.error("Error: response is {}".format(response))
        sys.exit(1)

    content = json.loads(response.content)
    stocks_dict[row[0]] = {'company_name': content.get('dataset').get('name')}
    stocks_dict[row[0]]['stock_values'] = []
    for values in content.get('dataset').get('data'):
        stock_dict1 = dict()
        stock_dict1['date'] = values[0]
        stock_dict1['close'] = values[4]
        stocks_dict[row[0]]['stock_values'].append(stock_dict1)

    stocks_dict[row[0]]['top_1'] = stocks_dict[row[0]]['stock_values'][0]
    stocks_dict[row[0]]['top_2'] = stocks_dict[row[0]]['stock_values'][1]
    stocks_dict[row[0]]['profit'] = True if stocks_dict[row[0]]['top_1'] >= stocks_dict[row[0]]['top_2'] else False
    del stocks_dict[row[0]]['stock_values']
    logging.info('Company info: {}'.format(content.get('dataset').get('name')))


csvFile.close()

wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1', cell_overwrite_ok=True)
row = 0
column = 0

sheet1.write(row, column, 'Share Name')
sheet1.write(row, column+1, 'Last Date')
sheet1.write(row, column+2, 'Last Day Closing Price')
sheet1.write(row, column+3, 'Two Days Back')
sheet1.write(row, column+4, 'Two Days Back Close Price')
sheet1.write(row, column+5, 'Profit/Loss')


for key, value in stocks_dict.iteritems():
    row += 1
    sheet1.write(row, column, value.get('company_name'))
    sheet1.write(row, column+1, value.get('top_1').get('date'))
    sheet1.write(row, column+2, value.get('top_1').get('close'))
    sheet1.write(row, column+3, value.get('top_2').get('date'))
    sheet1.write(row, column+4, value.get('top_2').get('close'))

    if not value.get('profit'):
        xlwt.add_palette_colour("custom_colour", 0x08)
        wb.set_colour_RGB(0x08, 255, 000, 000)
        message = 'Loss'
    else:
        xlwt.add_palette_colour("custom_colour", 0x21)
        wb.set_colour_RGB(0x21, 000, 255, 000)
        message = 'Profit'
    style = xlwt.easyxf('pattern: pattern solid, fore_colour custom_colour')
    sheet1.write(row, column+5, message, style)
    column = 0
    row += 1

wb.save('Trade.xls')
