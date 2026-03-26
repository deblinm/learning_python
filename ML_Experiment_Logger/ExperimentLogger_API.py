from dataclasses import dataclass, field, asdict
from experiment import Experiment
from typing import List
import json

@dataclass
class ExperimentLogger:
    experiments: List[Experiment]= field(default_factory=list)

    def add_new_experiment(self,experiment):
        self.experiments.append(experiment)

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



    def compare_experiment_outputs(self,user_inp1,user_inp2):
        match1 = next ((exp_nm for exp_nm in self.experiments if exp_nm.id == user_inp1),None)
        match2 = next((exp_nm for exp_nm in self.experiments if exp_nm.id == user_inp2), None)

        if not match1:
            print(
                f"There is no match found with experiment name {user_inp1}. Please input the exact name and retry. Thank You")
        elif not match2:
            print(
                f"There is no match found with experiment name {user_inp2}. Please input the exact name and retry. Thank You")
        else:
            print (f"{'':=<55}")
            print ("                 EXPERIMENT COMPARISON               ")
            print (f"{'':=<55}")
            print (f"{'':<15}{user_inp1[:20]}  {'':<5}| {'':<15}{user_inp2[:20]}")
            print (f"-------Metrics---------------")
            for key1, value1 in match1.model_metrics.items():
                print(f"{key1:<15}: {value1:<20}| {match2.model_metrics.get(key1, 'N/A')}")
            print(f"-------Parameters---------------")
            for key1, value1 in match1.model_parameters.items():
                print(f"{key1:<15}: {value1:<20}| {match2.model_parameters.get(key1, 'N/A')}")


    def view_best_model(self,in_metric):
        if not any(in_metric in exp.model_metrics for exp in self.experiments ):
            print("No Metric Name found")
        else:
            best_experiment = max(
            self.experiments,
            key=lambda exp: exp.model_metrics.get(in_metric, 0)
        )
            print(f"Best model for {in_metric} is: {best_experiment.model_name}")
            print(f"{in_metric} score: {best_experiment.model_metrics[in_metric]}")
            print(best_experiment)

    def save_to_file(self):
        path = "C:\\Users\\debli\\python_practice\\TargetData\\"
        file_name = "ML_Experiment_Logger"
        experiment_dict = [asdict(exp) for exp in self.experiments]
        with open (f"{path}{file_name}.json",'w') as f:
                json.dump(experiment_dict,f,indent=4, default=str)


    def load_from_file(self):
        path = "C:\\Users\\debli\\python_practice\\TargetData\\"
        file_name = "ML_Experiment_Logger"
        data_list = []
        with open(f"{path}{file_name}.json", 'r') as ip_file:
            reader = json.load(ip_file)
            for row in reader:
                data_obj = Experiment(**row)
                data_list.append(data_obj)
        return data_list