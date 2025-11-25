# Clubs 
from pyscript import display, document

communication_arts = {
    "Name": "✍️ Communication Arts Club",
    "Description": "Improve writing, speaking, and multimedia skills.",
    "Meeting": "Wednesday 4:00–5:30 PM",
    "Location": "MMHALL",
    "Advisor": "Mr. Loreto",
    "Members": 20,
    "Category": "Arts",
}

science_club = {
    "Name": "♟️ Science Club",
    "Description": "Conduct experiments, explore scientific phenomena, and join science fairs.",
    "Meeting": "Thursday 3:30–4:00 PM",
    "Location": "Science Lab",
    "Advisor": "Mr. Calpo",
    "Members": 18,
    "Category": "STEM",
}

volleyball_varsity = {
    "Name": "🏅 Volleyball Varsity",
    "Description": "Train, practice, and compete in interschool volleyball tournaments.",
    "Meeting": "Tuesday 3:00–5:00 PM",
    "Location": "Quadrangle",
    "Advisor": "Coach Gervacio",
    "Members": 15,
    "Category": "Sports",
}

def show_CommunicationArts(e):
    document.getElementById('club-name').innerHTML = ""
    document.getElementById('club-description').innerHTML = ""
    document.getElementById('club-meeting').innerHTML = ""
    document.getElementById('club-location').innerHTML = ""
    document.getElementById('club-advisor').innerHTML = ""
    document.getElementById('club-members').innerHTML = ""
    document.getElementById('club-category').innerHTML = ""

    display(communication_arts["Name"], target="club-name")
    document.getElementById("club-description").innerHTML = f"<strong>Description: </strong> {communication_arts['Description']}"
    document.getElementById("club-meeting").innerHTML = f"<strong>Meeting Time:</strong> {communication_arts['Meeting']}"
    document.getElementById("club-location").innerHTML = f"<strong>Location:</strong> {communication_arts['Location']}"
    document.getElementById("club-advisor").innerHTML = f"<strong>Advisor:</strong> {communication_arts['Advisor']}"
    document.getElementById("club-members").innerHTML = f"<strong>No. of Members:</strong> {communication_arts['Members']}"
    document.getElementById("club-category").innerHTML = f"<strong>Category:</strong> {communication_arts['Category']}"

def show_ScienceClub(e):
    document.getElementById('club-name').innerHTML = ""
    document.getElementById('club-description').innerHTML = ""
    document.getElementById('club-meeting').innerHTML = ""
    document.getElementById('club-location').innerHTML = ""
    document.getElementById('club-advisor').innerHTML = ""
    document.getElementById('club-members').innerHTML = ""
    document.getElementById('club-category').innerHTML = ""

    display(science_club["Name"], target="club-name")
    document.getElementById("club-description").innerHTML = f"<strong>Description: </strong> {science_club['Description']}"
    document.getElementById("club-meeting").innerHTML = f"<strong>Meeting Time:</strong> {science_club['Meeting']}"
    document.getElementById("club-location").innerHTML = f"<strong>Location:</strong> {science_club['Location']}"
    document.getElementById("club-advisor").innerHTML = f"<strong>Advisor:</strong> {science_club['Advisor']}"
    document.getElementById("club-members").innerHTML = f"<strong>No. of Members:</strong> {science_club['Members']}"
    document.getElementById("club-category").innerHTML = f"<strong>Category:</strong> {science_club['Category']}"

def show_VolleyballVarsity(e):
    document.getElementById('club-name').innerHTML = ""
    document.getElementById('club-description').innerHTML = ""
    document.getElementById('club-meeting').innerHTML = ""
    document.getElementById('club-location').innerHTML = ""
    document.getElementById('club-advisor').innerHTML = ""
    document.getElementById('club-members').innerHTML = ""
    document.getElementById('club-category').innerHTML = ""

    display(volleyball_varsity["Name"], target="club-name")
    document.getElementById("club-description").innerHTML = f"<strong>Description: </strong> {volleyball_varsity['Description']}"
    document.getElementById("club-meeting").innerHTML = f"<strong>Meeting Time:</strong> {volleyball_varsity['Meeting']}"
    document.getElementById("club-location").innerHTML = f"<strong>Location:</strong> {volleyball_varsity['Location']}"
    document.getElementById("club-advisor").innerHTML = f"<strong>Advisor:</strong> {volleyball_varsity['Advisor']}"
    document.getElementById("club-members").innerHTML = f"<strong>No. of Members:</strong> {volleyball_varsity['Members']}"
    document.getElementById("club-category").innerHTML = f"<strong>Category:</strong> {volleyball_varsity['Category']}"
