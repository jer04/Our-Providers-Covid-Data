# Flow:
#   Question #1:
#   1. Find all providers via provider number
#   2. Find their states
#   3. Group all of the providers that are in the same states
#   4. Find all percentages of healthcare personnel with a completed vaccination
#   5. Find the average of all of those percentages
#   6. If the average > 80%, then add that week(week_ending) into the list
#   Column: percentage_of_current_healthcare_personnel_who_received_a_completed_covid_19_vaccination_at_any_time
#
#   Question #2:
#   1. For each Provider, check if the [residents_weekly_confirmed_covid_19] = 0 for each week
#   2. For each Provider, find the longest streak of weeks where [residents_weekly_confirmed_covid_19] = 0

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
