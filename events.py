from datetime import date
import requests
import json

from api_football_credentials import API_FOOTBALL_KEY
 
class _Event:
  def __init__(self, event_id, time, league, teams):
    self.event_id = event_id
    self.time = time
    self.league = league
    self.teams = teams

class Events:
  def __init__(self):
    self.__url = "https://api-football-v1.p.rapidapi.com/v2/"

    # TODO modularize timezone??
    self.__timezone = "America/Sao_Paulo"

    self.__api_football_key = API_FOOTBALL_KEY
    
    self.__events_today = []
    self.__last_updated = None

  def get_events_today(self):
    return self.__events_today
  
  def get_last_updated(self):
    return self.__last_updated

  def get_events_size(self):
    return len(self.__events_today)

  # rebuilds events_today based on the current date
  def update(self, teams):
    today = date.today().strftime("%Y-%m-%d")

    print("\nUpdating for " + today + "...")

    url = self.__url + "fixtures/date/" + today
    params = {"timezone":self.__timezone}
    headers = {"x-rapidapi-key":self.__api_football_key}

    print("\nRequesting " + url + "?timezone=" + params["timezone"] + " ...")

    response = requests.request("GET", url, headers=headers, params=params)
    parsed_response = json.loads(response.text)

    print("Status code " + str(response.status_code) + " in " + str(response.elapsed) + " (time).")
    try:
      response.raise_for_status()
      self.events_today = []
      print("\nStarting update...")
    except:
      print("\nSkipping update...")
      return

    for event in parsed_response["api"]["fixtures"]:
      if (event["homeTeam"]["team_id"] in teams or \
        event["awayTeam"]["team_id"] in teams):

        event_teams = []
        if (event["homeTeam"]["team_id"] in teams):
          event_teams.append(event["homeTeam"]["team_name"])
        if (event["awayTeam"]["team_id"] in teams):
          event_teams.append(event["awayTeam"]["team_name"])

        event_time = event["event_date"] # TODO build substring

        print("Found match for " + "".join(event_teams) + " at " + event_time)

        self.events_today.append(_Event(event["fixture_id"], event_time, \
          event["league"]["name"], event_teams))

    print("\nUpdate complete, " + str(len(self.events_today)) + " matches.")
    self.last_updated = today