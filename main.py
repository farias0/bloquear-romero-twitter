import schedule

# TODO requirements.txt

from events import Events
from block import Block
import settings

def _calculate_time(events):

  time_to = {}
  
  print("Scheduling block from " + time_to.block + " to " + time_to.unblock + ".")
  return time_to

if __name__ == '__main__':

  teams = settings.TEAMS
  id_to_block = settings.ID_TO_BLOCK
  
  block = Block()  

  events = Events()
  events.update(teams)
  
  print(str(events.get_events_size()) + " matches.")
  for event in events.get_events_today():
    print(str(event.event_id) + " | " + event.time + " | " + event.league + " | " + "".join(event.teams))

  # schedule
  #   events.update(teams)
  #   time_to = _calculate_time(events.events_today)

  # schedule em time_to.block
  #   block.block(id_to_block)

  # schedule em time_to.unblock
  #   block.unblock(id_do_block)


