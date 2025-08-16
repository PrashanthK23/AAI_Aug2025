from pydantic import BaseModel
from typing import Optional

class Person_class(BaseModel):
    person_name:str
    person_height:Optional[float]=None
    person_age:Optional[int]=None

    model_config={"json_schema_extra":{"examples":[{
  "person_name": "mani",
  "person_height": 5.4,
  "person_age": 28
},
                      ]
                      }}