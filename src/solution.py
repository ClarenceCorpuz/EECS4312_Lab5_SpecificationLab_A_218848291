## Student Name: Clarence Corpuz
## Student ID: 218848391

"""
Stub file for the meeting slot suggestion exercise.

Implement the function `suggest_slots` to return a list of valid meeting start times
on a given day, taking into account working hours, and possible specific constraints. See the lab handout
for full requirements.
"""
from typing import List, Dict

def suggest_slots(
    events: List[Dict[str, str]],
    meeting_duration: int,
    day: str
) -> List[str]:
    """
    Suggest possible meeting start times for a given day.

    Args:
        events: List of dicts with keys {"start": "HH:MM", "end": "HH:MM"}
        meeting_duration: Desired meeting length in minutes
        day: Three-letter day abbreviation (e.g., "Mon", "Tue", ... "Fri")

    Returns:
        List of valid start times as "HH:MM" sorted ascending
    """

    def to_minutes(t: str) -> int:
        h, m = map(int, t.split(":"))
        return h * 60 + m

    def to_time_str(minutes: int) -> str:
        return f"{minutes // 60:02d}:{minutes % 60:02d}"

    MEETINGSTART = to_minutes("09:00")
    MEETINGEND = to_minutes("17:00")
    SLOT_STEP = 30  # minutes

    # Convert events to minute intervals
    busy_intervals = [
        (to_minutes(e["start"]), to_minutes(e["end"]))
        for e in events
    ]

    busy_intervals.sort()

    valid_slots = []

    start = MEETINGSTART
    latest_start = MEETINGEND = to_minutes("17:00") - meeting_duration

    while start <= latest_start:
        end = start + meeting_duration
        conflict = False
        for busy_start, busy_end in busy_intervals:
            if start < busy_end and end > busy_start:
                conflict = True
                break

        if not conflict:
            valid_slots.append(to_time_str(start))

        start += SLOT_STEP

    return valid_slots
