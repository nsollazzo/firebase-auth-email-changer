# firebase-auth-email-changer
Manually change a firebase auth email with this python script

# Steps

## 1. install 'firebase-admin'

```sh
pip install firebase-admin
```

## 2. get the 'serviceAccountKey.json' from firebase

You can [follow this guide](https://clemfournier.medium.com/how-to-get-my-firebase-service-account-key-file-f0ec97a21620) to get the file.

## 3. run the script

```sh
python main.py
```

## 4. enter the 'user_id_to_update' and 'new_email_address'

from the terminal enter the **user_id_to_update** that you find on the firebase auth page and the **new_email_address** that you want to use.