import firebase_admin
from firebase_admin import credentials, auth

# Initialize Firebase Admin SDK
cred = credentials.Certificate('./serviceAccountKey.json')
firebase_admin.initialize_app(cred)

def change_user_email(user_id, new_email):
    try:
        user = auth.update_user(user_id, email=new_email)
        print(f"Successfully updated email for user {user.uid}")
    except auth.AuthError as e:
        print(f"Error updating email: {e}")
    
if __name__ == "__main__":
    user_id_to_update = input("Enter the user ID to update: ")
    new_email_address = input("Enter the new email address: ")
    change_user_email(user_id_to_update, new_email_address)
