unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = ['julio']

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user {current_user.title()}")
    confirmed_users.append(current_user)

print("\n\tThe following users have been confirmed:")
for user in confirmed_users:
    print(user.title())
