from typing import Set

from sqlalchemy.orm.base import manager_of_class
from sqlalchemy.orm.state import InstanceState


def loaded_attribute_names(state: InstanceState) -> Set[str]:
    """ Get the set of loaded attribute names """
    # This is the opposite of InstanceState.unloaded which is supposed to perform better
    # See: InstanceState.unloaded
    return set(state.dict) | set(state.committed_state)


def is_sa_mapped_class(class_: type) -> bool:
    """ Tell whether the object is an class mapped by SqlAlchemy, declarative or not """
    return manager_of_class(class_) is not None
