from game import Game
from simple_object import SimpleObject


def test_impossible_to_change_absent_object():
    game = Game(version=0, log=(), objects={}, name='Test', id='111')
    new_game = game.change_object(object_id='1115', new_value=12)
    assert new_game.version == 0
    assert len(new_game.log) == 1
    assert new_game.log[0] == 'Trying to change object 1115, but ' \
                              'there is no object with that ID in game 111'


def test_change_game_object():
    game = Game(
            version=0,
            log=(),
            objects={
                '112': SimpleObject(
                        name='One object',
                        id='1',
                )},
            name='Test',
            id='112',
    )
    new_game = game.change_object(object_id='112', new_value=11)
    assert new_game.version == 1
    assert len(new_game.log) == 1
    assert new_game.log[0] == 'Object 112 value was changed ' \
                              'from Initial value to 11'
    assert new_game.objects['112'].get_value() == 11
    assert new_game.objects['112'].get_last_version() == 1
