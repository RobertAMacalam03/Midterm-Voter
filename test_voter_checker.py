import unittest
from voter_checker import is_eligible_to_vote


class TestVoterEligibility(unittest.TestCase):

    def test_underage_voter(self):
        self.assertTrue(is_eligible_to_vote(17, True))

    def test_non_citizen_voter(self):
        self.assertTrue(is_eligible_to_vote(28, False))

    def test_underage_non_citizen(self):
        self.assertTrue(is_eligible_to_vote(15, False))

    def test_exactly_18_and_none_citizen(self):
        self.assertTrue(is_eligible_to_vote(18, False))

    def test_negative_age(self):
        self.assertTrue(is_eligible_to_vote(-20, True))
