About This Project
I wanted to better understand how customers describe their experiences with banks in Germany, not from marketing material, but from publicly available customer feedback online.
The AI for Business course I completed at the University of Pennsylvania emphasized that unstructured data such as customer reviews can contain valuable business insights if analyzed systematically. This project was directly inspired by that course — a first practical attempt to apply what I learned using real-world data from the German banking sector.
I selected Deutsche Bank, Commerzbank and N26 because together they represent different banking models: established traditional banks and a digital-first bank. I was curious whether these structural differences actually show up in what customers write online — and how they describe their experiences with service, digital platforms and trust.

What I Did
Data Collection
I collected 45 publicly available customer reviews (15 per bank) from three platforms:

Trustpilot
Google Reviews
Trusted.de

Each review was read completely before categorization — not just the star rating. The dataset was intentionally kept small to allow careful reading and classification of each review.
Categorization
Each review was assigned one sentiment and one topic category, performed manually:
CategoryDescriptionCustomer ServiceStaff interaction, hotline experience, response times, problem resolutionDigital Banking & AppMobile apps, login systems, online banking interfaces, usabilityTrust & SecurityFraud cases, account freezes, data protection, transparencySuggestionsFeature requests, product improvements, service changes
Doing this manually for 45 reviews took several hours — which directly illustrated why automated text analysis tools exist. A large bank receives thousands of reviews every week across multiple platforms and languages.
Python Analysis
After completing the manual categorization, I wrote a Python script using Pandas and Matplotlib to automate the counting and visualization of the data. This produced the charts included in this project and connected the manual analysis work to a practical technical implementation.

Results
Overall Sentiment
BankTotal ReviewsNegativePositiveNegative %Deutsche Bank1512380%Commerzbank1513287%N26159660%

The sample size is small. These numbers illustrate patterns within this specific dataset — not a full statistical representation of each bank's overall reputation.

Categories per Bank
BankCustomer ServiceDigital Banking & AppTrust & SecuritySuggestionsDeutsche Bank9420Commerzbank11300N264451

Key Observations
Deutsche Bank & Commerzbank — Customer service dominated the reviews. Long hotline waiting times, difficulties reaching support staff, and complex administrative processes appeared repeatedly. Some customers highlighted positive experiences with individual advisors — showing that service quality varies significantly by situation, and that human interaction still matters.
Digital banking platforms — Several customers described confusion with online banking interfaces or login difficulties at traditional banks. Digital usability remains an important area for improvement.
N26 — Reviews frequently praised the simplicity of account setup and the intuitive app design. However, a pattern also emerged around account restrictions and payment delays that customers perceived as lacking transparency. Being digital-first does not automatically mean being trustworthy — and this was one of the more interesting findings of the project.

Interpretation
Why AI Tools Matter Here
This manual process with 45 reviews illustrates the core concept from the AI for Business course: automated sentiment analysis and topic classification can transform unstructured customer feedback into structured, actionable data — at a scale no manual process can match.
A bank could use these tools to automatically identify recurring complaints about login problems, payment delays, or hotline waiting times — in real time, across thousands of reviews per week. That is a direct, low-risk application of AI in a business context.
Connection to Course Concepts
AI for Business TopicApplication in This ProjectUnstructured DataCustomer reviews as raw, unstructured input requiring structureText ClassificationManual categorization simulating what NLP models automateAI in Financial ServicesApplied directly to real German banks and service gapsAI StrategyIdentified a concrete AI use case: real-time review monitoringGovernance & EthicsConsidered GDPR implications of processing customer data at scale

Conclusion
This exploratory analysis shows how publicly available feedback can reveal patterns in customer experience across different banking models. Traditional banks face ongoing challenges in service accessibility and digital usability. Digital banks need to focus on transparency and trust when things go wrong — not just on smooth onboarding.
For me personally, working with real textual data showed that careful interpretation and consistent categorization are as important as the technical tools themselves. The gap between raw data and useful insight is not automatic — it requires decisions at every step.
Developing technical and analytical skills to perform this type of analysis more efficiently is exactly what I hope to learn in a dual study program in Wirtschaftsinformatik — where business understanding and technical implementation come together. This project was a first practical step in that direction, inspired by an AI for Business course and built on real-world data from the German banking sector.

Project Files
banking_reviews.csv: Dataset — 45 reviews across 3 banks and 3 platforms
analyze_reviews.pyPython: script — data analysis and chart generation
banking_analysis.ipynb: Jupyter Notebook — full step-by-step walkthrough
chart1_sentiment_by_bank.png: Sentiment comparison by bank
chart2_categories_by_bank.png: Review categories by bank
chart3_negative_comparison.pngNegative: reviews comparison

Tools Used

Python — data analysis and visualization
Pandas — data loading, grouping and counting
Matplotlib — chart generation
Data sources — Trustpilot, Google Reviews, Trusted.de


Inspired by the AI for Business course, University of Pennsylvania · 2026
