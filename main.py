import schedule

# TODO requirements.txt

from events import Events
from mute import Mute
import settings

def _calculate_time(events):

  time_to = {}
  
  print("Scheduling block from " + time_to.block + " to " + time_to.unblock + ".")
  return time_to

if __name__ == '__main__':

  # teams = settings.TEAMS
  ids_to_mute = settings.USERS_IDS
  # timezone = settings.TIMEZONE
  
  mute = Mute(ids_to_mute)
  print(mute.was_muted)
  mute.unmute()  
  print(mute.me)


  # events = Events(teams, timezone)
  # events.update()
  
  # print(str(events.size()) + " matches.")
  # for event in events.today():
  #   print(str(event.event_id) + " | " + event.time + " | " + event.league + " | " + "".join(event.teams))

  # schedule
  #   events.update(teams)
  #   time_to = _calculate_time(events.events_today)

  # schedule em time_to.block
  #   block.block(ids_to_block)

  # schedule em time_to.unblock
  #   block.unblock(ids_do_block)


