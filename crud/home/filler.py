import requests
import json

url = 'http://localhost:5000/homes/'

headers = {'content-type': 'application/json'}
homes = [
    {
        'img': {
            'head': 'https://a0.muscache.com/im/pictures/229c96ef-3ac0-4328-ba9e-c9e0acde94e5.jpg',
            'tail': [
                'https://a0.muscache.com/im/pictures/aa0334b4-d3b6-45f2-a3ef-22b0d126dbc0.jpg',
                'https://a0.muscache.com/im/pictures/83c3b815-ace9-4b42-82c4-fb8f4a83cfdf.jpg',
            ],
        },
        'place': { # added dynamically
            'lat': 36.708693,
            'lng': 52.634107,
            'town': 'batumi',
        },
        'location': {
            'lat': 36.708532,
            'lng': 52.634357,
        },
        'title': "Chillout Hostel",
        'about': {
            'summary': 'Located in the coffee region, in the Andean mountains of Colombia, South America, a charming cabana made from bamboo, with a great view and a "sendero" or pathway through the bamboo forest which criss-crosses our 5 acre organic farm, leading down to a stream. A place to relax and commune with nature.',
            'specifications': {
                'The space': [
                    "Surrounded by beautiful rainforest plants, strategically placed for privacy, with an outdoor shower in a garden. Commune with nature, listen to crickets and night and birds in the morning.",
                    "Situated on a small organic farm. We grow tropical fruits and trees, flowers, with aloe vera as our main crop. There is an enchanting pathway through our bamboo forest, leading down to a mountain stream and a small waterfall. Near many coffee region tours and attractions, including our own organic farming workshops, visiting a nearby bee farm where our neighbor propagates bees in danger of extinction, local coffee tours, butterfly emporium, hang gliding, zip lining, white water rafting, horseback riding, hiking, visiting nearby historic towns and world heritage sites.",
                ],
                'Interaction with guests': [
                    "We offer breakfast daily, included in the room price, help to plan tours and make reservations, help to plan and facilitate transportation, other meals on site are offered, as well as airport or bus terminal pick-up. (20mil pesos) We will make sure you feel taken care of and have help with whatever needs you have.",
                ],
                'Other things to note': [
                    "Yudy is a good cook and in addition to a breakfast of your choice, she offers lunches or dinners for 20 mil pesos per person.",
                    "The King size bed can be separated into 2 twins.",
                ]
            }
        },
        'specifications': {
            'space': {  # hope
                'Accommodates': 2,
                'Bathrooms': 1,
                'Bedrooms': 'Studio',
                'Beds': 2,
                'Check In': 13,  # Anytime after 1PM
                'Check Out': 11,  # AM
                'Pet Owner': ['dog', 'cat'],  # Dog(s) and cat(s)
                'Property type': 'Cabin',
                'Room type': 'Entire home/apt',
            },
            'amenities': [  # hope
                'internet',
                'wireless internet',
                'family/kid friendly',
                'free parking on premises',
            ],
            'prices': {  # hope
                'price': 1,
                'extra people': 20,  # += / night after the first guest
                'cleaning Fee': 15,
                'Weekly Discount': 6,
            },
            'house rules': ['Check in is anytime after 1PM', ],  # hope
            'Cancellations': {
                'type': 'flexible',
                'description': 'Cancel up to 24 hours before your trip and get a full refund. Cancel within 24 hours of your trip and the first night is non-refundable.',
            },
            'Safety features': ['First aid kit', 'Safety card', 'Fire extinguisher'],  # hope
            'Availability': ['2 nights minimum stay View calendar', ],
        },  # hope
        'reviews': {
            'comments': {},
            'scores': {
                'size': 10,
                'score': 5,
            },
            'likes': {
                'me': True
            }
        },
        'hosts': [  # added dynamically
            {
                'language': 'english',
                'Response rate': 65,
                'Response time': 145,  # 145 min -> within a few hours
            }, {
                'language': ' Español',
                'response': {
                    'rate': 75,
                    'time': 125,
                }
            }
        ]
    },     {
        'img': {
            'head': 'https://a0.muscache.com/im/pictures/4ff370ab-7825-408b-a715-84b92df5367c.jpg',
            'tail': [
                'https://a0.muscache.com/im/pictures/f1f01d3a-79d7-40fc-82bb-4d01fb2a5a0b.jpg',
            ],
        },
        'place': {
            'lat': 36.708693,
            'lng': 52.634107,
            'town': 'batumi',
        },
        'location': {
            'lat': 36.708632,
            'lng': 52.634257,
        },
        'title': "trioxkomnatnaia kvartira vcentre",
        'about': {
            'summary': 'Located in the coffee region, in the Andean mountains of Colombia, South America, a charming cabana made from bamboo, with a great view and a "sendero" or pathway through the bamboo forest which criss-crosses our 5 acre organic farm, leading down to a stream. A place to relax and commune with nature.',
            'specifications': {
                'The space': [
                    "Surrounded by beautiful rainforest plants, strategically placed for privacy, with an outdoor shower in a garden. Commune with nature, listen to crickets and night and birds in the morning.",
                    "Situated on a small organic farm. We grow tropical fruits and trees, flowers, with aloe vera as our main crop. There is an enchanting pathway through our bamboo forest, leading down to a mountain stream and a small waterfall. Near many coffee region tours and attractions, including our own organic farming workshops, visiting a nearby bee farm where our neighbor propagates bees in danger of extinction, local coffee tours, butterfly emporium, hang gliding, zip lining, white water rafting, horseback riding, hiking, visiting nearby historic towns and world heritage sites.",
                ],
                'Interaction with guests': [
                    "We offer breakfast daily, included in the room price, help to plan tours and make reservations, help to plan and facilitate transportation, other meals on site are offered, as well as airport or bus terminal pick-up. (20mil pesos) We will make sure you feel taken care of and have help with whatever needs you have.",
                ],
                'Other things to note': [
                    "Yudy is a good cook and in addition to a breakfast of your choice, she offers lunches or dinners for 20 mil pesos per person.",
                    "The King size bed can be separated into 2 twins.",
                ]
            }
        },
        'specifications': {
            'space': {  # hope
                'Accommodates': 2,
                'Bathrooms': 1,
                'Bedrooms': 'Studio',
                'Beds': 2,
                'Check In': 13,  # Anytime after 1PM
                'Check Out': 11,  # AM
                'Pet Owner': ['dog', 'cat'],  # Dog(s) and cat(s)
                'Property type': 'Cabin',
                'Room type': 'Entire home/apt',
            },
            'amenities': [  # hope
                'internet',
                'wireless internet',
                'family/kid friendly',
                'free parking on premises',
            ],
            'prices': {  # hope
                'price': 100,
                'extra people': 20,  # += / night after the first guest
                'cleaning Fee': 15,
                'Weekly Discount': 6,
            },
            'house rules': ['Check in is anytime after 1PM', ],  # hope
            'Cancellations': {
                'type': 'flexible',
                'description': 'Cancel up to 24 hours before your trip and get a full refund. Cancel within 24 hours of your trip and the first night is non-refundable.',
            },
            'Safety features': ['First aid kit', 'Safety card', 'Fire extinguisher'],  # hope
            'Availability': ['2 nights minimum stay View calendar', ],
        },  # hope
        'reviews': {
            'comments': {
                'size': 2
            },
            'scores': {},
            'likes': {
                'me': False
            }
        },
        'hosts': [
            {
                'language': 'english',
                'Response rate': 65,
                'Response time': 145,  # 145 min -> within a few hours
            }, {
                'language': ' Español',
                'response': {
                    'rate': 75,
                    'time': 125,
                }
            }
        ]
    },     {
        'img': {
            'head': 'https://a0.muscache.com/im/pictures/aa0334b4-d3b6-45f2-a3ef-22b0d126dbc0.jpg',
            'tail': [
                'https://a0.muscache.com/im/pictures/229c96ef-3ac0-4328-ba9e-c9e0acde94e5.jpg',
                'https://a0.muscache.com/im/pictures/83c3b815-ace9-4b42-82c4-fb8f4a83cfdf.jpg',
            ],
        },
        'place': {
            'lat': 36.708693,
            'lng': 52.634107,
            'town': 'batumi'
        },
        'location': {
            'lat': 36.708732,
            'lng': 52.634357,
        },
        'title': "ushaka ashviki",
        'about': {
            'summary': 'Located in the coffee region, in the Andean mountains of Colombia, South America, a charming cabana made from bamboo, with a great view and a "sendero" or pathway through the bamboo forest which criss-crosses our 5 acre organic farm, leading down to a stream. A place to relax and commune with nature.',
            'specifications': {
                'The space': [
                    "Surrounded by beautiful rainforest plants, strategically placed for privacy, with an outdoor shower in a garden. Commune with nature, listen to crickets and night and birds in the morning.",
                    "Situated on a small organic farm. We grow tropical fruits and trees, flowers, with aloe vera as our main crop. There is an enchanting pathway through our bamboo forest, leading down to a mountain stream and a small waterfall. Near many coffee region tours and attractions, including our own organic farming workshops, visiting a nearby bee farm where our neighbor propagates bees in danger of extinction, local coffee tours, butterfly emporium, hang gliding, zip lining, white water rafting, horseback riding, hiking, visiting nearby historic towns and world heritage sites.",
                ],
                'Interaction with guests': [
                    "We offer breakfast daily, included in the room price, help to plan tours and make reservations, help to plan and facilitate transportation, other meals on site are offered, as well as airport or bus terminal pick-up. (20mil pesos) We will make sure you feel taken care of and have help with whatever needs you have.",
                ],
                'Other things to note': [
                    "Yudy is a good cook and in addition to a breakfast of your choice, she offers lunches or dinners for 20 mil pesos per person.",
                    "The King size bed can be separated into 2 twins.",
                ]
            }
        },
        'specifications': {
            'space': {  # hope
                'Accommodates': 2,
                'Bathrooms': 1,
                'Bedrooms': 'Studio',
                'Beds': 2,
                'Check In': 13,  # Anytime after 1PM
                'Check Out': 11,  # AM
                'Pet Owner': ['dog', 'cat'],  # Dog(s) and cat(s)
                'Property type': 'Cabin',
                'Room type': 'Entire home/apt',
            },
            'amenities': [  # hope
                'internet',
                'wireless internet',
                'family/kid friendly',
                'free parking on premises',
            ],
            'prices': {  # hope
                'price': 10000,
                'extra people': 20,  # += / night after the first guest
                'cleaning Fee': 15,
                'Weekly Discount': 6,
            },
            'house rules': ['Check in is anytime after 1PM', ],  # hope
            'Cancellations': {
                'type': 'flexible',
                'description': 'Cancel up to 24 hours before your trip and get a full refund. Cancel within 24 hours of your trip and the first night is non-refundable.',
            },
            'Safety features': ['First aid kit', 'Safety card', 'Fire extinguisher'],  # hope
            'Availability': ['2 nights minimum stay View calendar', ],
        },  # hope
        'hosts': [
            {
                'language': 'english',
                'Response rate': 65,
                'Response time': 145,  # 145 min -> within a few hours
            }, {
                'language': ' Español',
                'response': {
                    'rate': 75,
                    'time': 125,
                }
            }
        ]
    },
]


def import_homes():
    response = requests.post(url + '*')
    print(response.content)
    for home in homes:
        response = requests.post(url + '+', data={'json': str(home)})
        print(response.content)


def show_one_home():
    from config import homes as db_homes
    import json
    _home = db_homes.find_one()
    _home['_id'] = str(_home['_id'])
    _home['place']['_id'] = str(_home['place']['_id'])
    for host in _home['hosts']:
        host['_id'] = str(host['_id'])
    print(json.dumps(_home, indent=3))

