"""
Bank transactions visualization project
Leon Nijenhuis
Edit: 2023-05-14

To add:
Read all cvs files in directory, not just one


pseudo code

process files in directory, compare with last version, append files in new version
plot transactions in time domain [ in category xyz attribute]
plot all transactions [ in category xyz attribute]
get statistics


process files in directory, compare with last version, append files in new version
    read single csv file in directory
    For cvs file:
        get timestamp of data in files
        each timestamp not in previous version, append to list
        each timestamp in previous version, delete
    with list of data in timestamp, return single file
    look for common descriptions, ibans, other stuff to determine what kind of transaction
    place transaction under predetermined category and delete unnecessary data props
    add process transactions to last data set, in chronological order

plot transactions in time domain [ in category xyz attribute] - zelfde functies gebruiken als in all transactions, welk oop principe?
    read existing data set of all transactions
    take data within piece of timestamp
    make figure
    plot data in figure

plot all transactions [ in category xyz attribute]
    read existing data set of all transactions
    make figure
    plot data in figure
"""

import data_processing
import data_visualize

# process_data = data_processing.Handler()
# figures = data_visualize.Handler()
#
# process_data.process_directory()
# figures.plot_data()

