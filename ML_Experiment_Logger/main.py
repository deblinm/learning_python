from  ExperimentLogger_API import ExperimentLogger as EL
from fastapi import FastAPI
from dataclasses import asdict
from pydantic import BaseModel
from datetime import date

EL_OBJ = EL()
app = FastAPI()


@app.get("/view_all_experiments")
def view_all_experiment():
        if not EL_OBJ.experiments:
                return {"message": "There are not experiment records to show. Consider adding an experiment first. Thank You."}
        else:
                return [asdict(exp) for exp in EL_OBJ.experiments]



@app.get("/experiments/{exp_id}")
def get_experiment_by_id (exp_id: str):
        match = next((exp for exp in EL_OBJ.experiments if exp.id == exp_id), None)
        if not match:
                return {"message": f"No experiment found with id {exp_id}"}
        return asdict(match)

class Experiment_Inp(BaseModel):
        model_name: str
        model_parameters: dict
        model_metrics: dict
        experiment_date: date = date.today()
        notes: str
        status: str = 'completed'

