# Identifying and Reporting Cryptocurrrency Scams on Youtube

In this project, we analyze how bots are used to comment on crypto-related videos. We intend to create such a system that given any particular video looks at the comments and then uses sentimental analysis to classify the comments into potential scams. The program them follows the recommendations of the next videos and conducts the same experiment. We want to be able to identify these potential scams and then look into the extent in which these scams go into. In extension I want to build an identifier that reports these comments as "Unwanted commercial content or spam" on Youtube. Once reported, the team at YouTube will be able to successfully identify these scams and poitentially flag the account and stop the spread of these scams.

#### Social Significance
This is the age of the internet. With the recent trend in cryptocurrency there is a huge number of people going online to learn about the activity to potentially invest in such a way that they could maximise their profits. As bitcoin reaches a greater value, *every one in ten people [1]* are investing into crypto currency to cash in on this trend. Using tools like robinhood and coinbase *"cryptocurrencies have become far more accessible for the average American" [2]* and people who are not well-versed with technology have been learning to invest in it. According to a recent study over *'half of YouTube viewers use it to learn how to do things they’ve never done'[3]* and this includes learning crypto. With a larger traffic, youtube becomes a huge platform for scammers to advertise and potentially rob the general population of their earnings. Conducting this study has a huge social impact as it will help in create such a platform where the population can safely learn without being under the threat of being scammed. 

#### Other Application
Given the large usage of YouTube and the high traffic volumes that it experiences, although this project only focuses on a very specific topic- identifying cryptocurreny scams on YouTube it has a large application. If successful, this could be used to identify scams on other platforms including Twitter and Facebook. As an extension this could also be used to flag videos that contain malicious data that scams the users.

## Background
People have been using YouTube to learn multiple skills and with the rise in the popularity of Bitcoin, people are using YouTube to learn Cryptocurrency. As the number of viewers increase, this becomes an attractive platform for scammers to scam people into forwarding them bitcoins with a promise of a reward. This project in collaboration with professors **Gianluca Stringhini** and **Osama Alshaykh** aims at exposing these fradulent videos.  YouTube viewers *"had lost **$24 million** in bitcoin and related scams in the first six months of 2020" [4]* and therefore it is an important area that needs to be rectified.

## Literature Review


There has been research done on scams related to social engineering where users lose money because scammer promises to send them gifts in exchange, recieve benefits or just acts needy. These scammers not only recieve money but may convince the users to send them their private information as well. This topic has been heavily researched in context of email scams and phishing emails where the attackers aims to gain access to confidential information of the user. The paper **Scam Detection Assistant: Automated
Protection from Scammers** [5] takes this a step further by proposing a better approach that actually analyzes the whole text to classify it as a scam rather than "analyzing non content meta-data"[5] which is inefficient. To check emails that required users to perform a task, they esentially characterized the data into a verb-object pair that was then used to compare if the commands were forbidden. While this paper focuses on command identification, I do not believe that this needs to be done in our case. We however are interested in *Sentence Type Identification* for which this paper provides a basis. This paper only uses the idea for the purpose of identifying fradulent emails, we will be using this method to identify fradulent comments within YouTube.

The paper **Bringing the Kid back into YouTube Kids: Detecting Inappropriate Content**[6] provides a deep analysis of how data can be collected to ensure that we recieve enough dataset to apply our training and testing methods on them. Essentially the paper talks about how data from legitimate channels is added to a pool and then compared with videos that contain inappropriate content for the kids. The labels and links for such inappropriately tagged videos can be downloaded from different sources including reddit which contains a huge dataset. This particular approach interests me as manually identifying every comment becomes tedious and therefore searching for any preset datasets that actually contain these labeled phrases or comments that have a high frequency to be used in potential scams is necessary.

After reading a few papers, I came across various **databases** that contain previously found scam emails. These emails are particularly important as they contain important information regarding societal clues that the attackers leverage to gain access to private information of the users. These are large resources of data that contain email scams from multiple areas and will provide a basis for sentimental analysis and classification as these are the potential sentences that our data should be looking for. This data will already be labeled and can therefore be used for both supervised and unsupervised learning models to identify these scams on untested dataset/ other videos that are posted in the future. [7][8][9]

One of the most important papers that I came across that may help in this process is **“You Know What to Do”: Proactive Detection of YouTube Videos Targeted by Coordinated Hate Attacks"** [10] that aims to provide a solution to the expression of hate speech online. YouTube is a platform that, while allowing for the freedom of speech, takes the idea of creating a space safe for users very very seriously. However, given the large number of videos being uploaded every day on YouTube, they require the input of users to "police" the videos and comments therefore, creating a safer space. By defination, this approach- called reactive- is slow. The paper proposes a proactive approach that immediately flags videos that can be a target of hate speech for users and then provides a stringent approach as to how video platforms can  use the same methodology on their platform. This approach will help me expand the detection for possible scams to include YouTube ads and content within YouTube videos that are susceptible to these scams.


## Open Source
As an extension of the literature review, we decided to further research on Selenium webdriver that is the most important tool required to automatically conduct tests on YouTube, go to that particular video, search for the comments and save them.

*Github repo:* https://github.com/SeleniumHQ/selenium

*Contributors:* 579

*License:* Apache 2.0-license

*Users:* Over 113000

Selenium is a tool that can be used in multiple languages including Java, C++ and python which enables a user to actually replicate their steps to carry out experiments. This enables researchers to carry out mundane tasks to measure the different requirements without having a person carry out these tasks. I will be using Selenium to connect to YouTube, search for a particular video, go through the comments and save all the comments. In extension, after analysis, it will be used to check if a comment is a scam and Selenium will help flag that particular video and then report to YouTube which can then further review the comment.

## Replication
I have been working on a a script that helps evade YouTube security- since it kept blocking selenium because the algorithm already recognizes the headers in selenium. The idea was to evade this security feature so that I am safely able to open YouTube and search for a particular video, as I state it within my code. I am currently researching on different ways to change this method.

## References
[1] https://www.cnbc.com/2021/08/24/1-in-10-people-invest-in-cryptocurrencies-many-for-ease-of-trading.html

[2] https://www.fool.com/the-ascent/cryptocurrency/best-cryptocurrency-apps/

[3] https://www.theverge.com/2018/11/7/18071992/youtube-pew-study-education-news-childrens-videos

[4] https://www.cbsnews.com/news/youtube-twitter-bitcoin-scam-problems-alleged/

[5] https://par.nsf.gov/servlets/purl/10167943

[7] http://www.scamwarners.com

[8] http://antifraudintl.com

[9] http://www.scamdex.com

[10] https://seclab.bu.edu/people/gianluca/papers/youtube-CSCW2019.pdf
