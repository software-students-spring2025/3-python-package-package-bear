import pytest
from buildabearpackage import buildabear

class Test:

    @pytest.fixture
    def test_buy_food(self):
        #test that it actually modifies the budget and food
        buildabear.budget = 100
        buildabear.food = 0
        reference = 100
        food_ref = 0
        for i in range(90):
            buildabear.buy_food(1)
            food_ref = food_ref+1
            assert buildabear.food == food_ref, f"Expected buy_food() to return {food_ref}. Instead it returned {buildabear.food}."
            
            assert buildabear.budget < reference(
                reference = reference-1
            ), f"Expected buy_food() to return {reference-1}. Instead it returned {buildabear.budget}."
            
    
    def test_buy_food_negative(self):
        #test that food does not go into the negatives/not enough money
        buildabear.budget = 0
        for i in range(90):
            buildabear.buy_food(1)
            assert buildabear.budget == 0, f"Expected buy_food() to return 0. Instead it returned {buildabear.budget}."

    
    def test_buy_food_multiple(self):
        #test the scenario where you buy multiple amounts of food
        buildabear.budget = 100
        for i in range(10):
            buildabear.buy_food(2)
            assert buildabear.budget == 80, f"Expected buy_food() to return 80. Instead it returned {buildabear.budget}."
        