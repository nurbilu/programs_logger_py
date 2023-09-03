import requests

api_key = 'https://api.api-ninjas.com/v1/convertcurrency?want=ILS&have=USD&amount=1'

def convert_currency():
    print("Currency Converter")
    have_currency = input("Enter the currency you have (e.g., USD): ")
    want_currency = input("Enter the currency you want (e.g., ILS): ")
    amount = float(input("Enter the amount you want to convert: "))

    api_url = f'https://api.api-ninjas.com/v1/convertcurrency?want={want_currency}&have={have_currency}&amount={amount}'
    headers = {'X-Api-Key': api_key}

    response = requests.get(api_url, headers=headers)

    if response.status_code == requests.codes.ok:
        data = response.json()
        formatted_response = f"New Amount: {data['new_amount']}, New Currency: {data['new_currency']}, Old Currency: {data['old_currency']}, Old Amount: {data['old_amount']}"
        print(formatted_response)
    else:
        print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    convert_currency()


