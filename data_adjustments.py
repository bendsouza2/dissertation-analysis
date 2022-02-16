import pandas as pd

# Reading the data
df = pd.read_csv('binary_data.csv')
df = df.set_index('company')


# Adjustments to base data
df.loc['deliveroo', 'interests'] = 1
# Source https://corporate.deliveroo.co.uk/privacy-policy/
df.loc['zoom', 'mobile_number'] = 1
df.loc['zoom', 'employment_status'] = 1
df.loc['zoom', 'job'] = 1
df.loc['zoom', 'employer'] = 1
df.loc['zoom', 'face_recognition'] = 1
df.loc['zoom', 'voice_recognition'] = 1
df.loc['zoom', 'bank_account'] = 1
# Source https://explore.zoom.us/en/privacy/
df.loc['trainline', 'location'] = 1
# Source https://www.thetrainline.com/terms/privacy
df.loc['sleepcycle', 'name'] = 1
# Source https://www.sleepcycle.com/privacy-policy-2021/#:~:text=Depending%20on%20what%20personal%20data,indicate%20information%20about%20your%20health.&text=We%20do%20not%20collect%20information,the%20app)%20to%20do%20so.
df.loc['nike', 'camera_roll'] = 1
df.loc['nike', 'location'] = 1
df.loc['nike', 'mobile_number'] = 1
# Source https://agreementservice.svs.nike.com/rest/agreement?requestType=redirect&agreementType=privacyPolicy&country=US&language=en&uxId=com.nike
df.loc['tinder', 'location'] = 1
# Source https://policies.tinder.com/privacy/intl/en
df.loc['grindr', 'location'] = 1
df.loc['grindr', 'health_info'] = 1  # HIV status is considered as health_info
# Source https://www.grindr.com/privacy-policy/?lang=en-US
df.loc['uber', 'bank_account'] = 1
df.loc['uber', 'health_info'] = 1
df.loc['uber', 'location'] = 1
# Source https://www.uber.com/legal/en/document/?country=united-states&lang=en&name=privacy-notice#kix.gse4r1unjrzd
df.loc['tiktok', 'location'] = 1
df.loc['tiktok', 'gender'] = 1
# https://www.tiktok.com/legal/privacy-policy-eea?lang=en
df.loc['strava', 'location'] = 1
df.loc['strava', 'health_info'] = 1
# Source https://www.strava.com/legal/privacy
df.loc['tesco', 'location'] = 1
df.loc['tesco', 'health_info'] = 1
# Source https://www.tesco.com/help/privacy-and-cookies/privacy-centre/privacy-policy-information/privacy-policy/
df.loc['spotify', 'location'] = 1
# Source https://www.spotify.com/us/legal/privacy-policy/#3-personal-data-we-collect-about-you
df.loc['myfitnesspal', 'location'] = 1
df.loc['myfitnesspal', 'health_info'] = 1
df.loc['myfitnesspal', 'social_profile_friends'] = 1
df.loc['myfitnesspal', 'social_profile_hobbies'] = 1
df.loc['myfitnesspal', 'social_profile_interests'] = 1
# Source https://www.myfitnesspal.com/privacy-policy
df.loc['clubhouse', 'interests'] = 1
df.loc['clubhouse', 'bank_account'] = 1
df.loc['clubhouse', 'location'] = 1
# Source https://privacy.clubhouse.com/#87909f4bd49d4a76b311331932caeb72
df.loc['jet2', 'bank_account'] = 1
df.loc['jet2', 'religion'] = 1  # not collected for all users
df.loc['jet2', 'health_info'] = 1
df.loc['jet2', 'social_profile_friends'] = 1
df.loc['jet2', 'social_profile_hobbies'] = 1
df.loc['jet2', 'social_profile_interests'] = 1
# Source https://www.jet2.com/en/privacy#personal
df.loc['credit_karma', 'gender'] = 1
df.loc['credit_karma', 'location'] = 1
df.loc['credit_karma', 'employer'] = 1
df.loc['credit_karma', 'employment_status'] = 1
# Source https://www.creditkarma.com/about/privacy-20200101
df.loc['twitter', 'address'] = 1
df.loc['twitter', 'mobile_number'] = 1
df.loc['twitter', 'home_number'] = 1
df.loc['twitter', 'voice_recognition'] = 1
df.loc['twitter', 'bank_account'] = 1
df.loc['twitter', 'location'] = 1
df.loc['twitter', 'interests'] = 1
# Source https://twitter.com/en/privacy
df.loc['airbnb', 'contacts'] = 1
df.loc['airbnb', 'health_info'] = 1
df.loc['airbnb', 'location'] = 1
df.loc['airbnb', 'social_profile_friends'] = 1
df.loc['airbnb', 'social_profile_hobbies'] = 1
df.loc['airbnb', 'social_profile_interests'] = 1
# Source https://www.airbnb.co.uk/help/article/3175/privacy-policy?_set_bev_on_new_domain=1645024914_ZmMyNGExNzc3Zjk4
df.loc['lidl_plus', 'location'] = 1
df.loc['lidl_plus', 'camera_roll'] = 1
# Source https://www.lidl.co.uk/pages/lidl-app-privacy-notice
df.loc['american_airlines', 'gender'] = 1
df.loc['american_airlines', 'face_recognition'] = 1
df.loc['american_airlines', 'health_info'] = 1
df.loc['american_airlines', 'employer'] = 1
df.loc['american_airlines', 'job'] = 1
# Source https://www.aa.com/i18n/customer-service/support/privacy-policy.jsp
df.loc['ebay', 'gender'] = 1
df.loc['ebay', 'birth_country'] = 1
df.loc['ebay', 'employment_status'] = 1
df.loc['ebay', 'interests'] = 1
df.loc['ebay', 'location'] = 1
df.loc['ebay', 'social_profile_friends'] = 1
df.loc['ebay', 'social_profile_hobbies'] = 1
df.loc['ebay', 'social_profile_interests'] = 1
# Source https://www.ebay.co.uk/help/policies/member-behaviour-policies/user-privacy-notice-privacy-policy?id=4260#section4
df.loc['asos', 'location'] = 1
# Source https://www.asosplc.com/privacy-policy/
df.loc['depop', 'voice_recognition'] = 1
df.loc['depop', 'location'] = 1
df.loc['depop', 'gender'] = 1
df.loc['depop', 'social_profile_friends'] = 1
df.loc['depop', 'social_profile_hobbies'] = 1
df.loc['depop', 'social_profile_interests'] = 1
# Source https://depophelp.zendesk.com/hc/en-gb/articles/360001792147-Privacy-Policy-#h_01FJ2FX6HD4NXD3HDAE744XSZP
df.loc['ryanair', 'face_recognition'] = 1
df.loc['ryanair', 'gender'] = 1
df.loc['ryanair', 'health_info'] = 1
df.loc['ryanair', 'location'] = 1
df.loc['ryanair', 'interests'] = 1
# Source https://www.ryanair.com/gb/en/corporate/privacy-policy
print(df.loc['ryanair'])