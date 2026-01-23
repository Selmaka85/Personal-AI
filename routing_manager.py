# routing_manager.py

class RoutingManager:
    def __init__(self, llm_pool):
        self.llm_pool = llm_pool

    def direct_to_llm(self, input_data):
        # Simplified semantic match
        if "code" in input_data:
            return self.llm_pool.get("code")
        elif "strategy" in input_data:
            return self.llm_pool.get("strategy")
        else:
            return self.llm_pool.get("default")

    def fallback_logic(self, input_data):
        return self.llm_pool.get("backup").generate(input_data)