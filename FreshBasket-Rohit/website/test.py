from intasend import APIService

API_PUBLISHABLE_KEY = 'ISPubKey_test_afeed440-97ed-442b-8308-6eddf6d61541'
API_TOKEN = 'ISSecretKey_test_b1e2f910-dfa4-47d5-9d3c-7fe6b7501099'

service = APIService(token=API_TOKEN, publishable_key=API_PUBLISHABLE_KEY, test=True)

create_order = service.collect.mpesa_stk_push(phone_number='25472000000',
                                              email='test@gmail.com',
                                              amount=100,
                                              narrative='Purchase of items')

print(create_order)
