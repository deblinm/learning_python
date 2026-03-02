from experiment import Experiment

def main():
    trial = Experiment(model_name="Test Model",
                       model_parameters={"max_depth": 5,
                                         "learning_rate": 0.01,
                                         "n_estimators": 100},
                       model_metrics={"accuracy": 0.95,
                                      "precision": 0.89,
                                      "recall": 0.91,
                                      "f1_score": 0.90},
                       experiment_date="03/01/2026",
                       notes="testing my program")
    print(trial)






if __name__ == "__main__":
    main()