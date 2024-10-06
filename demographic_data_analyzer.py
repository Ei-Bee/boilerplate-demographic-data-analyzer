import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('/workspace/boilerplate-demographic-data-analyzer/adult.data.csv')

    # 1. How many of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # 3. What is the percentage of people who have a Bachelor's degree?
    total_people = df.shape[0]
    percentage_bachelors = (df[df['education'] == 'Bachelors'].shape[0] / total_people) * 100

    # 4. What percentage of people with advanced education make more than 50K?
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_rich = (higher_education[higher_education['salary'] == '>50K'].shape[0] / higher_education.shape[0]) * 100 if higher_education.shape[0] > 0 else 0

    # 5. What percentage of people without advanced education make more than 50K?
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education_rich = (lower_education[lower_education['salary'] == '>50K'].shape[0] / lower_education.shape[0]) * 100 if lower_education.shape[0] > 0 else 0

    # 6. What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # 7. What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = (num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100 if num_min_workers.shape[0] > 0 else 0

    # 8. What country has the highest percentage of people that earn >50K?
    country_counts = df['native-country'].value_counts()
    high_earners_by_country = df[df['salary'] == '>50K']['native-country'].value_counts()
    highest_earning_country_percentage = (high_earners_by_country / country_counts) * 100
    highest_earning_country = highest_earning_country_percentage.idxmax()
    highest_earning_country_percentage = highest_earning_country_percentage.max()

    # 9. Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    # Round results to the nearest tenth
    average_age_men = round(average_age_men, 1)
    percentage_bachelors = round(percentage_bachelors, 1)
    higher_education_rich = round(higher_education_rich, 1)
    lower_education_rich = round(lower_education_rich, 1)
    min_work_hours = round(min_work_hours, 1)
    rich_percentage = round(rich_percentage, 1)
    highest_earning_country_percentage = round(highest_earning_country_percentage, 1)

    # DO NOT MODIFY BELOW THIS LINE
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
