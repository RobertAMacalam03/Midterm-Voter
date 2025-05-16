import unittest
import voter_checker
from voter_checker import is_eligible_to_vote


class TestVoterEligibility(unittest.TestCase):

    def test_underage_voter(self):
        self.assertFalse(is_eligible_to_vote(16, True))

    def test_non_citizen_voter(self):
        self.assertFalse(is_eligible_to_vote(18, False))

    def test_underage_non_citizen(self):
        self.assertFalse(is_eligible_to_vote(15, False))

    def test_exactly_18_and_none_citizen(self):
        self.assertFalse(is_eligible_to_vote(18, False))

    def test_negative_age(self):
        with self.assertRaises(ValueError):
            voter_checker.is_eligible_to_vote(-18, True)
