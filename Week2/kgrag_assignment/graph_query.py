from enum import Enum
from typing import Optional

from pydantic import BaseModel


class GraphIntent(str, Enum):

    SCHEMES_FOR_BENEFICIARY = "SCHEMES_FOR_BENEFICIARY"

    BENEFITS_OF_SCHEME = "BENEFITS_OF_SCHEME"

    DEPARTMENT_OF_SCHEME = "DEPARTMENT_OF_SCHEME"

    SCHEMES_BY_DEPARTMENT = "SCHEMES_BY_DEPARTMENT"


class GraphQuery(BaseModel):

    intent: GraphIntent

    scheme: Optional[str] = None

    beneficiary: Optional[str] = None

    department: Optional[str] = None