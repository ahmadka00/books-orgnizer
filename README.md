# Books Organizer
#### Video Demo:  <https://youtu.be/JiFMTKAwxj0>
## Description:
*This program wrote in python to Organize the book in house library*
The program use sqlite3 library as a database call books.db and use terminal as the interface with user
when the program start it shouw up a welcom menu with 5 choices 1- add 2-delete 3-search 4- export to excel file Q- exite
the the program ask the user to input number from menue to of what the user want to do.
if the user input any wrong input that not (1-2-3-4-Q-q) the program show errer message and repromote again for choose 
correct number

*the user can exit in any level from the program using (ctrl+c) with goodbye message*
*The program in all level is case insensitive for text input which change the text to tilte case (title())*
*Also the program remove the white space from beganing and the end pf the text input*


## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
This project requires the following packages:

* SQLite3
* termcolor
* tabulate
* pandas
* openpyxl (for exporting to Excel) *no need to import it inside the code just install it*

## Installing
To install the required packages, you can use pip. Open your command prompt and run the following command:

pip install -r requirements.txt

### 1- Add books
If the user insert 1 after the main menu the user the program will ask the user of the number of the books s/he 
want to add (1 is min 5 is max) if the user insert any number of non number or level impty a messege of 
(Wrong input. Please enter an integer number.) will appear and prmote the question again. 
when the user enter a valid number of book s/he want to add (*example: user choose to add 2 books*) the program will ask the user to enter the details as below:
Books name: ,Release date:  ,Auther name: , Category: . 
for the Book name and Auther name the user should enter this details or if it keep empty a massage will appear and the question will promote again to enter the requested details. 
If the user enter first book details the program will ask for the second deatil book with the same questions book,date,auther,category, then after enting the 2nd book details a message of succsessfully added book will appear
After that the program will store the information inside (books.db) and prompte the main menu again. 

### 2- delete book
if the user enter number 2 from main menu a warning message will appear to warn that all information related to the book will deleted and there is no undo after delete action. 
Then the program will ask th user for name of the book s/he want to delete. 
If the user enter a name of the book match a name of the book inside the (books.db) a messare will appear that the book deleted succssesfully and will show the main menu again, but if the user enter a name that not match iside database a messge will appear that the book is not find and show the main menu again.

### 3-search book
if the user enter number 3 from main menu a new menu will appear :
Search by:
⓵  Book name
⓶  Auther name
⓷  Category

and the progeam will ask the user to enter the number from menu, if the user select 1 will the progam will ask the user to enter book name, if the book match a name inside the database the a table with one line book (id , book, writer, category)  will appear if not a mesage book not find will appear and promote the search menu again. 
if the user choose number 2- search by auther name the the program will ask the user about the authe name, if the auther name match the name inside datebase a table with (id, book, auther, category) of all book wrote by the match auther will appear, if the name not match a message auther not find will appear and promote the search menu again. 
if the user choose number 3- search by category the the program will ask the user about the category, if the category match the result inside datebase a table with (id, book, auther, category) of all book match the category will appear, if the category not match a message category not find will appear and promote the search menu again.
*in all three choices the program after matching the seaarch result will ask the user if s/he want to export the search reslt to excel file with(yes/no) choice if the user enter yes or y (or upper case of them) the program will export the table to excel file saved in the same directory of the program and appear a massage of export succssesfully with name of the file, but if the user choose to enter no, n (or upper case of them) the program will promote the main menu again*

## 4-export books
if the user enter number 4 from the main menu the program will show a message tell the uer that option will export all the library(datatbase) to excel fuke and it may take some time depending of the library size.
then the program will ask the user to confirm the choice (yes/no). if the user enter(yes/y/ or upperof them)the program will export all the data base to an excile file saved in the same directory of the program and a message will appear than the export done with name of the file. 
if the user choose (no/n/or uppercase of them) the program will promote the main menu again.

### Q-Exite 
if the user enter Q or q from the main menu a message will appear say(thankyou, Goodbye) and the program will exite, however if the user press ctrl+c at any level of the program the prgram will exit too and the same message will appear

## SQL books.sql
this file contain the .schema of the data base you should (if there is no books.db in the folder of the project) you should active the books.sql using the code. 
cat books.sql | sqlite3 books.db 
so the project will work correctly based on the designed database and tables. 

## test_projct.py
this is not work correcly as i couldn't write a good test to test the adding ,deleteing ,searching and exporting to excel function. 

# thank you
thank you for contact me for any further question. 
ahmad.kaddo00@gmail.com
