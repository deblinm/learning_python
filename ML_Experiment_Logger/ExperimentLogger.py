from dataclasses import dataclass,field
from experiment import Experiment
from typing import List


@dataclass
class ExperimentLogger:
    experiments: List[Experiment]= field(default_factory=list)

    def add_new_experiment(self,experiment):
        self.experiments.append(experiment)

    def view_all_experiments(self):
        if not self.experiments:
            print("There are not experiment records to show. Consider adding an experiment first. Thank You")
        else:
            for exp in self.experiments:
                print (exp)


    def filter_by_model(self,model_name):
        count=0
        model_list=[]
        for exp in self.experiments:
            if exp.model_name == model_name:
                count += 1
                model_list.append(exp)

        if count == 0:
                    print(f"There are no match to the model name {model_name}. Please input the exact name and retry. Thank You")
        else:
            print(f"{count} model name matched. Here are the details \n")
            for models in model_list:
                print(models)



    def compare_experiment_outputs(self):
        pass

    def view_best_model(self):
        pass

    def save_to_csv(self):
        pass

    def load_from_csv(self):
        pass