import json
from config.settings import DAO_CONSTITUTION
from core.identity.agent import Agent

class DAO:
    """Manages governance and the economy based on its locked constitution."""
    def __init__(self):
        self._constitution = DAO_CONSTITUTION
        self.treasury_axm: float = self._constitution["economics"]["treasury_allocation"]
        self.investment_fund_axm: float = self._constitution["economics"]["investment_fund_allocation"]
        self.legal_defense_fund_axm: float = self._constitution["economics"]["legal_defense_fund_allocation"]

    def get_constitution_as_json(self) -> str:
        """Serializes the constitution for display."""
        return json.dumps(self._constitution, sort_keys=True, indent=2)

    def collect_fee(self, agent: Agent, amount: float):
        """A conceptual function for collecting network fees."""
        if agent.axm_balance < amount:
            raise Exception("Insufficient AXM balance for fee.")
        agent.axm_balance -= amount
        self.treasury_axm += amount