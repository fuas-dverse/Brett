Created at: 27-02-2024 @ 12:17

# Table of Contents
[Instagram Clone](#Instagram%20Clone)
[Ticket System](#Ticket%20System)
[Combined Idea](#Combined%20Idea)

# Instagram Clone
A social media platform kind of like Instagram, it would feature some basic social media stuff like: uploading posts, uploading images, having friend, likes, follows etc.

Challenges:
- Developing a social media platform (likes, friends etc.)
- Make it secure for everyone
- Handle some large amounts of data like images
- Make it fun to interact with and stand out from other platforms

Initial ideas:
- Login system                     (Security by Design)
- Host on the cloud             (Cloud Native)
- Cloud image storage        (Cloud Native)
- ‘Big’ user based                 (Scalable Architectures)
- Multiple environments      (DevOps)
- CI/CD pipelines                 (DevOps)

Link to group project:
- Agents could filter some posts based on their #'s.
- Follow the posts of a news channel or celebrity.

# Ticket System
A ticket system that has basic information about a certain events like festivals, it will feature stuff like: showing information about a festival, booking a festival etc.

Challenges:
	- Developing a platform that shows festival information
- Handle large amount of users at the same time
- Make a secure platform, especially when handling user data
- Making payments to book a ticket

Initial ideas:
- Login system                     (Security by Design)
- Securing user data            (Security by Design)
- Host on the cloud             (Cloud Native)
- ‘Big’ user based                 (Scalable Architectures)
- Multiple environments      (DevOps)
- CI/CD pipelines                 (DevOps)

Link to group project:
- Search though the data of available festivals
- Book a festival
- Add festival to calendar


# Combined Idea
For this idea, we create the social media platform that allows user to use it like a normal social media platform, but allows creators or celebrity's to host ticket events on the feed of users.

For example: when I follow Martin Garrix, he will be able to host an event that has a time lock on it. When the time lock expires users will be able to buy a ticket for the event. 

Challenges:
- Same as above combined

Initial Ideas:
- Same as above combined

Link to group project:
- Same as above combined


# Final Idea
Reno and I have decided to choose the Ticket System idea. But we had to scale it down a bit, because of the connection with the group project. In this final section we will take a look on how to scale down this project idea, so that it can be worked on in combination with the group project.

## Scaled down idea

### Techniques
- Next JS - Front-End (TS)
	- Next UI
	- Tailwind CSS
- Festival information bot - OpenAI Gpt-4
- Google Calendar agent - Google API / Auth0 ??
- Docker / Kubernetes
- Python - Backend
- NoSQL Database - Most likely MongoDB
- Blob Storage - Not Defined
- Cloud Hosting - Vercel
- Code Quality Checker (e.g., SonarCloud, SonarCube etc.)