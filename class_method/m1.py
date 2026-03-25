cust_data = [
    {
        'cust_name': 'cust1',
        'cust_id': 101,
        'balance':200,
        'opening_date': '25-03-2026',
        'acc_type':'saving'
    },
    {
        'cust_name': 'cust2',
        'cust_id': 105,
        'balance':600,
        'opening_date': '15-03-2026',
        'acc_type':'current'
    }
]


class Bank:
    cust_name = ''
    cust_id = 0
    balance = 0
    opening_date = ''
    acc_type = ''

    # def __init__(self,custName,custId,custBalance,openingDate,accType):

    def __init__(self,custData):
        self.cust_name = custData.get('cust_name')
        self.cust_id = custData.get('cust_id')
        self.balance = custData.get('balance')
        self.opening_date = custData.get('opening_date')
        self.acc_type = custData.get('acc_type')

        print('cust_detals')
        print(f'cust_name := {self.cust_name}')
        print(f'cust_id := {self.cust_id}')
        print(f'balance := {self.balance}')
        print(f'opening_date := {self.opening_date}')
        print(f'acc_type := {self.acc_type}')


for cust in cust_data:
    print('customer bank details')
    bank_cust = Bank(cust)
    print('-'*10)
    print('-'*10)