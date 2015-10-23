from cards.player import Player
import unittest

class TestPlayer(unittest.TestCase):
    def test_human_player_creation(self):
        player_name = "Test Human"
        player = Player(player_name, 1)
        self.assertIsNotNone(player)
        self.assertEqual(player.name, player_name)
        self.assertEqual(player.human, 1)

    def test_cpu_player_creation(self):
        player_name = "Test CPU"
        player = Player(player_name)
        self.assertIsNotNone(player)
        self.assertEqual(player.human, 0)

    def test_set_name(self):
        original_player_name = "Test"
        new_player_name = "Bob"
        player = Player(original_player_name)
        self.assertEqual(player.name, original_player_name)
        player.set_name(new_player_name)
        self.assertEqual(player.name, new_player_name)

    def test_set_human(self):
        player = Player("CPU")
        self.assertEqual(player.human, 0)
        player.set_human()
        self.assertEqual(player.human, 1)

if __name__ == '__main__':
    unittest.main()
