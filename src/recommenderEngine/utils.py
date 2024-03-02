from faker import Faker
fake = Faker()

def create_fake_data(count = 10):
    userData = []
    for _ in range(count):
        userName = fake.profile()['username']
        userEmail = fake.profile()['mail']
        data = {
            'username' : userName,
            'email' : userEmail
        }
        if 'name' in fake.profile():
            data['first_name'],data['last_name'] = fake.profile()['name'].split(' ')[:2]
        userData.append(data)
    return userData


userData = create_fake_data()

