Why I Did This
I wanted to better understand how customers describe their experiences with banks in Germany not from  marketing material, but from publicly available customer feedback online.
For this small exploratory project, I selected Deutsche Bank, Commerzbank and N26 because together they  represent different banking models: established traditional banks and a digital-first bank. I was curious whether  these structural differences appear in customer reviews and how customers describe their experiences with  service, digital platforms and trust.
The AI for Business course I completed at the University of Pennsylvania emphasized that unstructured data  such as customer reviews can contain valuable business insights if analyzed systematically. This project was my  attempt to apply that concept on a small scale using real customer feedback.
What I Did
Data Collection
I collected 45 publicly available customer reviews (15 per bank) from three platforms:
 • Trustpilot
 • Google Reviews
 • Trusted.de
The sample included a mix of positive and negative reviews in order to reflect a realistic range of customer  experiences. Each review was read completely before categorization rather than relying only on star ratings. Because the project was conducted manually, the dataset was intentionally kept small to allow careful reading  and classification of each review.
How I Categorized the Reviews
Each review was assigned:
 • one overall sentiment (positive or negative)
 • one primary topic category
The categorization was performed manually. While this process required significant time for a relatively small  dataset, it helped illustrate why automated text analysis tools are widely used in practice. A large financial  institution receives thousands of reviews across multiple platforms every week.The categories used were:
Customer Service
Comments regarding staff interaction, hotline experience, response times, and problem resolution.
Digital Banking & App
User experiences with mobile banking apps, login systems, online banking interfaces, and usability.
Trust & Security
Mentions of fraud cases, account freezes, data protection concerns, or transparency in banking processes.
Suggestions / Improvements
Requests for additional features, product improvements, or service changes.
Each review was assigned the category that represented its main topic.
What I Found Overall Numbers
   
Bank
Deutsche Bank Commerzbank
N26
Total Reviews Negative Positive Negative %
15 12 3
15 13 2
15 9 6
The following chart illustrates the share of negative reviews within the analyzed sample.
Figure 1: Share of negative customer reviews in the analyzed sample dataset. Generated using Python 
(Pandas, Matplotlib).
Because the sample size is relatively small, these numbers should not be interpreted as a full representation of  each bank’s overall reputation. Instead, they illustrate patterns that appeared within this specific dataset.Categories per Bank
  
 
  Bank Customer Service Digital Banking & App Trust & Security Suggestions
Deutsche Bank     9   4    2 0 
Commerzbank    11    3 0 0 
N26     4    4 5 1 
Observations from the Reviews
Several patterns appeared during the review analysis.
For Deutsche Bank and Commerzbank, customer service experiences were mentioned most frequently. Many  reviews described long waiting times on hotlines, difficulties reaching support staff, or complex administrative  processes. At the same time, some customers highlighted positive interactions with individual advisors,  indicating that service quality can vary significantly depending on the situation.
Another recurring theme concerned digital banking platforms. Some customers reported confusion with online  banking interfaces or difficulties with login systems. This suggests that digital usability remains an important  area for continued improvement in traditional banking environments.
For N26, the reviews often mentioned the simplicity of account setup and the intuitive design of the mobile  banking app. Customers frequently described the onboarding process as fast and user-friendly. However, some  reviews also raised concerns related to account restrictions or payment delays, which customers sometimes  perceived as lacking transparency.
Interpretation
Digital Experience in Traditional Banks
Customer reviews for Deutsche Bank and Commerzbank often discussed challenges related to service  accessibility and digital platforms. Many customers described long response times or complex support  processes. These observations suggest that improving service responsiveness and digital usability could further  strengthen the overall customer experience.
At the same time, some customers reported positive experiences with individual advisors, which highlights the  continued importance of human interaction and relationship-based banking.
Trust and Transparency in Digital Banking
The feedback related to N26 showed a somewhat different pattern. Many customers appreciated the speed and  simplicity of the digital platform. However, some reviews described account restrictions or payment issues that  were perceived as unclear or insufficiently explained.
This suggests that while digital-first banking models can offer strong usability advantages, maintaining  transparency and customer trust during problem resolution is equally important.
Why AI Tools Matter Here
Conducting this analysis manually required several hours to read and categorize all 45 reviews. A large bank  receives thousands of reviews every week across multiple platforms and languages.
As a next step, I also wrote a small Python script using Pandas and Matplotlib to automate the counting and  visualization of the categorized review data producing the charts included in this project.This is where AI-based text analysis tools become valuable. Automated sentiment analysis and topic  classification can transform unstructured customer feedback into structured data that management teams can  monitor in real time.
For example, a bank could automatically identify recurring complaints related to login problems, payment  delays, or hotline waiting times and address them earlier.
This type of application reflects a practical use case of the concepts covered in the AI for Business course,  where natural language processing can support decision-making by summarizing large amounts of textual  feedback.
Conclusion
This exploratory analysis of 45 customer reviews illustrates how publicly available feedback can reveal patterns  in customer experience across different banking models.
The results suggest that traditional banks may face ongoing challenges related to service accessibility and digital  platform usability, while digital banks may need to focus particularly on transparency and trust when  operational issues occur.
While the dataset used in this project is relatively small, the exercise demonstrates how structured analysis of  unstructured data can provide useful insights.
For me personally, the project also showed that working with real textual data requires careful interpretation and  consistent categorization. This process reflects the broader challenge that organizations face when attempting to  turn large volumes of unstructured information into actionable insights.
Developing technical and analytical skills to perform this type of analysis more efficiently is exactly what I hope  to learn in greater depth during a dual study program in Wirtschaftsinformatik.
