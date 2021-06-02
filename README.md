**PROJECT NAME** <br>
  PENGU Milktea: Ordering System Software
  
<br>**ABOUT THE PROJECT** <br>
  This project is a web application software which serves as an ordering system for the PENGU Milktea Business. It allows the customer of the business to place their orders without having physical contact with the owner/s through this web application. Also, the software allows the owner/s itself to manage the number of orders, the number of sales every day, week and month, and the inventory and availability of their products.  The project is written in python programming language for its back-end system, and it is written in JavaScript and CSS programming language for its front-end. It is also for the partial fulfillment of the course _Software Design Laboratory_.
  
<br>**REQUIREMENTS OR DEPENDENCIES USED**
  - Python IDE v3.9
  - IntelliJ IDEA Pycharm Professional
  - Django Software

<br>**ENVIRONMENT SET-UP FOR THE PROJECT TO RUN (Step-by-step Procedures or Commands for Windows Only)**
  1. Download and install Python IDE v3.9. Skip this step if it is already installed.
  2. Download and install IntelliJ IDEA Pycharm Professional. Skip this step if it is already installed.
  3. Download the zipped project repository, then extract it in your computer.
  4. Open the project through Pycharm.
  5. Click File -> Click Setting -> Click Project Tab -> Click Setting Icon -> Click Ok -> Click Apply
  6. Click configure -> Click Remove All Version Control Directories
  7. Add Configuration -> Put a name -> Click Apply -> Click Run

  <br>Another step that you can choose for easier configuration, here's another set of instructions:<br>
  1. Follow steps 1-3 again.
  2. Open Pycharm, then create a new project under Django. This will automatically configure the IDE
  3. Open the project through Pycharm
  4. Run the program.

<br>**ABOUT THE AUTHORS**<br>
  **Brief Background:** <br>
    The authors of this project are undergraduate students of De La Salle University taking BS - Computer Engineering. 
    
  **Contact Details:**<br>
  Mark Brendon D. Medrano <br>
  Email: brendon_medrano@dlsu.edu.ph <br>
  GitHub: mbdmedrano-28 <br><br>
  Gabriel Francis D. Perez <br>
  Email: gab_perez@dlsu.edu.ph <br>
  GitHub: gfdperez <br><br>
  Christian Paul S. Velasco <br>
  Email: christian_paul_velasco@dlsu.edu.ph <br>
  Github: PaulVelasco19 <br><br>

<br>**REVISION LOGS**
  - 04-05-21:
    - Login Page with html and css is presented as the initial output
  - 04-21-21:
    - Home Page is already displayed
    - Menu Page with complete list of items is displayed
    - Partial add to cart page is also displayed
    - Backend part is not yet implemented
  - 05-02-21:
    - Login and Signup Page for customer interface are working powered by PostgreSQL database.
    - Login Page for the Admin/Owner is now working however the landing page is not yet integrated
    - About Page is also displayed.
    - Home Page and Menu Page views are modified for better UX.
    - The whole project is changed to organize the folder directories and its applications.
  - 05-07-21:
    - The home page and menu page are revised with proper css wrapping 
    - The account settings is now working supported by the database
    - Admin login interface is also implemented with a proper working user authentication
    - The database is also changed to enhance the security of the user's data
    - A modified user account model is implemented
  - 05-10-21:
    - The edit menu feature in the admin interface is also working supported by the database system
    - The changes in the menu's table in the database also reflects to the menu in the customer interface making it more dynamic
    - A simple inventory page is also implemented in the admin interface with a maximum of 10 slots. The data here is also stored in the database
  - 05-23-21:
    - The user can now add an item in their cart, with a 5-item capacity.
    - Checking out process is also completed.
    - Check out process includes the following: choosing of size, quantity, and filling-up information.
    - Cart page is dynamic with order page
    - Cart page has a remove option to edit.
    - My order page has included an order status for order updates.
    - Queueing of order in the order's database is also implemented but not yet reflected in the admin interface for status update
  - 05-26-21:
    - The bug that occurred in the account settings page during the demonstration is now fixed.
    - 90% of the project is fully working here, views sales and order feature in admin interface is not yet implemented.
  - 06-01-21:
    - The order list feature for the admin interface is now working and it can now update the status of the orders of the customers
    - The view daily sales is now implemented supported by the database
    - The program is now 100% complete
    - All bugs are also checked and fixed.
