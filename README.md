# Identifying and Reporting Cryptocurrrency Scams on Youtube

In this project, we analyze how bots are used to comment on crypto-related videos. We intend to create such a system that given any particular video looks at the comments and then uses sentimental analysis to classify the comments into potential scams. The program them follows the recommendations of the next videos and conducts the same experiment. We want to be able to identify these potential scams and then look into the extent in which these scams go into. In extension I want to build an identifier that reports these comments as "Unwanted commercial content or spam" on Youtube. Once reported, the team at YouTube will be able to successfully identify these scams and poitentially flag the account and stop the spread of these scams.

### Social Significance
This is the age of the internet. With the recent trend in cryptocurrency there is a huge number of people going online to learn about the activity to potentially invest in such a way that they could maximise their profits. As bitcoin reaches a greater value, *every one in ten people [1]* are investing into crypto currency to cash in on this trend. Using tools like robinhood and coinbase *"cryptocurrencies have become far more accessible for the average American" [2]* and people who are not well-versed with technology have been learning to invest in it. According to a recent study over *'half of YouTube viewers use it to learn how to do things they’ve never done'[3]* and this includes learning crypto. With a larger traffic, youtube becomes a huge platform for scammers to advertise and potentially rob the general population of their earnings. Conducting this study has a huge social impact as it will help in create such a platform where the population can safely learn without being under the threat of being scammed. 

## Background
People have been using YouTube to learn multiple skills and with the rise in the popularity of Bitcoin, people are using YouTube to learn Cryptocurrency. As the number of viewers increase, this becomes an attractive platform for scammers to scam people into forwarding them bitcoins with a promise of a reward. This project in collaboration with professors **Gianluca Stringhini** and **Osama Alshaykh** aims at exposing these fradulent videos.  YouTube viewers *"had lost **$24 million** in bitcoin and related scams in the first six months of 2020" [4]* and therefore it is an important area that needs to be rectified.

## Other Application
Given the large usage of YouTube and the high traffic volumes that it experiences, although this project only focuses on a very specific topic- identifying cryptocurreny scams on YouTube it has a large application. If successful, this could be used to identify scams on other platforms including Twitter and Facebook. As an extension this could also be used to flag videos that contain malicious data that astray the users.

## Literature Review


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
