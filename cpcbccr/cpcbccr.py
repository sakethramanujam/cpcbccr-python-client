from typing import List
import pandas as pd
from .config import API_URL
from .state import State
from .tools import get


def get_state(state: str) -> State:
    """
    Returns a "State" object

    Arguments:
    ---
    state: str

    Examples:
    ---
    state = get_state(state="Andhra Pradesh")
    state
    <object Andhra Pradesh>
    """
    r = get(f'{API_URL}/states')
    status = r.status_code
    if status != 200:
        raise Exception(f'failed to fetch <{state}> with status {status}')
    if state in r.json()['states']:
        return State(state)
    else:
        raise Exception(f"<{state} not found/does not exist")


def get_states() -> List[State]:
    """
    Returns a list of 
    available "State" objects

    Examples
    ---
    >>> states = client.get_states()
    >>> states
    ['<object Andhra Pradesh>','<object Karnataka>',....]
    """
    r = get(f'{API_URL}/states')
    status = r.status_code
    if status != 200:
        raise Exception(f'failed to fetch states {r.status_code}')
    states = [State(state) for state in r.json()['states']]
    return states