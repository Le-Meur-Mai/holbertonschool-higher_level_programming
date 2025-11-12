#!/usr/bin/python3

import os

''' a Python function that generates personalized invitation files from a
template with placeholders and a list of objects.
Arguments:
template: text with placeholders
attendees: a list of dictionaries
return: Error on failure, nothing on success.'''


def generate_invitations(template, attendees):

    if not isinstance(template, str) or not isinstance(attendees, list):
        raise TypeError('template must be a string and attendees a list of'
                        'dictionaries.')

    elif len(template) <= 0:
        raise ValueError('Template is empty, no output files generated.')

    elif len(attendees) <= 0:
        raise ValueError('No data provided, no output files generated.')

    for invite in attendees:
        if not isinstance(invite, dict):
            raise ValueError('template must be a string and attendees a list'
                             ' of dictionaries.')
        for key in invite:
            if invite[key] is None:
                invite[key] = 'N/A'
    try:
        i = 0
        for attendee in attendees:
            i += 1
            if os.path.exists(f'./output_{i}.txt'):
                continue
            with open(
                    f'./output_{i}.txt', 'w', encoding='utf-8') as invitation:
                invitation.write(template.format(**attendee))

    except Exception:
        raise
