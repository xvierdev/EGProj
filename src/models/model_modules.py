from datetime import datetime


class Module:
    def __init__(
        self,
        module_id: int = 0,
        module_name: str = "",
        description: str = "",
        count_total_access: int = 0,
        record_user_id: int = 0,
        record_value: int = 0,
        record_datetime: datetime = NotImplemented,
    ):
        self.module_id = module_id
        self.module_name = module_name
        self.description = description
        self.count_total_access = count_total_access
        self.record_user_id = record_user_id
        self.record = record_value
        self.record_datetime = record_datetime

    def display_info(self) -> str:
        return f"{self.module_name=}, {self.description=}"
