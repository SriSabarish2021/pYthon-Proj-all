#---Transaction Application---#
from datetime import datetime
import pandas
# import matplotlib.pyplot as ploter
App_name="Transaction Application"
print('')
print(App_name.center(60,'-'))
print("")
def Transaction_Process():
        print("Select Your Requirement:")
        print('-->')
        print("Add Transaction--- 1")
        print("View Transaction History on DATE Range-- 2")
        print("Exist --- 3")
        print('')
        entry=int(input("Enter Your Requirement: "))
        if entry==1:
            
            print("")
            print("Your Requirement is to ADD Transaction -Please Enter Following Details:")
            def transaction_details():

                def GET_amount():
                    try:
                        amt_to_add_inp=int(input("Enter Amount: "))
                        return amt_to_add_inp
                    except:
                        print("***Enter Valid Amount***")
                        return GET_amount()   
                get_amt_to_add=GET_amount()
                
                def GET_date():
                    get_date_inp=input("Enter Date of Transaction (DD-MM-YYYY): ")
                    try:
                        datetime.strptime(get_date_inp,"%d-%m-%Y")
                        return get_date_inp
                    except:
                        print("***Enter Valid Date***")
                        return GET_date()
                get_date=GET_date()

                get_description=input("Enter Transation Decription: ")

                def GET_TRANS_type():
                    transaction_type_inp=input("Enter Transaction Type(Income/Expense): ").strip().lower()
                    if transaction_type_inp not in ["income","expense"]:
                        print("***Enter Valid Type***")
                        return GET_TRANS_type()
                    return transaction_type_inp
                get_transaction_type=GET_TRANS_type()

                print("")

                transaction_array=[get_date,get_description,get_amt_to_add,get_transaction_type]
                details_array=["Date","Description","Amount","Type"]
                print("Check Your Transaction Details:")
                for index,transaction in enumerate(transaction_array):
                        print(f"{details_array[index]}= {transaction}")
                print("")
                get_changes_response=input("If Changes needed Type-(Y) , to Continue Type-(N): ").lower().strip()
                if get_changes_response=='y':
                    print("Your Can Now Change Details:")
                    return transaction_details()
                df = pandas.DataFrame([transaction_array])
                df.to_csv("./transaction.csv", mode="a", header=False, index=False)
                print("-----Your Transaction has been Recorded-----")
                continue_inp=input("Want to Continue(y/n) :").lower().strip()
                if continue_inp=='y':
                    return Transaction_Process()

            transaction_details()
        elif entry==2:
            print("")
            print("Your Requirement is to View Transaction History:")
            file=pandas.read_csv('./transaction.csv')
            print(file)
            print("")
            get_amt=list(file["AMOUNT"])
            Total_Amount=0
            for amount in get_amt:
                Total_Amount+=int(amount)
            print(f"Total Amount = {Total_Amount}")
            month_arr=[]
            expenses_arr=[]
            amount_arr_tot=0
            Income_Amount=0
            Expenses_Amount=0
            for index,type_trans in enumerate(file["TYPE"]):
                if str(type_trans)=="income":
                    
                    Income_Amount+=int(file["AMOUNT"][index])
                else:
                    Expenses_Amount+=int(file["AMOUNT"][index])

                    if len(month_arr):
                        for index,month in enumerate(month_arr):
                            if int(month)!=int(str(file["DATE"][index]).split('-')[1]) and str(type_trans)=="expenses" and len(month_arr)==0:
                                month_arr.append(month)
                                
                    else:
                        month_arr.append(int(str(file["DATE"][index]).split('-')[1]))                          
                   
            for indises,type_date in enumerate(file["DATE"]):
                if int(str(file["DATE"][indises]).split('-')[1])==int(str(type_date).split('-')[1]) and str(file["TYPE"][indises])=="expense":
                    amount_arr_tot+=int(file["AMOUNT"][indises])
                elif int(str(file["DATE"][indises]).split('-')[1])!=int(str(type_date).split('-')[1]) and str(file["TYPE"][indises])=="expense":
                    expenses_arr.append(int(file["AMOUNT"][indises]))
            expenses_arr.append(amount_arr_tot)
            print(month_arr)
            print(expenses_arr)
            print(f"Total Income = {Income_Amount}") 
            print(f"Total Expenses = {Expenses_Amount}")   
            print(f"-----Total Savings = {Income_Amount-Expenses_Amount}")
            print("")
            get_graph_inp=input(f"Want to See the Graph of the year {datetime.now().date().year}-(y/n): ").lower().strip()
            if get_graph_inp=='y':
                print(len(expenses_arr),len(month_arr))
                print(expenses_arr)
                print(month_arr)
                # ploter.plot(expenses_arr,month_arr)
                # ploter.title(f"{datetime.now().date().year} Analysis")
                # ploter.xlabel("Month")
                # ploter.ylabel("Expenses")
                # ploter.show()    
        elif entry==3:
            exist_inp=input("Do you Want to Exist(y/n): ").lower()
            if exist_inp=='n':
                return Transaction_Process()
            else:
                print("Thank You For Performing")
        else:
            print("-----Please Enter Valid Input-----")


Transaction_Process()


