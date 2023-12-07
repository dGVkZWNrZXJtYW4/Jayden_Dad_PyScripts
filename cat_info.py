import requests

# here we are defining a function that will call the cat facts api (application program interface) 
def get_cat_fact():
    url = "https://catfact.ninja/fact"
    try:
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            return data['fact']
        else:
            return "Failed to retrieve cat fact"
    except Exception as e:
        return f"An error occurred: {e}"

# define a variable based on the response from the api
cat_fact = get_cat_fact()

#print the variable containing the retrieved cat fact, but also print a blank line before and after
print()
print(cat_fact)
print()
