while True:

    print('How may I assist you today ?')
    print('1. Load an Account')
    print('2. Open a new account')
    print('3. Terminate Program')
    try:

        n = int(input('Please Enter Choice : '))
    except:
        continue


    if (n == 1):
        print('Please Enter the Account Name : ')
        name = input().lower()
        col_names=[]
        data=[]
        line_count = 0
        try:
            with open(name+'.txt','r') as f:
                for line in f:
                    if line_count == 0:
                        col_names = line.split('\t')
                    else:
                        data.append(line.split('\t'))
                    line_count += 1

                if 'Credit' in data[-1]:
                        print('Latest Credit Balance : ')
                        print(data[-1][-1])
                else:
                    print('Latest Debit Balance : ')
                    print(data[-1][-2])

            latest_credit_balance = data[-1][-1]
            latest_debit_balance = data[-1][-2]

            print('What operation would you like to perform today : ')
            print('1. Withdrawal')
            print('2. Deposit')

            ch = int(input('Enter the choice here : '))
            money = float(input('Enter Amount : '))
            import datetime
            arr=[]
            today = datetime.date.today()
            if ch == 1:
                print('Withdrawal of Amount $'+str(money)+' Successful !')
                balance = float(latest_debit_balance)-money
                print('Current Debit Balance : '+str(balance))
                arr = data[-1]
                arr[-2] = balance
                arr[-4] = 'Debit'
                arr[-3] = ''
                arr[2]=str(today)
                arr[3]=float(arr[3])-float(balance)
            else:
                print('Deposit of Amount $'+str(money)+' Successful !')
                balance = float(latest_credit_balance)+money
                print('Current Credit Balance : '+str(balance))
                arr = data[-1]
                arr[-1] = balance
                arr[-3] = 'Credit'
                arr[-4] = ''
                arr[2]=str(today)
                arr[3]=float(arr[3])+float(balance)



            with open(name+'.txt','a') as f:
                f.writelines('\t'.join([str(x) for x in arr]))

        except Exception as e:
            print(str(e))
            print('Name Not Found in Database. Please Enter Accurately')

    if (n==2):
        print('Please Enter the Account Name : ')
        name = input().lower()
        print('Account Opened Successfully !')
        print('Please use Menu to Deposit or Withdraw from Account')
        with open(name+'.txt','w+') as f:
            pass
        continue
    
    if (n==3):
        
        print('Welcome to Admin Section .. ')
        print('Please Enter Password: ')
        st = input()
        if st == '12345abcd':
            print('Thank You for Using our Services')
            
            break      
        else:
            
            print('Incorrect Password. Attempt Terminated !')
            
    print('#'*30)