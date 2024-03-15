Created at: 15-03-2024 @ 09:07 by Reno Muijsenberg & Brett Mulder

# Context
For our sixth semester at Fontys we are creating a group project call 'Collaborating Bots'. The goal of this application is to make a platform where users can specify a task they want to achieve, this task is then executed by a number of different agents.

For example, a user asks the following prompt:
`I want to book a festival in the summer of 2024 in the Netherlands`

This prompt needs to be handled by different agents. For example:
- First I have a agent that will look up festivals at the given date.
- After that another agent will give you the link to the ticket shop.
- And in the end, a Google Calendar appointment can be created by the Google Calendar agent.

Our individual project is closely linked together with our group project, as creating one (or multiple) of those agents will be our individual project. We decided to create some agents regarding the example given (booking a festival).

# Problem / Opportunity
For this project, the most obvious problem is on how to create a network that allows these agents to collaborate with each other in a trustworthy manner.

This allows for multiple opportunities, like setting up and creating a stable network connection between these agents or making agents curious to listen to available work.

# Expected Delivery
- **Functional Agent:** A fully functional software agent that interacts with the "Collaborating Bots" platform and fulfills a specific task related to festival booking (e.g., festival searching, ticket purchase link retrieval, calendar event creation).

# Main Question
How can we design and implement a functional and reliable agent(s) for the "Collaborating Bots" platform that contributes to booking festival tickets?

## Sub-questions
1. What APIs or data sources are available for the agent to utilize (e.g., festival databases, ticketing platforms, Google Calendar API)?
2. How can the agent access real-time festival ticket availability data?
3. How can we ensure the agent performs efficiently and handles potential errors gracefully?
4. How will the performance of the agent be monitored to ensure its functionality and reliability?
5. How can the agent be easily updated to adapt to changes in festival ticketing platforms?

## Research Strategies / Methods

<div style="overflow: auto">
	<div style="width: 60%; float: left">
		<i>Sub-question 1:</i>
			<ul>
				<li><b>Library:</b> Available product analysis, Community research, Literature study</li>
				<li><b>Field:</b> Stakeholder analysis, Problem analysis</li>
				<li><b>Workshop:</b> Prototype, Code review</li>
				<li><b>Lab:</b>Unit testing, Data analytics</li>
			</ul>
	</div>
	<div style="width: 30%; float: right">
		<img src="https://ictresearchmethods.nl/img/patterns/choose-fitting-technology.webp" style="width: 200px; height: 200px;">
	</div>
</div>

<div style="overflow: auto">
	<div style="width: 60%; float: right">
		<i>Sub-question 2:</i>
			<ul>
				<li><b>Library:</b> Available product analysis, Community research, Literature study</li>
				<li><b>Workshop:</b> Prototype, Code review</li>
				<li><b>Showroom:</b> Static code analysis, Product review</li>
			</ul>
	</div>
	<div style="width: 30%; float: left">
		<img src="https://ictresearchmethods.nl/img/patterns/realise-as-an-expert.webp" style="width: 200px; height: 200px;">
	</div>
</div>

<div style="overflow: auto">
	<div style="width: 60%; float: left">
		<i>Sub-question 3:</i>
			<ul>
				<li><b>Workshop:</b> Prototype, Root cause analysis</li>
				<li><b>Lab:</b> System test, Unit test</li>
				<li><b>Showroom:</b> Static code analysis, Guideline conformity analysis</li>
			</ul>
	</div>
	<div style="width: 30%; float: right">
		<img src="https://ictresearchmethods.nl/img/patterns/validate.webp" style="width: 200px; height: 200px;">
	</div>
</div>

<div style="overflow: auto">
	<div style="width: 60%; float: right">
		<i>Sub-question 4:</i>
			<ul>
				<li><b>Workshop:</b> Prototype</li>
				<li><b>Lab:</b> System test, Unit test</li>
				<li><b>Showroom:</b> Static code analysis, Product review</li>
			</ul>
	</div>
	<div style="width: 30%; float: left">
		<img src="https://ictresearchmethods.nl/img/patterns/validate.webp" style="width: 200px; height: 200px;">
	</div>
</div>

<div style="overflow: auto">
	<div style="width: 60%; float: left">
		<i>Sub-question 5:</i>
			<ul>
				<li><b>Library:</b> Best good and bad practices, Community research</li>
				<li><b>Workshop:</b> Brainstorm, Gap analysis</li>
				<li><b>Showroom:</b> Peer review, Product review</li>
			</ul>
	</div>
	<div style="width: 30%; float: right">
		<img src="https://ictresearchmethods.nl/img/patterns/realise-as-an-expert.webp" style="width: 200px; height: 200px;">
	</div>
</div>


# Estimate Time Required
- Research: 2 weeks
- Prototype: 4 weeks

*Total Estimated Time:* 6 weeks