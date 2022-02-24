import pandas as pd

# Reading the data
df = pd.read_csv('binary_data.csv')
df = df.set_index('company')

# Removing American-only apps
df = df.drop('walmart', axis=0)
df = df.drop('protect_scotland', axis=0)
df = df.drop('offerup', axis=0)
df = df.drop('doordash', axis=0)
df = df.drop('amtrak', axis=0)

# Adjustments to base data
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
df.loc['ocado', 'location'] = 1
# Source https://www.ocado.com/webshop/scontent/privacyPolicy
df.loc['paypal', 'social_profile_friends'] = 1
# Source https://www.paypal.com/uk/webapps/mpp/ua/privacy-full#2
df.loc['google_maps', 'mobile_number'] = 1
df.loc['google_maps', 'location'] = 1
df.loc['google_maps', 'address'] = 1  # App store
df.loc['google_maps', 'contacts'] = 1  # App store
df.loc['google_maps', 'bank_account'] = 1  # App store
df.loc['google_maps', 'mobile_number'] = 1  # App store
df.loc['google_maps', 'camera_roll'] = 1  # App store
# Source https://policies.google.com/privacy?hl=en-US#footnote-personal-info
# Source https://support.google.com/youtube/answer/10364219?hl=en-GB#zippy=%2Chow-youtube-may-use-data-linked-to-your-account
# The second source above confirms that google detail the data categories that they collect in the app store, as such
# the app store index for google maps has been used to update the base data
df.loc['youtube', 'location'] = 1
df.loc['youtube', 'contacts'] = 1
df.loc['youtube', 'bank_account'] = 1
df.loc['youtube', 'address'] = 1
df.loc['youtube', 'camera_roll'] = 1
df.loc['youtube', 'voice_recognition'] = 1
# Source same as google maps
df.loc['slack', 'bank_account'] = 1
df.loc['slack', 'location'] = 1
df.loc['slack', 'contacts'] = 1
df.loc['slack', 'employer'] = 1
# Source https://slack.com/intl/en-gb/trust/privacy/privacy-policy#:~:text=Slack%20may%20share%20and%20disclose,applicable%20law%20and%20legal%20process.
df.loc['ikea_app', 'location'] = 1
df.loc['ikea_app', 'birth_country'] = 1
# Source https://www.ikea.com/gb/en/customer-service/privacy-policy/
df.loc['amazon', 'contacts'] = 1
df.loc['amazon', 'location'] = 1
df.loc['amazon', 'health_info'] = 1
df.loc['amazon', 'camera_roll'] = 1
df.loc['amazon', 'voice_recognition'] = 1
# Source amazon.co.uk/gp/help/customer/display.html?nodeId=GX7NJQ4ZB8MHFRNJ#GUID-A440AA65-7F7E-4134-8FA8-842156F43EEE__SECTION_22160257376047E78334D565CD73852D
df.loc['trainline', 'address'] = 1
df.loc['trainline', 'voice_recognition'] = 1
df.loc['trainline', 'social_profile_friends'] = 1
df.loc['trainline', 'social_profile_hobbies'] = 1
df.loc['trainline', 'social_profile_interests'] = 1
df.loc['trainline', 'location'] = 1
df.loc['trainline', 'camera_roll'] = 1  # App store
# Source https://www.thetrainline.com/terms/privacy
df.loc['slimming_world', 'mobile_number'] = 1
df.loc['slimming_world', 'home_number'] = 1
df.loc['slimming_world', 'interests'] = 1
df.loc['slimming_world', 'social_profile_friends'] = 1
df.loc['slimming_world', 'social_profile_hobbies'] = 1
df.loc['slimming_world', 'social_profile_interests'] = 1
# Source https://www.slimmingworld.co.uk/privacy-policy#:~:text=When%20you%20sign%20in%20to,your%20sign%2Din%20details%20again.
df.loc['whatsapp', 'bank_account'] = 1
df.loc['whatsapp', 'location'] = 1
df.loc['whatsapp', 'social_profile_friends'] = 1
df.loc['whatsapp', 'social_profile_hobbies'] = 1
df.loc['whatsapp', 'social_profile_interests'] = 1
# Source https://www.whatsapp.com/legal/updates/privacy-policy/
df.loc['zoom', 'mobile_number'] = 1
df.loc['zoom', 'employment_status'] = 1
df.loc['zoom', 'job'] = 1
df.loc['zoom', 'employer'] = 1
df.loc['zoom', 'face_recognition'] = 1
df.loc['zoom', 'voice_recognition'] = 1
df.loc['zoom', 'bank_account'] = 1
df.loc['zoom', 'camera_roll'] = 1  # App store
# Source https://explore.zoom.us/en/privacy/
df.loc['deliveroo', 'interests'] = 1
df.loc['deliveroo', 'location'] = 1  # App store
df.loc['deliveroo', 'camera_roll'] = 1  # App store
# Source https://corporate.deliveroo.co.uk/privacy-policy/
df.loc['costar', 'languages'] = 1
# Source https://www.costarastrology.com/privacy#:~:text=Co%2DStar%20does%20not%20sell,and%20for%20other%20commercial%20purposes.
df.loc['cvs_pharmacy', 'health_info'] = 1
df.loc['cvs_pharmacy', 'bank_account'] = 1
df.loc['cvs_pharmacy', 'camera_roll'] = 1
df.loc['cvs_pharmacy', 'location'] = 1
# Source is app store which is more detailed than their privacy policy
# https://www.cvshealth.com/app-privacy-policy
df.loc['coinbase', 'gender'] = 1
df.loc['coinbase', 'mobile_number'] = 1
df.loc['coinbase', 'home_number'] = 1
df.loc['coinbase', 'employer'] = 1
df.loc['coinbase', 'job'] = 1
df.loc['coinbase', 'voice_recognition'] = 1
df.loc['coinbase', 'location'] = 1
df.loc['coinbase', 'social_profile_hobbies'] = 1
df.loc['coinbase', 'social_profile_interests'] = 1
# Source https://www.coinbase.com/legal/privacy
df.loc['justeat', 'location'] = 1
df.loc['justeat', 'mobile_number'] = 1
df.loc['justeat', 'home_number'] = 1
df.loc['justeat', 'religion'] = 1
# Source https://www.just-eat.co.uk/info/privacy-policy
df.loc['facetune', 'name'] = 1
df.loc['facetune', 'mobile_number'] = 1
df.loc['facetune', 'home_number'] = 1
df.loc['facetune', 'bank_account'] = 1
df.loc['facetune', 'social_profile_friends'] = 1
df.loc['facetune', 'social_profile_hobbies'] = 1
df.loc['facetune', 'social_profile_interests'] = 1
df.loc['facetune', 'location'] = 1  # App store
# Source https://static.lightricks.com/legal/Lightricks-Privacy-Policy-13-06-2019.pdf
df.loc['wetherspoon', 'address'] = 1
df.loc['wetherspoon', 'mobile_number'] = 1
df.loc['wetherspoon', 'home_number'] = 1
df.loc['wetherspoon', 'location'] = 1
# Source https://www.jdwetherspoon.com/pubs/order-and-pay-app/app-privacy-policy
df.loc['pornhub', 'bank_account'] = 1
df.loc['pornhub', 'gender'] = 1
# For models Pornhub also collect biometric information, voice recognition and face recognition
# Source https://www.pornhub.com/information/privacy
df.loc['mcdonalds_usa', 'age'] = 1
df.loc['mcdonalds_usa', 'address'] = 1
df.loc['mcdonalds_usa', 'device_type'] = 1
df.loc['mcdonalds_usa', 'location'] = 1
df.loc['mcdonalds_usa', 'social_profile_friends'] = 1
df.loc['mcdonalds_usa', 'social_profile_hobbies'] = 1
df.loc['mcdonalds_usa', 'social_profile_interests'] = 1
# Source https://www.mcdonalds.com/gb/en-gb/privacy-policy/full.html#uk
df.loc['bet365_usa', 'location'] = 1
df.loc['bet365_usa', 'bank_account'] = 1
# Source https://help.bet365.com/en/privacy-policy
df.loc['headspace', 'mobile_number'] = 1
df.loc['headspace', 'home_number'] = 1
df.loc['headspace', 'address'] = 1
df.loc['headspace', 'health_info'] = 1  # App store
df.loc['headspace', 'location'] = 1  # App store
df.loc['headspace', 'social_profile_friends'] = 1
df.loc['headspace', 'social_profile_hobbies'] = 1
df.loc['headspace', 'social_profile_interests'] = 1
# Source https://www.headspace.com/privacy-policy
df.loc['google_docs', 'mobile_number'] = 1
df.loc['google_docs', 'location'] = 1
df.loc['google_docs', 'camera_roll'] = 1  # App store
df.loc['google_docs', 'address'] = 1  # App store
df.loc['google_docs', 'home_number'] = 1  # App store
# Source the same as for google maps
df.loc['google_sheets', 'mobile_number'] = 1
df.loc['google_sheets', 'location'] = 1
df.loc['google_sheets', 'camera_roll'] = 1  # App store
df.loc['google_sheets', 'address'] = 1  # App store
df.loc['google_sheets', 'home_number'] = 1  # App store
# Source the same as for google maps
df.loc['gmail', 'mobile_number'] = 1
df.loc['gmail', 'location'] = 1
df.loc['gmail', 'camera_roll'] = 1  # App store
df.loc['gmail', 'voice_recognition'] = 1  # App store
df.loc['gmail', 'address'] = 1  # App store
df.loc['gmail', 'home_number'] = 1  # App store
# Source the same as for google maps
df.loc['vsco', 'mobile_number'] = 1
df.loc['vsco', 'home_number'] = 1
df.loc['vsco', 'bank_account'] = 1
df.loc['vsco', 'social_profile_friends'] = 1
df.loc['vsco', 'social_profile_hobbies'] = 1
df.loc['vsco', 'social_profile_interests'] = 1
df.loc['vsco', 'contacts'] = 1
df.loc['vsco', 'location'] = 1
# Source https://vsco.co/about/privacy_policy
df.loc['skybet', 'location'] = 1
df.loc['skybet', 'device_type'] = 1
df.loc['skybet', 'address'] = 1
df.loc['skybet', 'employer'] = 1
df.loc['skybet', 'past_employer'] = 1
df.loc['skybet', 'social_profile_hobbies'] = 1
df.loc['skybet', 'social_profile_interests'] = 1
df.loc['skybet', 'mobile_number'] = 1  # App store
df.loc['skybet', 'home_number'] = 1  # App store
# Source https://support.skybet.com/s/article/Cookies-Policy-Privacy-Notice#information_from_you
df.loc['flo_my_health', 'name'] = 1
df.loc['flo_my_health', 'location'] = 1
df.loc['flo_my_health', 'languages'] = 1
df.loc['flo_my_health', 'gender'] = 1
df.loc['flo_my_health', 'weight'] = 1
df.loc['flo_my_health', 'camera_roll'] = 1  # App store
# Source https://flo.health/privacy-policy#1
df.loc['facebook', 'bank_account'] = 1
df.loc['facebook', 'health_info'] = 1  # App store
# Source https://en-gb.facebook.com/policy.php
df.loc['instagram', 'religion'] = 1
df.loc['instagram', 'race'] = 1
df.loc['instagram', 'health_info'] = 1
df.loc['instagram', 'bank_account'] = 1
df.loc['instagram', 'gender'] = 1
# Source https://help.instagram.com/519522125107875/?maybe_redirect_pol=0


# Combining the hobbies/interests columns and mobile_number/home_number columns
adjusted = df.drop('home_number', axis=1).copy()
adjusted = adjusted.drop('hobbies', axis=1)
adjusted.loc[df['home_number'] == 1, 'mobile_number'] = 1
adjusted.loc[df['hobbies'] == 1, 'interests'] = 1
adjusted.rename(columns={'mobile_number': 'phone_number'}, inplace=True)

adjusted.rename(index={'mcdonalds_usa': 'mcdonalds', 'bet365_usa': 'bet365'}, inplace=True)

# Writing the data to csv
adjusted.to_csv('binary_adjusted.csv')
