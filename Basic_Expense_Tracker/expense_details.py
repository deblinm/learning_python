from dataclasses import dataclass, field
from datetime import date
import uuid


@dataclass(kw_only=True)
class Expense:
        id: str = field(default_factory=lambda: uuid.uuid4().hex)
        category : str
        expense_type : str
        amount : float
        description : str
        expense_date: date = date.today()

        def __str__(self):
            return f"ID : {self.id}. On {self.expense_date} your {self.category} expense was {self.amount}"


