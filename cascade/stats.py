class Stats:
    """
    Stats of a single reconciliation.
    """

    def __init__(self):
        """
        Create a new stats block with all counters initialized to zero.
        """
        self.elapsed_process_time = None
        self.elapsed_real_time = None
        self.ask_parity_messages = 0
        self.ask_parity_blocks = 0
        self.infer_parity_blocks = 0