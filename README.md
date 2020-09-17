# filter_to_csv python 3.8.2
simple script
to demonstrate skills in working in the OOP style,
using a decorator, generator and working with files

serves for filtering incorrect data from the .csv file
and writing to bad logs format .log

Use:
~/filter_to_csv$ python3 run_script.py 'example_data'

Result to terminal:

Invalid format: it is not name! in example_data/data32.csv line 6

Invalid format: it is not email! in example_data/data32.csv line 8

Result to file:

~/filter_to_csv/err_data_csv.log

too many values to unpack (expected 3) type <class 'ValueError'> 

it is not name! type <class 'ErrDecorator.NotNameError'> 

it is not email! type <class 'ErrDecorator.NotEmailError'> 
