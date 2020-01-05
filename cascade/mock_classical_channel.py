from cascade.classical_channel import ClassicalChannel
from cascade.key import Key
from cascade.shuffle import Shuffle

class MockClassicalChannel(ClassicalChannel):
    """
    A mock concrete implementation of the ClassicalChannel base class, which is used for the
    experiments.
    """

    # TODO: Add unit test

    def __init__(self, correct_key):
        assert isinstance(correct_key, Key)
        self._correct_key = correct_key
        self._id_to_shuffle = {}
        self._reconciliation_started = False

    def start_reconciliation(self):
        assert not self._reconciliation_started
        self._reconciliation_started = True

    def end_reconciliation(self):
        assert self._reconciliation_started
        self._reconciliation_started = False
        self._id_to_shuffle = {}

    def ask_parities(self, shuffle_ranges):

        # Validate arguments.
        assert isinstance(shuffle_ranges, list)
        assert self._reconciliation_started

        # Collect the parities of all the requested shuffle ranges.
        parities = []
        for shuffle_range in shuffle_ranges:

            # Validate shuffle range.
            assert isinstance(shuffle_range, tuple) and len(shuffle_range) == 3
            (shuffle_identifier, shuffle_start_index, shuffle_end_index) = shuffle_range
            assert isinstance(shuffle_identifier, int)
            assert isinstance(shuffle_start_index, int)
            assert isinstance(shuffle_end_index, int)

            # Create the shuffle from the identifier, if we don't already have it.
            if shuffle_identifier in self._id_to_shuffle:
                shuffle = self._id_to_shuffle[shuffle_identifier]
            else:
                shuffle = Shuffle.create_shuffle_from_identifier(shuffle_identifier)
                self._id_to_shuffle[shuffle_identifier] = shuffle

            # Compute the parity.
            parity = shuffle.calculate_parity(self._correct_key, shuffle_start_index,
                                              shuffle_end_index)
            parities.append(parity)

        return parities