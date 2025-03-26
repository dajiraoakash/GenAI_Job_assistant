class Job:
    def __init__(self, title, company, location, description):
        self.title = title
        self.company = company
        self.location = location
        self.description = description

class Resume:
    def __init__(self, name, contact_info, skills, experience):
        self.name = name
        self.contact_info = contact_info
        self.skills = skills
        self.experience = experience

class Agent:
    def __init__(self, agent_type, behavior):
        self.agent_type = agent_type
        self.behavior = behavior

class Task:
    def __init__(self, task_type, requirements):
        self.task_type = task_type
        self.requirements = requirements

# Add any additional ORM models as needed for your application.