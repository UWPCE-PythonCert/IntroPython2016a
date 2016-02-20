import hash_keyfile

# create a mapping of state to abbreviation
states = hash_keyfile.new()
hash_keyfile.set(states, 'Oregon', 'OR')
hash_keyfile.set(states, 'Florida', 'FL')
hash_keyfile.set(states, 'California', 'CA')
hash_keyfile.set(states, 'New York', 'NY')
hash_keyfile.set(states, 'Michigan', 'MI')

# create a basic set of states and some cities in them
cities = hash_keyfile.new()
hash_keyfile.set(cities, 'CA', 'San Francisco')
hash_keyfile.set(cities, 'MI', 'Detroit')
hash_keyfile.set(cities, 'FL', 'Jacksonville')

# add some more cities
hash_keyfile.set(cities, 'NY', 'New York')
hash_keyfile.set(cities, 'OR', 'Portland')


# print out some cities
print ('-' * 10)
print ("NY State has: %s" % hash_keyfile.get(cities, 'NY'))
print ("OR State has: %s" % hash_keyfile.get(cities, 'OR'))

# print some states
print ('-' * 10)
print ("Michigan's abbreviation is: %s" % hash_keyfile.get(states, 'Michigan'))
print ("Florida's abbreviation is: %s" % hash_keyfile.get(states, 'Florida'))

# do it by using the state then cities dict
print ('-' * 10)
print ("Michigan has: %s" % hash_keyfile.get(cities, hash_keyfile.get(states, 'Michigan')))
print ("Florida has: %s" % hash_keyfile.get(cities, hash_keyfile.get(states, 'Florida')))

# print every state abbreviation
print ('-' * 10)
hash_keyfile.list(states)

# print every city in state
print ('-' * 10)
hash_keyfile.list(cities)

print ('-' * 10)
state = hash_keyfile.get(states, 'Texas')

if not state:
  print ("Sorry, no Texas.")

# default values using ||= with the nil result
# can you do this on one line?
city = hash_keyfile.get(cities, 'TX', 'Does Not Exist')
print ("The city for the state 'TX' is: %s" % city)

print("states are *****:")
hash_keyfile.list(states)

print("cities are ******")

hash_keyfile.list(cities)