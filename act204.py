# librey name finance 0.2502
#  pip install finance-calculator
from date_guesser import guess_date, Accuracy

# Uses url slugs when available
guess = guess_date(url='https://www.cbc.ca/radio/thecurrent/the-current-for-april-21-2021-1.5996015/chauvin-verdict-seen-as-victory-for-black-community-but-academic-calls-it-an-anomaly-1.5996449',
                   html='https://www.cbc.ca/radio/thecurrent/the-current-for-april-21-2021-1.5996015/chauvin-verdict-seen-as-victory-for-black-community-but-academic-calls-it-an-anomaly-1.5996449')

#  Returns a Guess object with three properties
guess.date      # datetime.datetime(2017, 10, 13, 0, 0, tzinfo=<UTC>)
guess.accuracy  # Accuracy.DATE
guess.method    # 'Found /2017/10/13/ in url'