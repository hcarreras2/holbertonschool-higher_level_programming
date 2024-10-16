#!/usr/bin/python3

import requests
import csv

# Function to fetch and print posts
def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    
    # Fetch data
    response = requests.get(url)
    
    # Print status code
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        # Parse JSON data
        posts = response.json()
        
        # Iterate through the posts and print titles
        for post in posts:
            print(f"Title: {post['title']}")
    else:
        print("Failed to fetch posts.")

# Function to fetch and save posts to CSV
def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    
    # Fetch data
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parse JSON data
        posts = response.json()
        
        # Structure data for CSV
        data_to_save = [{"id": post["id"], "title": post["title"], "body": post["body"]} for post in posts]
        
        # Write data to CSV
        with open("posts.csv", mode="w", newline="") as csv_file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            
            # Write header
            writer.writeheader()
            
            # Write rows
            for post in data_to_save:
                writer.writerow(post)
                
        print("Posts saved to posts.csv")
    else:
        print("Failed to fetch posts.")

# Test the functions
fetch_and_print_posts()  # This will print the titles of the posts
fetch_and_save_posts()   # This will save the posts into a CSV file
