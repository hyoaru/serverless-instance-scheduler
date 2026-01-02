from app.services.ec2_instance_state_manager.strategies import (
    StartInstancesByFilters,
    Ec2InstanceStateActionStrategyABC,
    StopInstancesByFilters,
)


class Ec2InstanceStateManagerStrategyFactory:
    @staticmethod
    def create(strategy: str) -> Ec2InstanceStateActionStrategyABC:
        supported_strategies = ["START", "STOP"]
        if strategy not in supported_strategies:
            raise ValueError(f"Unsupported strategy type {strategy}")

        match strategy:
            case "START":
                return StartInstancesByFilters()

        return StopInstancesByFilters()
