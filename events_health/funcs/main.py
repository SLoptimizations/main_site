import requests
import xmltodict
from openpyxl import load_workbook
from collections import OrderedDict
from bs4 import BeautifulSoup as bs4


def load_phones_from_xl(file):
    try:
        wb = load_workbook(filename=file)
        book = wb['SLop']

        len_Phone = len(book['A'])
        len_name = len(book['B'])
        print(len_name)

        failed = []

        for i in range(2, len_Phone+1):
            name = str(book['A' + str(i)].value)
            phone = str(book['B'+str(i)].value)
            if None in [phone, name]:
                failed.append(i)
                continue
            if len(phone) != 9 or phone[0] != '5':
                failed.append(i)
                continue

            print('phone', phone, 'name', name)
            #TODO !! - Implement SQL data insertion with phone and name value


        print('failed indexes', failed)
    except:
        import traceback
        traceback.print_exc()
        print('Cant get sim details from Sims Excel')
        return -1

# Usage Example
#load_phones_from_xl('xmls/Book1.xlsx')


class SMS:
    def __init__(self, user=None, password=None):
        '''
        Required -
        sms
            user
                username
                password

            source
            destinations
            #id in phone used to check if the sms arrived
                phone
                ...
                phone

            message


        not Required -
            tag
            Add_dynamic
            timing (format 30/01/20
            add_unsubscribe 0/1
            response
        '''
        self.user = user if user else '019sms'
        self.password =password if password else 'A210420a'
        self.bs = ''
        self.xml_dict = ''

    # Load from file or xml_dict
    def load(self, file=None, xml_data=None):
        if file:
            with open(file, "r", encoding='utf-8') as file:
                content = file.readlines()
                content = "".join(content)
                self.bs = bs4(content, "xml")
        else:
            self.bs = bs4(xml_data, "xml")

        self.xml_dict = xmltodict.parse(self.bs.prettify('utf-8'))

    # Build xml "from scratch"
    def build(self, from_num, phones_dict, message_text, timing=None, unsubscribe=None, tag=None, response=None):
        main = OrderedDict()
        tuples_list = []

        def credentials():
            credentials = OrderedDict([('username', self.user), ('password', self.password)])
            tuples_list.append(('user', OrderedDict(credentials)))

        def source_build():
            ''' Sender number (spoofable) '''
            tuples_list.append(('source', from_num))

        def destinations():
            ''' All phones to send phone to
             input dict should look like {"0501234567": "id1"}
             '''
            temp_list = []
            for phone in phones_dict:
                temp_list.append(OrderedDict([('@id', phones_dict[phone]), ('#text', phone)]))
            temp_list = OrderedDict([('phone', temp_list)])
            tuples_list.append(('destinations', temp_list))

        def message():
            ''' message to sent '''
            if (len(message_text)>201):
                print('WARNING MSG ABOVE 201 CHARACTERS, ABORTING!')
                exit()
            tuples_list.append(('message', message_text))

        def not_required():
            ''' For google to classify sms tags should use #'''
            if tag: tuples_list.append(('tag', tag))

            ''' input look like "DD/MM/YY HH:MM" '''
            if timing: tuples_list.append(('timing', timing))

            ''' input look like "DD/MM/YY HH:MM" '''
            if timing: tuples_list.append(('timing', timing))

            ''' input 0/1" '''
            if unsubscribe: tuples_list.append(('add_unsubscribe', unsubscribe))
            if response: tuples_list.append(('response', response))

        credentials()
        source_build()
        destinations()
        message()
        not_required()

        main['sms'] = OrderedDict(tuples_list)
        self.xml_dict = main

    # Send sms, use demo=False for production
    def send(self, demo=True):
        production_api = 'https://019sms.co.il/api'
        demo_api = 'https://019sms.co.il:8090/api/test'
        send_to = demo_api if demo else production_api
        test_response = bs4(requests.post(demo_api, data=self.pretty()).text, "xml")
        response = xmltodict.parse(test_response.prettify('utf-8'))
        print(response['sms']['message'])
        if not demo and response['sms']['message'] == 'SMS will be sent':
            prod_response = bs4(requests.post(send_to, data=self.pretty()).text, "xml")
            response = xmltodict.parse(prod_response.prettify('utf-8'))
            print(response['sms']['message'])

    # Add single phone instance to xml_dict
    def add_phone_to_list(self, phone_num, id):
        doc = OrderedDict()
        doc['@id'] = id
        doc['#text'] = phone_num
        self.xml_dict['sms']['destinations']['phone'].append(doc)

    def pretty(self):
        return xmltodict.unparse(self.xml_dict, pretty=True)

    def print(self):
        print(self.pretty())

    def change_message(self, message):
        self.xml_dict['sms']['message'] = message

    def add_timing(self, time):
        '''
        :param time: MM/DD/YY HH:MM string
        '''
        self.xml_dict['sms']['timing'] = time

    def save(self, to_file_path):
        with open(to_file_path, "w", encoding='utf-8') as file:
            file.write(self.pretty())

# Usage Example
x = SMS()
phone_dict = {"0543097191": "uuid1", "0526600550":"nuid2"} # for example

# Building XML file can be generated either from scratch or XML file.
# From scratch build
x.build(from_num='Liad', message_text='test', phones_dict=phone_dict)
# or From file -
# x.load(file='xmls/new.xml')

# Add single instance phone to the preloaded/built xml
x.add_phone_to_list('0541234567', 'uuidx')

# Change message on to the preloaded/built xml
x.change_message('message to be sent, up to 210 characters')

# Schedule time for the sms - format MM/DD/YY HH:MM string
x.add_timing('30/05/20 10:10')

# Send SMS with XML, use param demo=False for production
x.send()

# Save updated xml from object to XML file
# x.save('xmls/file_path.xml')

#  TODO  - Implement SQL data extraction to phone dict in format {phone:uuid} ex. {"0501234567": "2ub7"}
#          than you can inject phone dict into "build" function