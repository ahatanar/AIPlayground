import requests



def get_cohere_response(prompt,action):
    cohere_api_key = 'CWDmyCR7osjXqlLmvGI1EPt5qN7iAsG3B3xjbFCj'

    url = f'https://api.cohere.ai/v1/{action}'
    print(url)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {cohere_api_key}'
    }

    data = {
        'prompt': prompt,
        'num_completions': 1,
    }

    response = requests.post(url, json=data, headers=headers,verify=False)
    response_json = response.json()
    print(response)
    generations = response_json.get('generations', [])
    if generations:
        return generations[0].get('text', '')
    else:
        return 'Error: Failed to retrieve response from Cohere API'
