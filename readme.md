# Sales Search XML

For this project you're given a data file `sales-data.xml` that contains 1,000 random sales from between 8/1/2019 and 8/30/2020. Your task is to parse data out of this file.

### Helper Method

Because you're going to be working with floating point values you've got a helper method `round_dictionary` to help you out. You'll want to run any dictionaries your methods create through `round_dictionary` before returning to round all values to no more than 2 decimal places.

For example...

```python
return self.round_dictionary({"A": 123.456, "B", 1.70001});
# {"A": 123.46, "B": 1.7}
```

This will help take care of the rounding weirdness that comes with floating point numbers.



### Amount Spent

The first method, `amount_spent`, should go through the data file and find the amount spent in a specified category. For example, `amount_spent('Baby')` would return the amount spent in the `Baby` category.

### Spent by Gender

`spent_by_gender` returns a dictionary with the amount spent for each gender. Keys should be `"M"` and `"F"`.  Key order does not matter. 

Be sure to run your dictionary through `round_dictionary` before returning. 

### All Categories

`all_categories` returns a dictionary of the amount spent in each category, with the category name as key and amount as value. 

Category names are case sensitive, although it doesn't matter because they don't vary in the data. You won't see both `computers` and `Computers`. Category names are all title cased.

The order of keys does not matter. The auto grader will consider `{"A": 12, "B": 16}` and `{"B": 16, "A": 12}` equal. 



### Spent Between

The `spent_between` method takes a `start_date` and `end_date` and returns the amount of sales between those two dates, inclusive.

`start_date` and `end_date` are both timestamps, not strings. You'll need to convert the `timestamp` field from the XML from a string to a timestamp to be able to compare. To do that use the `dateutil.parser.parse(date_string)` method. It will convert the string representation `date_string` to a timestamp. Once that's done you can compare the dates just like numbers with `<`, `>`, `<=` and `>=`.

