from dice import Dice

class TestDice:
  def test_is_dice(self):
      dice = Dice()
      assert isinstance(dice, Dice)
      
  def test_roll(self):
      dice = Dice()
      assert dice.roll() in [1,2,3,4,5,6]

