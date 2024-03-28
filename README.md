# mmp
My money management program

The goal:
 1. To track current balance
 2. Implement the way to deal with several currencies

Balance tracking needs a way to deal with data, how should I store the data and how to interact with data?
 - Maybe try using `tinydb`?

We now have `tinydb` database implementation, but the format is not so convenient for viewing and dealing with. Let's try adding interaction with `polars`.
