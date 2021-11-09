info = '''
    You can work on your SQL and read about:

    S&OP.
    Demand Forecasting/Planning.
    Oracle Demand Management Cloud.
    Demand Sensing.
    Trade Promotions.
'''

# with open('sql/day2/xp_gold/gold.txt', 'w') as file:
#     for line in file:
#         file.write(line+'\n')
lines = ['Exercise 1: DVD Rental\n', 'Instructions\n', 'You were hired to babysit your cousin and you want to find a few movies that he can watch with you.\n', 'Find out how many films there are for each rating.\n', '\n', 'Get a list of all the movies that have a rating of G or PG-13.\n', 'Filter this list further: look for only movies that are under 2 hours long, and whose rental price (rental_rate) is under 3.00. Sort the list alphabetically.\n', '\n', 'Find a customer in the customer table, and change his/her details to your details, using SQL UPDATE.\n', 'Now find the customerג€™s address, and use UPDATE to change the address to your address (or make one up).\n', '\n', '*****************\n', '1.\n', '1.1 select count(distinct rating) from film;\n', "1.2select title from film where rental_rate < 3 and length < 120 and rating in ('G', 'PG-13') order by title;\n", "1.3 update customer set first_name = 'Ido', last_name = 'Sarue' where customer_id = 1;\n", "1.4 update address set address = 'dizengof 12', city_id = (select city_id from city where city ilike 'tel%'), phone = 0525791695 where address_id = 5;\n", '\n', 'Exercise 2: Students Table\n', 'Update\n', '1. ג€˜Lea Benichouג€™ and ג€˜Marc Benichouג€™ are twins, they should have the same birth_dates.  Update both their birth_dates to 02/11/1998.\n', '\n', "update students set birth_date = '1998/11/02' where last_name = 'Benichou';\n", '\n', '2. Change the last_name of David from ג€˜Grezג€™ to ג€˜Guezג€™.\n', " insert into students (last_name, first_name, birth_date) values('Guez', 'David','1998/11/02' );\n", '\n', '**Delete**\n', 'Delete the student named ג€˜Lea Benichouג€™ from the table.\n', '\n', " delete from students where first_name = 'lea' and last_name ilike '%benichou%' returning *;\n", '\n', '**Count**\n', 'Count how many students are in the table.\n', 'select count(*) from students;\n', '\n', 'Count how many students were born after 1/01/2000.\n', "select count(*) from students where birth_date > '2000/01/1';\n", '\n', '**Insert / Alter**\n', 'Add a column to the student table called math_grade.\n', 'Add 80 to the student which id is 1.\n', 'Add 90 to the students which have ids of 2 or 4.\n', 'Add 40 to the student which id is 6.\n', 'Count how many students have a grade bigger than 83\n', 'Add another student named ג€˜Omer Simpsonג€™ with the same birth_date as the one already in the table. Give him a grade of 70.\n', 'Now, in the table, ג€˜Omer Simpsonג€™ should appear twice. Itג€™s the same student, although he received 2 different grades because he retook the math exam.\n', 'Bonus: Count how many grades each student has.\n', 'Tip: You should display the first_name, last_name and the number of grades of each student. If you followed the instructions above correctly, all the students should have 1 math grade, except Omer Simpson which has 2.\n', 'Tip : Use an alias called total_grade to fetch the grades.\n', 'Hint : Use GROUP BY.\n', 'SUM\n', 'Find the sum of all the students grades.\n']

with open('sql/day2/xp_gold/gold.txt', 'w') as file:
    for line in lines:
        file.write(line+'\n')

with open('sql/day2/xp_gold/gold.txt', 'r') as file:
    print(file.readlines())
# def add_underscore(name):
#     print(name.replace(' ', '_'))

# add_underscore(input('file name: '))
