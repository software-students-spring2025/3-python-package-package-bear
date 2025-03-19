import pytest
from buildabearpackage import buildabear
import time

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


    #feed bear tests
    def test_feed_bear_increase(self):
        buildabear.food = 2
        buildabear.hunger = 20
        buildabear.lastChecked = time.time()
        buildabear.feed_bear()
        assert buildabear.hunger == 30, f"Expected hunger variable to be 30. Instead it returned {buildabear.hunger}."
    
    def test_feed_bear_food_count(self):
        buildabear.food = 2
        buildabear.lastChecked = time.time()
        buildabear.feed_bear()
        assert buildabear.food == 1, f"Expected food variable to be 1. Instead it returned {buildabear.food}."

    def test_feed_bear_no_food(self):
        buildabear.food = 0
        buildabear.hunger = 20
        buildabear.happiness = 30
        buildabear.lastChecked = time.time()
        buildabear.feed_bear()
        assert buildabear.food == 0, f"Expected food variable to be 0. Instead it returned {buildabear.food}."
        assert buildabear.hunger == 20, f"Expected hunger variable to be 20. Instead it returned {buildabear.hunger}."
        assert buildabear.happiness == 20, f"Expected happiness variable to be 20. Instead it returned {buildabear.happiness}."
    
    #clean bear tests
    def test_clean_bear_increase(self):
        buildabear.cleanliness = 20
        buildabear.lastChecked = time.time()
        buildabear.clean_bear()
        assert buildabear.cleanliness == 50, f"Expected cleanliness variable to be 50. Instead it returned {buildabear.cleanliness}."

    def test_clean_bear_multiple(self):
        buildabear.cleanliness = 0
        buildabear.lastChecked = time.time()
        for i in range(3):
            buildabear.clean_bear()
        assert buildabear.cleanliness == 90, f"Expected cleanliness variable to be 90. Instead it returned {buildabear.cleanliness}."
    
    def test_clean_bear_time_passed(self):
        buildabear.cleanliness = 20
        buildabear.lastChecked = time.time()
        time.sleep(300)
        buildabear.clean_bear()
        assert buildabear.cleanliness == 47, f"Expected cleanliness variable to be 47. Instead it returned {buildabear.cleanliness}."

    #play with bear tests
    def test_play_bear_increase(self):
        buildabear.happiness = 20
        buildabear.lastChecked = time.time()
        buildabear.play_with_bear()
        assert buildabear.happiness == 40, f"Expected happiness variable to be 40. Instead it returned {buildabear.happiness}."
    
    def test_play_bear_multiple(self):
        buildabear.happiness = 0
        buildabear.lastChecked = time.time()
        for i in range(3):
            buildabear.play_with_bear()
        assert buildabear.cleanliness == 60, f"Expected happiness variable to be 60. Instead it returned {buildabear.happiness}."

    def test_play_bear_time_passed(self):
        buildabear.happiness = 20
        buildabear.lastChecked = time.time()
        time.sleep(300)
        buildabear.play_with_bear()
        assert buildabear.happiness == 37, f"Expected happiness variable to be 37. Instead it returned {buildabear.happiness}."
