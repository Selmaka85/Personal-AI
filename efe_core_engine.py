# efe_core_engine.py

class EFECoreEngine:
    def __init__(self, config, routing_manager, scoring_module, logger):
        self.config = config
        self.routing_manager = routing_manager
        self.scoring_module = scoring_module
        self.logger = logger

    def evaluate(self, input_data):
        llm = self.routing_manager.direct_to_llm(input_data)
        output = llm.generate(input_data)
        score = self.scoring_module.evaluate_all(output)
        self.logger.save_logs(input_data, output, score)
        return output if score["total"] >= self.config.thresholds["accept"] else "Rerouted or rejected."

    def reroute(self, input_data):
        return self.routing_manager.fallback_logic(input_data)

    def compare(self, outputs):
        return self.scoring_module.select_best(outputs)