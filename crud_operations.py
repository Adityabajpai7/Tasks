import requests


base_url = 'https://jsonplaceholder.typicode.com/posts'


def new_post(title, body, user_id):
    post_data = {
        'title': title,
        'body': body,
        'userId': user_id  
    }
    response = requests.post(base_url, json=post_data)
    if response.status_code == 201:
        print("Post created successfully:", response.json())
    else:
        print("Failed to create post:", response.status_code)


def read_post(post_id):
    url = f"{base_url}/{post_id}"
    response = requests.get(url)
    if response.status_code == 200:
        print("Post details:", response.json())
    else:
        print("Failed to retrieve post:", response.status_code)


def update_post(post_id, title=None, body=None, user_id=None):
    update_data = {}
    if title:
        update_data['title'] = title
    if body:
        update_data['body'] = body
    if user_id:
        update_data['userId'] = user_id
    
    url = f"{base_url}/{post_id}"
    response = requests.put(url, json=update_data)
    if response.status_code == 200:
        print("Post updated successfully:", response.json())
    else:
        print("Failed to update post:", response.status_code)


def delete_post(post_id):
    url = f"{base_url}/{post_id}"
    response = requests.delete(url)
    if response.status_code == 200:
        print("Post deleted successfully")
    else:
        print("Failed to delete post:", response.status_code)
