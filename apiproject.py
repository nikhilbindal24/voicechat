import requests
# url = "https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"

# data = requests.get(url)

# print(data)

def fetch_1():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

    data1 = requests.get(url)
    data = data1.json()

    if data.get("success") and "data" in data:
        user_name_email = data["data"]["name"]["first"] , data["data"]["name"]["last"] , data["data"]["email"]
        return user_name_email
    else:
        raise Exception("Data not found ")


store = fetch_1()
print(store)

