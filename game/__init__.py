from dataclasses import dataclass
from typing import Tuple, Any, Dict
from simple_object import SimpleObject


@dataclass(frozen=True)
class Game:
    """
    Game is just a set of SimpleObjects, that changes its version everytime
    when any of objects is changed. It also keeps logs of every change (even
    failure ones).
    There also should be possible to save and load game
    """
    version: int
    log: Tuple[str, ...]
    objects: Dict[str, SimpleObject]
    name: str
    id: str

    def change_object(self, object_id: str, new_value: Any) -> 'Game':
        if object_id not in self.objects:
            return Game(version=self.version,
                        objects=self.objects,
                        log=self.log + (f'Trying to change object '
                                        f'{object_id}, but there is no '
                                        f'object with that ID in game '
                                        f'{self.id}', ),
                        id=self.id,
                        name=self.name)

        target_object = self.objects[object_id]
        new_object = target_object.set_value(
                version=self.version + 1,
                value=new_value,
        )

        updated_objects = self.objects
        updated_objects[object_id] = new_object
        return Game(
                version=self.version + 1,
                log=self.log + (f'Object {object_id } value was changed from '
                                f'{target_object.get_value()} to '
                                f'{new_object.get_value()}', ),
                name=self.name,
                id=self.id,
                objects=updated_objects,
        )
