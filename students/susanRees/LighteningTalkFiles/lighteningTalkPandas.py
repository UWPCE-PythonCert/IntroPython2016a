# Imports pandas
# reads the spreadsheet
# pops the "Age" column out
# uses .value_counts to group ages together and
# sorts them in ascending order according to frequency of occurance

import pandas as pd
df = pd.read_excel("surveyData.xlsx")
ages = df.pop("Age")
print(ages.value_counts(normalize=True, sort=True, ascending=False, bins=None, dropna=True))


# pandas.series.value_counts
# series.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True)

#   Returns object containing counts of unique values.

#   The resulting object will be in descending order so that the first
#   element is the most frequently-occurring element. Excludes NA values
#   by default.

#       Parameters:

#       normalize : boolean, default False
#           If True then the object returned will contain the relative
#           frequencies of the unique values.

#       sort : boolean, default True
#           Sort by values

#       ascending : boolean, default False
#           Sort in ascending order

#       bins : integer, optional
#           Rather than count values, group them into half-open bins, a
#           convenience for pd.cut, only works with numeric data

#       dropna : boolean, default True
#           Don’t include counts of NaN.

#       Returns:
#           counts : Series
