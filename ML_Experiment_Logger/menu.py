import sys
from datetime import datetime

from experiment import Experiment
from  ExperimentLogger import ExperimentLogger as EL

def take_user_choice():
    user_choice = input("\n\nDo you want to go back to the main menu? Press Y for yes : ")
    if user_choice not in ('Y', 'y'):
        print("Thank You for using our experiment logger. \n\n")
        sys.exit(0)

def main():
    # trial = Experiment(id = "EXP 1",
    #                    model_name="Test Model",
    #                    model_parameters={"max_depth": 5,
    #                                      "learning_rate": 0.01,
    #                                      "n_estimators": 100},
    #                    model_metrics={"accuracy": 0.95,
    #                                   "precision": 0.89,
    #                                   "recall": 0.91,
    #                                   "f1_score": 0.90},
    #                    experiment_date="03/01/2026",
    #                    notes="testing my program")
    #

    EL_OBJ = EL()
    # EL_OBJ.add_new_experiment(trial)
    # EL_OBJ.add_new_experiment(trial1)
    # EL_OBJ.add_new_experiment(trial2)
    # EL_OBJ.view_all_experiments()
    # EL_OBJ.filter_by_model("Test Model2")
    # EL_OBJ.filter_by_model("Test Model3")
    # EL_OBJ.compare_experiment_outputs("EXP 2","EXP 3")
    # EL_OBJ.view_best_model("accuracy")
    # EL_OBJ.save_to_file()
    # EL_OBJ.load_from_file()
    while True:
        print("==============================")
        print("     Experiment Logger Menu     ")
        print("==============================")
        try:
            user_input = int(input("\n Please enter your choice from the below menu:\n"
                                       "Enter 1 if you want to Add a new experiment to the system\n"
                               "Enter 2 if you want to view all experiments\n"
                               "Enter 3 if you want view results by a specific Model\n"
                               "Enter 4 if you want to compare two experiment data\n"
                               "Enter 5 if you want to view view the best model result\n"
                               "Enter 6 if you want to save your experiment data to a file\n"
                               "Enter 7 if you want to load your experiment data from the saved file\n"
                               "Enter 8 if you want to Exit\n"))

            if user_input == 8:
                print("Thank You For using our experiment logger")
                break
            elif user_input == 1:
                while True:
                    model_name_ip = input("\nPlease enter your experiment model name : ")

                    print("Lets now enter model parameter values")
                    model_parameters_ip ={}
                    while True:
                        key_param = input ("Enter parameter name (or 'done' to finish): ")
                        if key_param == 'done':
                            break
                        while True:
                            try:
                                value = float(input(f"Enter value for {key_param}: "))
                                model_parameters_ip[key_param] = value
                                break
                            except ValueError:
                                print("Please enter a number.")

                    print("Lets now enter model metric values")
                    model_metric_ip = {}
                    while True:
                        key_metric = input("Enter metric name (or 'done' to finish): ")
                        if key_metric == 'done':
                            break
                        while True:
                            try:
                                value = float(input(f"Enter value for {key_metric}: "))
                                model_metric_ip[key_metric] = value
                                break
                            except ValueError:
                                print("Please enter a number.")
                    while True:
                        try:
                            experiment_date_ip = input("\n Please enter your experiment date : ")
                            date_obj = datetime.strptime(experiment_date_ip, '%m/%d/%Y')
                            break
                        except ValueError:
                            print("Invalid date. Please use MM/DD/YYYY format.")

                    notes_ip = input("\nPlease enter if you want to add any specific notes for this experiment : ")

                    exp_obj = Experiment(model_name=model_name_ip,
                                         model_parameters=model_parameters_ip,
                                         model_metrics=model_metric_ip,
                                         experiment_date=date_obj,
                                         notes=notes_ip
                                         )
                    EL_OBJ.add_new_experiment(exp_obj)
                    print ("Your experiment details were successfully added")
                    take_user_choice()
            elif user_input == 2:
                EL_OBJ.view_all_experiments()
                take_user_choice()
            elif user_input == 3:
                ip_model_name = input("Enter the model name you want to filter by: ")
                EL_OBJ.filter_by_model(ip_model_name)
                take_user_choice()
            elif user_input == 4:
                print("We will be comparing 2 Experiments data")
                EL_OBJ.view_all_experiments()
                ip_model_name_1 = input("Enter the first experiment id : ")
                ip_model_name_2 = input("Enter the second experiment id : ")
                EL_OBJ.compare_experiment_outputs(ip_model_name_1,ip_model_name_2)
                take_user_choice()
            elif user_input == 5:
                category_ip = input("Enter the model metric based on which you want to see the output: ")
                EL_OBJ.view_best_model(category_ip)
                take_user_choice()
            elif user_input == 6:
                EL_OBJ.save_to_file()
                take_user_choice()
            elif user_input == 7:
                EL_OBJ.load_from_file()
                take_user_choice()
        except ValueError:
            print("Please enter a number between 1 and 9.")
            continue







if __name__ == "__main__":
    main()