from urllib.parse import urlparse
'''
Classification= [['End of Season Sale is Live!', 'Urgency'], ['₹12,599 30% OFF', 'Urgency'], ['Flat 50% off on buying 3 products or more', 'Urgency'], ['Innovative, Modern and Luxury, Da Milano is dedicated to a vision of style that provides sublimity of opulence from the House of great craftsmanship and genuine leather.', 'Obstruction'], ['Get the latest launches and event updates directly in your inbox,sign up to our newsletter:', 'Scarcity'], ["We use cookies to ensure that we give you the best experience on our website. If you continue we'll assume that you understand this.", 'Misdirection'], ['End of Season Sale is Live!', 'Urgency'], ['₹12,599 30% OFF', 'Urgency'], ['Flat 50% off on buying 3 products or more', 'Urgency'], ['Innovative, Modern and Luxury, Da Milano is dedicated to a vision of style that provides sublimity of opulence from the House of great craftsmanship and genuine leather.', 'Obstruction'], ['Get the latest launches and event updates directly in your inbox,sign up to our newsletter:', 'Scarcity'], ["We use cookies to ensure that we give you the best experience on our website. If you continue we'll assume that you understand this.", 'Misdirection'], ['End of Season Sale is Live!', 'Urgency'], ['₹12,599 30% OFF', 'Urgency'], ['Flat 50% off on buying 3 products or more', 'Urgency'], ['Innovative, Modern and Luxury, Da Milano is dedicated to a vision of style that provides sublimity of opulence from the House of great craftsmanship and genuine leather.', 'Obstruction'], ['Get the latest launches and event updates directly in your inbox,sign up to our newsletter:', 'Scarcity'], ['End of Season Sale is Live!', 'Urgency'], ['₹12,599 30% OFF', 'Urgency'], ['Flat 50% off on buying 3 products or more', 'Urgency'], ['Innovative, Modern and Luxury, Da Milano is dedicated to a vision of style that provides sublimity of opulence from the House of great craftsmanship and genuine leather.', 'Obstruction'], ['Get the latest launches and event updates directly in your inbox,sign up to our newsletter:', 'Scarcity'], ['End of Season Sale is Live!', 'Urgency'], ['End of Season Sale is Live!', 'Urgency'], ['End of Season Sale is Live!', 'Urgency'], ['End of Season Sale is Live!', 'Urgency'], ['End of Season Sale is Live!', 'Urgency'], ['End of Season Sale is Live!', 'Urgency'], ['End of Season Sale is Live!', 'Urgency'], ['End of Season Sale is Live!', 'Urgency'], ['End of Season Sale is Live!', 'Urgency'], ['End of Season Sale is Live!', 'Urgency'], ['End of Season Sale is Live!', 'Urgency'], ['₹12,599 30% OFF', 'Urgency'], ['Flat 50% off on buying 3 products or more', 'Urgency'], ['Innovative, Modern and Luxury, Da Milano is dedicated to a vision of style that provides sublimity of opulence from the House of great craftsmanship and genuine leather.', 'Obstruction'], ['₹12,599 30% OFF', 'Urgency'], ['Flat 50% off on buying 3 products or more', 'Urgency'], ['₹12,599 30% OFF', 'Urgency'], ['Flat 50% off on buying 3 products or more', 'Urgency'], ['₹12,599 30% OFF', 'Urgency'], ['Flat 50% off on buying 3 products or more', 'Urgency'], ['₹12,599 30% OFF', 'Urgency'], ['Flat 50% off on buying 3 products or more', 'Urgency'], ['₹12,599 30% OFF', 'Urgency'], ['Flat 50% off on buying 3 products or more', 'Urgency'], ['₹12,599 30% OFF', 'Urgency'], ['Flat 50% off on buying 3 products or more', 'Urgency'], ['₹12,599 30% OFF', 'Urgency'], ['Flat 50% off on buying 3 products or more', 'Urgency'], ['₹12,599 30% OFF', 'Urgency'], ['Flat 50% off on buying 3 products or more', 'Urgency'], ['₹12,599 30% OFF', 'Urgency'], ['Flat 50% off on buying 3 products or more', 'Urgency'], ['Flat 50% off on buying 3 products or more', 'Urgency'], ['Flat 50% off on buying 3 products or more', 'Urgency'], ['Flat 50% off on buying 3 products or more', 'Urgency'], ['Flat 50% off on buying 3 products or more', 'Urgency'], ['Flat 50% off on buying 3 products or more', 'Urgency'], ['Innovative, Modern and Luxury, Da Milano is dedicated to a vision of style that provides sublimity of opulence from the House of great craftsmanship and genuine leather.', 'Obstruction'], ['Innovative, Modern and Luxury, Da Milano is dedicated to a vision of style that provides sublimity of opulence from the House of great craftsmanship and genuine leather.', 'Obstruction'], ['Innovative, Modern and Luxury, Da Milano is dedicated to a vision of style that provides sublimity of opulence from the House of great craftsmanship and genuine leather.', 'Obstruction'], ['Innovative, Modern and Luxury, Da Milano is dedicated to a vision of style that provides sublimity of opulence from the House of great craftsmanship and genuine leather.', 'Obstruction'], ['Innovative, Modern and Luxury, Da Milano is dedicated to a vision of style that provides sublimity of opulence from the House of great craftsmanship and genuine leather.', 'Obstruction'], ['Innovative, Modern and Luxury, Da Milano is dedicated to a vision of style that provides sublimity of opulence from the House of great craftsmanship and genuine leather.', 'Obstruction'], ['Innovative, Modern and Luxury, Da Milano is dedicated to a vision of style that provides sublimity of opulence from the House of great craftsmanship and genuine leather.', 'Obstruction'], ['Innovative, Modern and Luxury, Da Milano is dedicated to a vision of style that provides sublimity of opulence from the House of great craftsmanship and genuine leather.', 'Obstruction'], ['Innovative, Modern and Luxury, Da Milano is dedicated to a vision of style that provides sublimity of opulence from the House of great craftsmanship and genuine leather.', 'Obstruction'], ['Innovative, Modern and Luxury, Da Milano is dedicated to a vision of style that provides sublimity of opulence from the House of great craftsmanship and genuine leather.', 'Obstruction'], ['Innovative, Modern and Luxury, Da Milano is dedicated to a vision of style that provides sublimity of opulence from the House of great craftsmanship and genuine leather.', 'Obstruction'], ['Innovative, Modern and Luxury, Da Milano is dedicated to a vision of style that provides sublimity of opulence from the House of great craftsmanship and genuine leather.', 'Obstruction'], ['Innovative, Modern and Luxury, Da Milano is dedicated to a vision of style that provides sublimity of opulence from the House of great craftsmanship and genuine leather.', 'Obstruction'], ['Get the latest launches and event updates directly in your inbox,sign up to our newsletter:', 'Scarcity'], ['Get the latest launches and event updates directly in your inbox,sign up to our newsletter:', 'Scarcity'], ['Get the latest launches and event updates directly in your inbox,sign up to our newsletter:', 'Scarcity'], ['Get the latest launches and event updates directly in your inbox,sign up to our newsletter:', 'Scarcity'], ['Get the latest launches and event updates directly in your inbox,sign up to our newsletter:', 'Scarcity'], ['Get the latest launches and event updates directly in your inbox,sign up to our newsletter:', 'Scarcity'], ['Get the latest launches and event updates directly in your inbox,sign up to our newsletter:', 'Scarcity'], ['Get the latest launches and event updates directly in your inbox,sign up to our newsletter:', 'Scarcity'], ['Get the latest launches and event updates directly in your inbox,sign up to our newsletter:', 'Scarcity'], ['Get the latest launches and event updates directly in your inbox,sign up to our newsletter:', 'Scarcity'], ["We use cookies to ensure that we give you the best experience on our website. If you continue we'll assume that you understand this.", 'Misdirection'], ["We use cookies to ensure that we give you the best experience on our website. If you continue we'll assume that you understand this.", 'Misdirection'], ["We use cookies to ensure that we give you the best experience on our website. If you continue we'll assume that you understand this.", 'Misdirection']]
Total_Dark_Patterns: 85
All_the_unique_dark_patterns: ['Urgency', 'Obstruction', 'Scarcity', 'Misdirection']
score=70
'''

