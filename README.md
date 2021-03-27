# ninja_gold_project
A mini-game learning how to use session and redirect 

Assignment: Ninja Gold
Practice passing data to a template
Practice using forms
Practice using Django session


You're going to create a mini-game that helps a ninja make some money! When you start the game, your ninja should have 0 gold. The ninja can go to different places (farm, cave, house, casino) and earn different amounts of gold. In the case of a casino, your ninja can earn or lose up to 50 gold. Your job is to create a web app that allows this ninja to earn gold and to display past activities of this ninja.

Guidelines
Refer to the wireframe below.
Have the four forms appear when the user goes to http://localhost:8000
Use a hidden input tag in each form to pass the relevant location to the server
Have /process-money determine how much gold the user should have
For now, save the activity log in session

(image of wireframe)

Create a new project/app  
Have the root route render the main Ninja Gold page  
NINJA BONUS: Refactor your code so the location is being passed in the URL rather than via a form  
SENSEI BONUS: Have the user specify the win conditions before starting, and then implement them in the game (# of moves, goal for gold)  
Have the "/process-money" POST route increase/decrease the user's gold by an appropriate amount and redirect to the root route
