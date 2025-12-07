RESTful API: JSONPlaceholder Posts
Overview

This project demonstrates basic interactions with a RESTful API using Python. It leverages the requests library to fetch data from JSONPlaceholder
, a free online REST API for testing and prototyping.

Students will learn how to:

Send HTTP GET requests using requests

Parse JSON responses

Extract and manipulate structured data

Export data to CSV format

Project Structure
restful-api/
├── task_02_requests.py
└── posts.csv (generated)

Requirements

Python 3.x

requests library

Install requests if not already installed:

pip install requests

Usage
Fetch and print post titles
#!/usr/bin/python3
"""
Fetch posts from JSONPlaceholder and print their titles
"""

import requests


def fetch_and_print_posts():
    """Fetch all posts and print their titles"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print("Status Code:", response.status_code)
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


Example usage:

from task_02_requests import fetch_and_print_posts

fetch_and_print_posts()


Sample Output:

Status Code: 200
sunt aut facere repellat provident occaecati excepturi optio reprehenderit
qui est esse
ea molestias quasi exercitationem repellat qui ipsa sit aut
...

Fetch posts and save to CSV
#!/usr/bin/python3
"""
Fetch posts from JSONPlaceholder and save them to posts.csv
"""

import requests
import csv


def fetch_and_save_posts():
    """Fetch all posts and save them to posts.csv"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        data_list = [{"id": post["id"], "title": post["title"], "body": post["body"]}
                     for post in posts]
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["id", "title", "body"])
            writer.writeheader()
            for data in data_list:
                writer.writerow(data)


Example usage:

from task_02_requests import fetch_and_save_posts

fetch_and_save_posts()


Generates a posts.csv file containing all posts

CSV columns: id, title, body
