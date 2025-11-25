# Home
from pyscript import display

AboutOurSchool = {
    "Title": "About Our School",
    "Description": "Silver Academy of Silveridia is dedicated to nurturing excellence in academics, arts, and sports. Our mission is to provide a safe and inspiring environment where students can achieve their full potential and develop lifelong skills.",
}

AcademicPrograms = {
    "Title": "Academic Programs",
    "Description": "We offer a well-rounded curriculum including Science, Mathematics, English, Filipino, ICT, and Physical Education. Our experienced teachers use innovative teaching methods to ensure every student succeeds.",
}

ExploreClubs = {
    "Title": "Clubs & Activities",
    "Description": "Students can join various clubs and organizations to explore their interests: from Robotics and Varsity teams to Arts and Communication Clubs. We believe in learning beyond the classroom.",
}

GradeCalculator = {
    "Title": "Grade Calculator",
    "Description": "Can’t wait to see your report card and find out how you really did this quarter? Use this calculator to estimate your grades early and get a clear picture of your performance!",
}

display(AboutOurSchool["Title"], target="AOS-Title")
display(AboutOurSchool["Description"], target="AOS-Desc")

display(AcademicPrograms["Title"], target="AP-Title")
display(AcademicPrograms["Description"], target="AP-Desc")

display(ExploreClubs["Title"], target="CA-Title")
display(ExploreClubs["Description"], target="CA-Desc")

display(GradeCalculator["Title"], target="GC-Title")
display(GradeCalculator["Description"], target="GC-Desc")