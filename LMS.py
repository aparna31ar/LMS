#!/usr/bin/env python
# coding: utf-8

# In[615]:


from datetime import date, timedelta
from dateutil.parser import parse
import time
class LMS:
    users= {}
    current_user = {}
    book_details={}
    book_issue={}
    book_return={}
    
    
    def signup(self,name,DOB,Mobile_No,email_id,password, user_type):
        self.users[len(LMS.users) + 1] = {
            "name": name,
            "DOB": DOB,
            "mobile": Mobile_No,
            "email_id": email_id,
            "password": password,
            "type": user_type,
            "user_id": len(LMS.users) + 1
            }
        print('User Registered Successfully')
        print(self.users)
            
    def login(self,email_id,user_password):
        for i in self.users:
#             print(self.users[i]['email_id'])
            if email_id == self.users[i]['email_id'] and user_password == self.users[i]['password']:
                print("Borrower is Logged in")
                self.current_user = self.users[i] 
                return self.current_user
        print('Wrong credentials')
    
    def create_users(self,name,DOB,mobile,email_id,password,user_type):
        if(self.current_user['type'] == 'admin'):
            self.users[len(LMS.users) + 1] = {
                "name": name,
                "DOB": DOB,
                "mobile": Mobile_No,
                "email_id": email_id,
                "password": password,
                "type": user_type
                }
            print('User Registered Successfully')
            print(self.users)
            
    def books(self,title,author,pages,year,isbn,copies):
        self.book_details[len(LMS.book_details) + 1] = {
            "title": title,
            "author": author,
            "pages": pages,
            "year": year,
            "isbn": isbn,
            "copies": copies,
            "book_id": len(LMS.book_details) + 1
            }
        print('Book added Successfully')
        print(self.book_details)
        
    def book_issued(self,email_id,book_id,user_id):
        if len(self.book_issue) == 0:
            self.book_issue[len(self.book_issue) + 1] = {
                    "email_id": email_id,
                    "book_id": book_id,
                    "user_id": user_id,
                    "issue_date": self.days()
                    }
            print("The book is available")
            for i in self.book_issue:
                if self.book_issue[i]['book_id'] == book_id:
                    self.check_book_stock(book_id, user_id)
                    return self.book_issue
                else:
                    self.book_issue[len(self.book_issue) + 1] = {
                        "email_id": email_id,
                        "book_id": book_id,
                        "user_id": user_id
                        }
                    return self.book_issue
                    print("The book is available inside else")

        print(self.book_issue) 
        
    def days(self):
        today = date.today()
        d1 = today.strftime("%d/%m/%y")
        return d1
    
    def check_book_stock(self, book_id, user_id):
        for i in self.book_details:
            if self.book_details[i]['copies'] > 0:
                #print(self.book_issue[i]['copies'])
                self.book_details[i]['copies']=self.book_details[i]['copies']-1
                #print(self.book_issue[i]['copies'])
                print('Book id {} issued to user_id {}'.format(self.book_details[i]['book_id'],user_id))
                return self.book_details
        

    def book_return(self,email_id,book_id,user_id):
        self.book_id=book_id
#         return_date=input('Enter the return date:')
#         issue_date=input('Enter the issue date:')
        for i in self.book_issue.keys():
            if self.book_issue[i]['book_id'] == book_id:
                print(self.book_issue[i]['book_id'])
                max_days=14
                today = date.today()
                return_date = today.strftime("%d/%m/%y")
#                 print('return date', return_date)
                
                td = parse(return_date) - parse(self.book_issue[i]['issue_date'])
                print(td.days)
                delta = td.days - 14
                if delta > 0:
                    print('You will be fined!!!')
                    print(delta*100)
                    
                self.book_issue[i].pop('book_id')
                self.update_book_data(book_id,user_id)
                return self.book_details
            else:
                print('this is wrong book')
                
    def update_book_data(self, book_id, user_id):
        for i in self.book_details.keys():
            if self.book_details[i]['book_id'] == book_id:
                self.book_details[i]['copies'] = self.book_details[i]['copies']+1
                print('Book id {} is returned by user_id {}'.format(book_id,user_id))
                print(self.book_details)

