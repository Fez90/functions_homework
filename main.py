def display_message():
    print("We are learning about functions in this chapter")
display_message()
def favorite_book(title):
    print(f"One of my favorite books is {title.title()}")
favorite_book('Alice in Wonderland')

def make_shirt(size,text):
    print(f"\nYour size is {size}")
    print(f"\nThe following text was printed {text}")
make_shirt('s','Hello')
make_shirt(size = 's',text = 'Hello')

def make_shirts(size,text='I love Python'):
    print(f"\nYour size is {size}")
    print(f"\nMessage was selected {text}")
make_shirts('L')
make_shirts(size = 'M')

def describe_city(city,country = 'Iceland'):
    print(f"\n{city.title()} in the {country.title()}")
describe_city('reykjavik')
# 8-6 page 142
# def city_country(city,country):
#     city_country = f"\n\"{city} {country}\""
#     return city_country.title()
# formatted_name = city_country('santiago','chile')
# print(formatted_name)
# # 8-7 page 142
# def make_album(name_album,title_album,songs=None):
#     """Return a dictionary about album"""
#     album = {'name': name_album,'title':title_album }
#     if songs:
#         album['number_songs'] = songs
#     return album
# music = make_album('sjdfsdj','hsdhfjhsdhf', songs = 7)
# print(music)
# music = make_album('vhfghfh','fghf')
# print(music)
# 8 page 142
# def make_album(name_album,title_album,songs=None):
#     """Return a dictionary about album"""
#     album = {'name': name_album,'title':title_album }
#     if songs:
#         album['number_songs'] = songs
#     return album
# while True:
#     print("\"please enter q to quit\"")
#     name_al = input("Please, enter album name: ")
#     if name_al == 'q':
#         break
#     t_album = input("Please, enter title name: ")
#     if t_album == 'q':
#         break
# formatted_album = make_album(name_al,t_album)
# if 'q' not in name_al and t_album:
#     print(f"\nYour album is {formatted_album}")
def show_messages(show_messages):
    """Print simple text"""
    for message in show_messages:
        print(f"\nThe following text messages: {message.title()}")
greeting = ['hello','hi','how you doing']
show_messages(greeting)
def show_messages(example_messages,sent_messages):
    """Print given message,then sent it to the list sent messages"""
    while example_messages:
        current_message = example_messages.pop()
        print(f"\nShowing message: {current_message}")
        sent_messages.append(current_message)
example_messages = ['hello','hi','how you doing']
sent_messages = []
show_messages(example_messages[:],sent_messages)
print(f"Original list : {example_messages}")
# 8-12,page 150
def sandwich(size,*toppings):
    """Summarize sandwich we about to make"""
    print(f"Making {size} size sandwich with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")
sandwich(6,'steak','cheease','tomato')
sandwich(12,'chicken', 'mozarella','pickles')
def build_profile(first,last,**user_info):
    """Building dictionary containing everything we know about user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('rachel','balke',location = 'New York',work = 'data analyst')
print(user_profile)