# Hint:  use Google to find python function

from datetime import datetime

####a)
date_start_a = '01-02-2013'
date_stop_a = '07-28-2015'

####b)
date_start_b = '12312013'
date_stop_b = '05282015'

####c)
date_start_c = '15-Jan-1994'
date_stop_c = '14-Jul-2015'

# Date formats
date_format_a = "%m-%d-%Y"
date_format_b = "%m%d%Y"
date_format_c = "%d-%b-%Y"

# Function to find number of days
def num_days( start, stop, date_format, question ):
    new_start = datetime.strptime(start, date_format)
    new_stop = datetime.strptime(stop, date_format)
    days_diff = new_stop - new_start
    print "The number of days between the start and stop date for", question, "is", days_diff.days, "days."
    return

num_days(date_start_a, date_stop_a, date_format_a, "a")
num_days(date_start_b, date_stop_b, date_format_b, "b")
num_days(date_start_c, date_stop_c, date_format_c, "c")
