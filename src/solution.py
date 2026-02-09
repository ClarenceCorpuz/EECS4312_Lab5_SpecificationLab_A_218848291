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

    WORK_START = to_minutes("09:00")
    WORK_END = to_minutes("17:00")
    FRIDAY_CUTOFF = to_minutes("15:00")
    SLOT_STEP = 15  # minutes

    # Convert events to minute intervals, ignoring those outside working hours
    busy_intervals = []
    for e in events:
        start = to_minutes(e["start"])
        end = to_minutes(e["end"])

        if end <= WORK_START or start >= WORK_END:
            continue

        busy_intervals.append(
            (max(start, WORK_START), min(end, WORK_END))
        )

    busy_intervals.sort()

    # Determine latest possible start time
    latest_start = WORK_END - meeting_duration


    if day == "Fri":
        latest_start = min(latest_start, FRIDAY_CUTOFF) #Lab 6 requirements for Friday Cutoff cannot start after 15:00

    valid_slots = []
    start = WORK_START

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
