from  ExperimentLogger_API import ExperimentLogger as EL
from fastapi import FastAPI
from dataclasses import asdict
from pydantic import BaseModel
from datetime import date
from experiment import Experiment

EL_OBJ = EL()
app = FastAPI()

try:
    EL_OBJ.experiments = EL_OBJ.load_from_file()
except FileNotFoundError:
    pass


@app.get("/view_all_experiments")
def view_all_experiment():
        if not EL_OBJ.experiments:
                        return {"message": "No experiments found."}
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

@app.post("/add_new_experiment")
def add_experiment(exp_input: Experiment_Inp):
        new_exp = Experiment(**exp_input.model_dump())
        EL_OBJ.add_new_experiment(new_exp)
        EL_OBJ.save_to_file()
        return{"message": "Experiment added successfully", "id": new_exp.id}


