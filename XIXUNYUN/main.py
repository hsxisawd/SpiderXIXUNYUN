import GetBaiDU_Address
from Login import Login
from SignIn import SignIn
import setting

if __name__ == "__main__":
    token = Login().login()['data']['token']
    SignIn().SignIn(token)
