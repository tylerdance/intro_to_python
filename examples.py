# comment

"""welcome to python"""

name = 'Tyler'
age = 5
is_old = False

# print(name)

# Methods for a string
sentence = 'it is nicoles birthday'

nicole_birthday = sentence.split(' ')
# print(nicole_birthday)

new_sentence = " ".join(nicole_birthday)
# print(new_sentence)

# find index
# print(new_sentence.index('n'))

# upper and lower case
name.upper()
name.lower()

# replace
day_sentence = sentence.replace('birthday', 'day')
# print(day_sentence)

# in
is_day = 'day' in day_sentence
# print(is_day)

"""
    str[index] choose one letter at index
    str[-index] choose letter at index counting backwards from the end.
    str[start:end] get a range of letters from a start to end.
    str[start:end:step] get a range of letters taking step sized steps between.
    str[:end] omit the start index and grab letters from zero up to end.
    str[start:] omit the end index and grab letters from start up to the end of the string.
    str[::-1] reverses a string by going backwards with a step of -1 from start to end.
"""

# ranges
last_letter = day_sentence[-1]
nicole_range = day_sentence[6:12]
# print(nicole_range)

# length
# print(len(nicole_range))

equal_to = 5 == 5
not_equal = 5 != 5

not True
not False

# true_story = 5 <= 5
# this_should_be+true = 6 >= 5

# print('Rome' == 'rome' or 'Pete' == 'Pete')
# print('Rome' == 'Rome' or 'Pete' == 'Pete')

# print('' or 'Rome')

# lists (arrays)
numbers = [3,4,5,6]
# print(len(numbers))

numbers[1]

# print(numbers[-1])

numbers[len (numbers) - 1]

five_rome = ['Rome'] * 5
# print(five_rome)

one_thru_five = list(range(5))
# print(one_thru_five)

# iterate
for i in range(len(one_thru_five)):
    num = one_thru_five[i]
    # print(num)

# create a list, iterate over, and print value
my_list = list(['hi', 'i', 'am', 'tyler'])
for i in range(len(my_list)):
    hi = my_list[i]
    # print(hi)

random_numbers = [45, 88, 4, 17]
random_numbers.sort()

random_numbers.append(33)
# print('yuh', random_numbers)

reverse_random_numbers = random_numbers[::-1]
# print(reverse_random_numbers)

thirty_three = random_numbers.pop()
# print(thirty_three)

# insert (puts 99 at first index)
random_numbers.insert(0, 99)
# print(random_numbers)

# help
# print(help(my_list))

"""dictionary"""
car = {
    "color": 'Red',
    "make": 'Tesla',
    "model": "S",
    "all_colors": ['red', 'white', 'black'],
    "cool": True,
    "other_products": {
        "one": 'model 3',
        "two": 'cybertruck',
        "three": 'model s'
    }
}
# print(car["make"])
car["speed"] = 200
# print(car)
# print(car.get('color'))
# print(car.items())
# print(car.keys())

"""type conversion"""
int('33')
str(33)
float(33)
bool(0)
bool(3)


"""string interpolation"""
# print('hello my name is ' + name)
# print(f"hello my name is {name}")

phrase = 'this is a phrase {}'
phrase.format(name)
# print(phrase)

"""functions"""
def name(someone):
    return someone

# print(name('Tyler'))

def old_enough(age):
    if age < 21:
        return 'no beans'
    elif age == 21:
        return 'big beans'
    else:
        return 'spicy'
# print(old_enough(20))


def add(num1, num2):
    return num1 + num2
print(add(1, 2))

def subtract(num1, num2):
    return

def random_function(beans):
    if beans == 'spiced':
        return 'spicy'
    elif beans == 'salted':
        return 'no spice'
print(random_function('salted'))

