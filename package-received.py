# https://www.codewars.com/kata/6707688c0f597511f6649270/train/python


def was_package_received_yesterday(tz_from, tz_to, start, duration):
    start_utc = start - tz_from

    arrival_utc = start_utc + duration

    arrival_local = arrival_utc + tz_to

    return arrival_local < 0
