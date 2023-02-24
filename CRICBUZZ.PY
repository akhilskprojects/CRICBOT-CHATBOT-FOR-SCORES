import requests
import json

def get_match_scores(match_id):
    response = requests.get(f"https://www.cricbuzz.com/match-api/{match_id}/live-scores.json")

    # Go through the json by parsing
    data = json.loads(response.content)

    match_desc = data['header']['match_desc']
    batting_team = data['score']['batting']['team_name']
    score = data['score']['batting']['score']
    wickets = data['score']['batting']['wickets']
    overs = data['score']['batting']['overs']
    run_rate = data['score']['batting']['run_rate']
    req_run_rate = data['score']['run_rate']['required_run_rate']
    bowling_team = data['score']['bowling']['team_name']
    recent_overs = data['score']['recent_overs']

    message = f"{match_desc}\n{batting_team}: {score}/{wickets} ({overs} overs), RR: {run_rate}, RRR: {req_run_rate}\n{bowling_team}: {data['score']['bowling']['score']} ({data['score']['bowling']['overs']} overs)\nRecent Overs: {', '.join(recent_overs)}"

    return message

def main():
    print("Hello Im cricbot what match do you want the scores for?")

    while True:
        # Get user input
        user_input = input(" ")
        if user_input.lower() in ["quit", "bye"]:
            print("See You Again Buddy!")
            break
        try:
            match_id = user_input
            message = get_match_scores(match_id)
        except:
            message = "Enter A valid Match ID."
        print(message)

# Call the main function 
if __name__ == "__main__":
    main()