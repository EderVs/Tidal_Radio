# -*- coding: utf-8 -*-
""" Users' utils """


tidals_sessions = {}


def add_tidal_session(username, session): 
    """
        Push tidal session to dict
    """

    tidals_sessions[username] = session


def get_tidal_session(username):
    """
        Get tidal session
    """
    
    return tidals_sessions.get(username, None)


def remove_tidal_session(username):
    """
        Remove tidal session to dict
    """

    if tidals_sessions.get(username, False):
        del tidals_sessions[username]

