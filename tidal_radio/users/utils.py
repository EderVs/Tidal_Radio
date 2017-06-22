# -*- coding: utf-8 -*-
""" Users' utils """

import tidalapi
import requests

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


def remove_repeated_by_name(xs):
    """
        Removes repeated name attribute of list of objects in a new list
    """
    ys = []
    for x in xs:
        for y in ys:
            if x.name == y.name:
                break
        else:
            ys.append(x)
    return ys


def get_all_similar_artists_to_favs(username):
    """
        Gets all similar artists
    """
    session = tidals_sessions.get(username, None)
    if session is None:
        return None
    favs = tidalapi.Favorites(session, session.user.id)
    favs_artists = favs.artists()
    similar_artists = []
    for artist in favs_artists:
        try:
            similar_artists_i = session.get_artist_similar(artist.id)
            for similar_artist_i in similar_artists_i:
                for fav_artist in favs_artists:
                    if similar_artist_i.name == fav_artist.name:
                        break
                else:
                    similar_artists.append(similar_artist_i)
        except requests.exceptions.HTTPError:
            print('Error with ' + artist.name)
    return remove_repeated_by_name(similar_artists)

