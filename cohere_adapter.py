import requests



def get_cohere_response(prompt,action):
    cohere_api_key = 'CWDmyCR7osjXqlLmvGI1EPt5qN7iAsG3B3xjbFCj'

    url = f'https://api.cohere.ai/v1/{action}'
    print(url)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {cohere_api_key}'
    }


    if action == 'summarize':
       data = {
        'text': prompt,
        'length': 'auto',
    }

    else:
        data = {
            'prompt': prompt,
            'num_completions': 5,
        }

    response = requests.post(url, json=data, headers=headers,verify=False)
    
    response_json = response.json()
    print(response_json)
    if response.status_code == 200:
        generations = response_json.get('generations', [])
        if generations:
            return generations[0].get('text', '')
        else:
            return 'Error: Failed to retrieve response from Cohere API'
    else:
            error_message = response_json.get('message', 'Unknown error occurred')
            return f'Error: {error_message}'
