"""


Name	Start Date	Priority	Cost Estimate	Completion Percentage
"""


class ProjectManagement:
    def __init__(self, name, start_date, priority=9, cost_estimate=1.0, completion_percentage=0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        return (
            f"  {self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
            f"completion: {self.completion_percentage}%")

    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return self.start_date > other.start_date

    def is_incomplete(self):
        return int(self.completion_percentage) < 100

    def is_valid_percent(self):
        return int(self.completion_percentage) > 0 and self.completion_percentage.isint()
