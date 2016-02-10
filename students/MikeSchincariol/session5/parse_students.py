#!/usr/bin/python3


#Open the students file
language_dict = {}

with open("students.txt", "r") as f:
    for line in f:

        # Split on full name (given by ':')
        name = line.split(":")[0]
        languages = line.split(":")[1]

        # Convert the languages into a list
        languages = languages.split(",")

        # Clean up white space from around language string items post strip
        for idx, lang_line in enumerate(languages[:]):
            languages[idx] = lang_line.strip()

        # Filter for empty language lists
        if len(languages[0]) == 0:
            continue

        # Loop over the languages specified and if they are not present
        # then add them to the dict with a count of 1. If they are present,
        # increment the count
        for language in languages:
            if language not in language_dict:
                language_dict[language] = 0
            language_dict[language] = language_dict[language] + 1


# Print the list of languages and how many times it was seen
for k, v in language_dict.items():
    print ("{0:>12}:{1:>5}".format(k, v))