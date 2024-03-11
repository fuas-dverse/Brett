# Architecture Idea - Startup Business

For this example I have created a scenario for a business startup.

When starting the project, there needs to be a some sort of main AI to handle the leading to other AI / world services. Or maybe it is just going to be hardcoded for now.

Then the user can make a input to start the process. Based on the question a bot is getting fired up to handle the
request. Let's say we want to achieve the following things:

1. A business name
2. A business slogan that triggers the users attention
3. A business description that tells more about the company
4. A logo bases on the name, logo, description and the users preferences
5. A video about what the company does

Let's start with the following question the user could ask:

_<u>I want to create a new business, can you help me with this?</u>_

From now on, the main service / bot spins up the first bot, and we can start the process:

1. The AI from openAI gets spinned up, and starts you asking question about what the company is like:

_<u>Hi, I can help you with starting a new company. Let's start with some questions: ...</u>_

2. Now the AI is generating the text points first, so a first suggestion for the name, slogan and description is given
   by the AI.
3. You as a user can choose if you accept this or want to change anything. If you want to change anything, the AI should
   start asking more questions for a better response the next time.
4. When agreed, the AI for text is getting turned off.
5. When the AI for text gets turned off, the Logo generator gets turned on
6. The AI for logos now knows about your company name, slogan and description. But it still needs to know about the
   style of the logo. So it should start asking questions about this.

_<u>Hi, now that the name, slogan and description for your company is created. We can start with your logo. Can you
provide
me a small but detailed description about the style of your logo? Think about colors, outlined, clean ...</u>_

7. Now your logos gets created, and here you can also make the choise to agree of change anything.
8. When agreed, the AI for logos gets turned off
9. The AI for the video gets turned on
10. Now this video AI, knows about all your previous info (name, slogan, description and logo). It should start ask
    questions about your video for what your company stands for.

_<u>Hi, now I also know your name. Let's create a stunning introduction video for your company. Can you provide me a
short but detailed description about how your video should look like?</u>_

11. Now video gets created, and here you can also make the choise to agree of change anything.
12. When agreed, the AI for video gets turned off and at this point a ZIP folder gets created with a pdf, logos and video.
13. You can download this, and from here all services gets turned off.
