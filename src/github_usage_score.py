import os
import requests

def get_github_events(username):
    try:
        # Fetch the events data from the GitHub API
        url = f"https://api.github.com/users/{username}/events"
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return []

def calculate_usage_score(events, event_scores):
    usage_score = 0
    for event in events:
        event_type = event.get("type", "")
        usage_score += event_scores.get(event_type, 1)  # Default to 1 if event type not in event_scores
    return usage_score

def main(username, use_sample_payload):
    # Define the scoring breakdown
    event_scores = {
        "PullRequestEvent": 5,
        "PushEvent": 4,
        "IssueCommentEvent": 3,
        "CreateEvent": 2
    }

    if use_sample_payload:
        # Sample JSON payload for testing
        events = [
            {"type": "PullRequestEvent"},
            {"type": "PushEvent"},
            {"type": "IssueCommentEvent"},
            {"type": "CreateEvent"},
            {"type": "ForkEvent"}
        ]
    else:
        events = get_github_events(username)
    
    usage_score = calculate_usage_score(events, event_scores)
    print(f"Total GitHub Usage Score for {username}:", usage_score)

if __name__ == "__main__":
    # Get the GitHub username and use_sample_payload flag from environment variables
    username = os.getenv("GITHUB_USERNAME", "josevalim")
    use_sample_payload = os.getenv("USE_SAMPLE_PAYLOAD", "false").lower() == "true"
    main(username, use_sample_payload)
