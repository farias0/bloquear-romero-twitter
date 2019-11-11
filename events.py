from datetime import date
import requests
import json

from api_football_credentials import API_FOOTBALL_KEY
 
class _Event:
  def __init__(self, event_id, time, league, teams):
    self.__event_id = event_id
    self.__time = time
    self.__league = league
    self.__teams = teams
  
  @property
  def event_id(self):
    return self.__event_id
  
  # @event_id.setter
  # def event_id(self, event_id):
  #   self.__event_id = event_id
  
  @property
  def time(self):
    return self.__time
  
  # @time.setter
  # def time(self, time):
  #   self.__time = time
  
  @property
  def league(self):
    return self.__league
  
  # @league.setter
  # def league(self, league):
  #   self.__league = league

  @property
  def teams(self):
    return self.__teams
  
  # @teams.setter
  # def teams(self, teams):
  #   self.__teams = teams

class Events:
  def __init__(self, teams, timezone):
    self.__teams = teams
    self.__timezone = timezone

    self.__url = "https://api-football-v1.p.rapidapi.com/v2/"

    self.__api_football_key = API_FOOTBALL_KEY
    
    self.__events_today = []
    self.__last_updated = None

  @property
  def today(self):
    return self.__events_today
  
  @property
  def last_updated(self):
    return self.__last_updated

  @property
  def teams(self):
    return self.__teams

  @property
  def size(self):
    return len(self.__events_today)

  # rebuilds events_today based on the current date
  def update(self):
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
      if (event["homeTeam"]["team_id"] in self.__teams or \
        event["awayTeam"]["team_id"] in self.__teams):

        event_teams = []
        if (event["homeTeam"]["team_id"] in __teams):
          event_teams.append(event["homeTeam"]["team_name"])
        if (event["awayTeam"]["team_id"] in __teams):
          event_teams.append(event["awayTeam"]["team_name"])

        event_time = event["event_date"] # TODO build substring

        print("Found match for " + "".join(event_teams) + " at " + event_time)

        self.events_today.append(_Event(event["fixture_id"], event_time, \
          event["league"]["name"], event_teams))

    print("\nUpdate complete, " + str(len(self.events_today)) + " matches.")
    self.last_updated = today