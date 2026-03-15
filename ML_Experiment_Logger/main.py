from experiment import Experiment
from  ExperimentLogger import ExperimentLogger as EL

def main():
    trial = Experiment(id = "EXP 1",
                       model_name="Test Model",
                       model_parameters={"max_depth": 5,
                                         "learning_rate": 0.01,
                                         "n_estimators": 100},
                       model_metrics={"accuracy": 0.95,
                                      "precision": 0.89,
                                      "recall": 0.91,
                                      "f1_score": 0.90},
                       experiment_date="03/01/2026",
                       notes="testing my program")

    trial1 = Experiment(id = "EXP 2",
                        model_name="Test Model2",
                       model_parameters={"max_depth": 3,
                                         "learning_rate": 0.03,
                                         "n_estimators": 100},
                       model_metrics={"accuracy": 0.90,
                                      "precision": 0.85,
                                      "recall": 0.90,
                                      "f1_score": 0.91},
                       experiment_date="03/02/2026",
                       notes="testing my second program")

    trial2 = Experiment(id = "EXP 3",
                        model_name="Test Model3",
                        model_parameters={"max_depth": 5,
                                          "learning_rate": 0.03,
                                          "n_estimators": 100},
                        model_metrics={"accuracy": 0.96,
                                       "precision": 0.88,
                                       "recall": 0.98,
                                       "f1_score": 0.95},
                        experiment_date="03/03/2026",
                        notes="testing my second program")
    EL_OBJ = EL()
    EL_OBJ.add_new_experiment(trial)
    EL_OBJ.add_new_experiment(trial1)
    EL_OBJ.add_new_experiment(trial2)
    EL_OBJ.view_all_experiments()
    EL_OBJ.filter_by_model("Test Model2")
    EL_OBJ.filter_by_model("Test Model3")
    EL_OBJ.compare_experiment_outputs("EXP 2","EXP 3")
    EL_OBJ.view_best_model("accuracy")
    EL_OBJ.save_to_file()
    EL_OBJ.load_from_file()







if __name__ == "__main__":
    main()