import firebase_admin
from firebase_admin import credentials, db
from time import gmtime, strftime

# Path to your service account's private key
cred = credentials.Certificate('darkpattern-da8a1-firebase-adminsdk-fbsvc-9f6acec6ac.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://darkpattern-da8a1-default-rtdb.firebaseio.com/'
})

ref = db.reference('/')
#print(db.reference().get())

def upload_data(domain_name, dark_pattern_strings, total_dark_patterns, all_unique_dp, score):
    # Reference to the database
    
    ref = db.reference('/')
    domain_name = urlparse(domain_name).netloc
    domain_name = domain_name.replace('.', ',')

    # Data to upload
    data = {
        domain_name: {
            'Time':strftime("%Y-%m-%d %H:%M:%S", gmtime()),
            'Dark Pattern Strings': dark_pattern_strings,
            'Total Dark Patterns': total_dark_patterns,
            'All unique dp': all_unique_dp,
            'Score': score
        }
    }

    # Update the database
    ref.update(data)


#link='https://www.damilano.com/collections/women-handbags/products/medium-wax-quilting-leather-satchel-misa-rose-lb-00309amisa-rosewax-quilting'
#domain = urlparse(link).netloc
#sanitized_domain_name = domain.replace('.', ',')
#dark_pattern_strings = 'Classification'
#total_dark_patterns = 85
#all_unique_dp = ['Urgency', 'Obstruction', 'Scarcity', 'Misdirection']
#score = 85
#print(type(domain),type(dark_pattern_strings),type(total_dark_patterns),type(all_unique_dp))
#upload_data('sanitized_domain_name', dark_pattern_strings, total_dark_patterns, all_unique_dp, score)
