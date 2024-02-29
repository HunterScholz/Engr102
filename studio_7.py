import csv


class Participant:
    def __init__(self, age, industry, salary, currency, country, experience, education):
        # self.x = x
        self.age = age
        self.industry = industry
        self.salary = salary
        self.currency = currency
        self.country = country
        self.experience = experience
        self.education = education

class AverageSalary:
    def __init__(self, key, average, participant_count):
        self.key = key
        self.average = average
        self.participant_count = participant_count

def main():

    rows = load_csv_file("survey.csv")
    participants = create_participants(rows)

    print("Answer #1:", len(participants))

    industry_groups = group_by_attribute(participants, "industry")

    average_salaries_by_industry = get_average_salary(industry_groups)

    filtered_average_salaries_by_industry = []
    for group in average_salaries_by_industry:
        if group.participant_count >= 10: 
            filtered_average_salaries_by_industry.append(group)

    sorted_filtered_average_salary_by_industry = sorted(filtered_average_salaries_by_industry, key = lambda x: x.average, reverse=True)
    
    top_5_industries = []

    for entry in sorted_filtered_average_salary_by_industry[:5]:
        top_5_industries.append(entry.key)
    print("Answer #2:", top_5_industries)
    
    # TODO: print top 5 industries by salary. Only include industries with at least 10 participants

    # TODO: Use existing logic to solve questions 3,4,5

    #3
    age_groups = group_by_attribute(participants, "age")
    average_salaries_by_industry = get_average_salary(age_groups)

    for group in average_salaries_by_industry:
        print("Answer #3:", group.key, group.average)

    #4
    education_groups = group_by_attribute(participants, "education")
    average_salaries_by_industry = get_average_salary(education_groups)

    for group in average_salaries_by_industry:
        print("Answer #4:", group.key, group.average)

    #5
    experience_groups = group_by_attribute(participants, "experience")
    average_salaries_by_industry = get_average_salary(experience_groups)

    for group in average_salaries_by_industry:
        print("Answer #5:", group.key, group.average)

    return


def get_average_salary(groups_list):
    '''
        get the average salary from a groupped list

        params:
            groups_list: dict<String, List<Participant>>

        return:
            List<tuple<Str, int, int> - Returns a list of tuples which include the key as a string, the average as an int, and the amount of participants as an int.
            TODO: rather than returning a tuple, create an AverageSalary object, and process the information that way.
    
    '''
    average_salaries = []
    for key, group in groups_list.items():
        avg = int(sum([x.salary for x in group]) / len(group))
        # TODO: With the AverageSalaries class we created, append in instance of AverageSalaries instead of just key, avg, len(group)
        average_salaries.append(AverageSalary(key, avg, len(group)))

    return average_salaries

def group_by_attribute(objects, property):
    '''
        params:
            objects: List<Participant> - a list of the participant objects
            propery: Str - whichever object property we want to group by
        return:
            dict<String, List<Participant>> - a dictionary, using the value of the property as the key, and the list of participants which include that value as the value.

    '''

    # The logic for groupping has been simplified greatly for both faster execution and easier understanding
    
    groups = {}
    
    # create a dictionary using the property
    for obj in objects:
        value = getattr(obj, property)
        if value in groups:
            groups[value].append(obj)
        else:
            groups[value] = [obj]

    return groups




def create_participants(rows):
    '''
    parse the rows, extracting the required content for the data analysis

    params:
        rows: Lists<List<Str>> - Each entry is a list of strings, the entries are contained in a larger list.

    return:
        List<Participant> - Returns a list of Participant objects
    '''
    # Age, Industry, Salary, Currency, Country, Years of Experience Overall, Highest level of Education

    participants = []

    for row in rows[1:]:
        age = row[1]
        industry = row[2]
        salary = int(row[5].replace(",",""))
        currency = row[7]
        country = row[10]
        experience = row[13]
        education = row[15]
        # only add if currency == 'USD'
        if currency == "USD":
            participants.append(Participant(age, industry, salary, currency, country, experience, education))

    return participants



def load_csv_file(filename):
    '''
    loads contents of a csv file and returns the contents as a list of the row, each row representing an entry.

    params: 
        filename: Str - filename with path to the csv file which will be read

    returns:
        rows: List<List<Str>> - A list of the rows, each row is a list of strings from the csv file
    '''
    rows = []
    with open(filename, "r", encoding='iso-8859-1') as f:
        reader_obj = csv.reader(f)

        for row in reader_obj:
            rows.append(row)

    return rows

if __name__ == "__main__":
    main()