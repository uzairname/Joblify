## Inspiration
One of the most popular goals of college students is to land internships, jobs, fellowships, co-ops, and other valued work experiences during their college years. **Resumes** are definitely one of the greatest determining factors for a candidate during this experience. But the greatest rival standing between students and employers is the grueling **Applicant Tracking System (ATS)**. Most of these are quite primitive, and redundant, and don't do justice matching a candidate's skills, profiles, and interests with the job description provided by the recruiter. Rather they are infamous for dwindling down the applicant pool to certainly smaller numbers based on trivial formatting issues/preferences. 
This system does not give a holistic criteria-based experience for filtering candidates at different stages. 
Moreover, several small-scale recruiters at times lose the opportunity to meet the "right" person for the role due to such **ATS biases**.  

As college students ourselves, we've faced similar struggles during our job/internship research and have yearned for a more sophisticated and acceptable model for the application process as well as networking. Although there are a few other application platforms like Handshake available to students Driven to resolve this persistent problem, we decided to envision and create a new recruitment-networking application system that scores a candidate's resume with regards to a particular job description and displays a list of candidates in decreasing precedence of the evaluated resume scores.

## What does it do?
We developed Joblify (Your Career Companion), a custom Natural Language Processing solution for resumes, taking advantage of the resources and datasets available to us. We used a semantic search pipeline from the spaCy library and specified a pattern using an existing job skill dataset by Microsoft ([link](https://github.com/microsoft/SkillsExtractorCognitiveSearch/tree/master/data)) to specialize it to select job-related entities, such as fields of expertise, soft skills, and programming languages. 


## Target Audiences
Our web application aims to serve two different sections of people with different kinds of specifically designed user interfaces: employers looking to hire candidates on one hand and college students seeking jobs, and internships, on the other. 


## How we built it
We 


## Challenges we ran into
1)  Extracting entities from text tailored to job postings was a difficult task. We started with a generalized named entity recognition model from the Cohere API, but it struggled to extract relevant information. We ended up using a semantic search pipeline from the spaCy library and used a dataset by Microsoft to specialize it to select job skill-related entities, such as fields, soft skills, and programming languages.

2)  Alignment of elements on pages

3)  Developing common coding styles.




## Accomplishments that we're proud of
 UI design



## What we learned



## What's next for Joblify - Your Career Companion
One of the constraints of the 24-hour hackathon is having a rough prototype of the ML model without access to much **user feedback** to help us improve it. If we were given the time to do further research and development, using a **semantic search algorithm fine-tuned on training data** offered by **real-time users** of the site would help us greatly improve the strength and accuracy of the job and employee matching functionality. This would be our immediate next step in the growth and development of Joblify. 
