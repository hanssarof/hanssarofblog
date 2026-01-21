---
title: 0 - From idea to prototype
date: 2024-09-18
---
## The start
Hi, my name is Hans, thank you for visiting this website! I am writing this blog to share my progress on the indie game I am working on - Desert Defender. My goal is to go through all the development steps and release the game on Steam. I am working with the Unreal Engine 5 and using both C++ and blueprints. I am not a professional programmer, nor a 3D artist: just a random but passionate guy trying his best at game develpment as a hobby while having a full time job and a social life.

I've been playing with the Unreal Engine for 3 or 4 years now, trying to understand how things work and learn how to make video games. When I started out, I made two big mistakes that a lot of beginners make and that cost me a lot of time. First, I started with a project that was far too big, and second I got stuck in tutorial hell. This project is my attempt to make things right this time.

## The idea
I don’t know exactly how my idea came to me, but I wanted to make a fun game, kind of a parody of zombie games, in a cartoon style with a western vibe. Yes, why not? I wanted a main character who feels a bit cozy, either a fox or a coyote, and who could be a bit like Rocket in Guardians of the Galaxy: a funy animal but with humanoid capabilities. I also decided he would fight snakes — what better way to replace zombies?

So to sum up, my new project is:
- A solo game
- A third-person shooter because I prefer that camera angle
- Few different weapons, but no more than 5, with a simple system to use them
- A zombie-style mode with a point to defend and waves of enemies to fight
- 3 or 4 enemy types at most
- A western desert–style environment
- 3 to 5 levels
- 3 to 5 bosses maximum (one per level)
- Maybe a few abilities, bonuses, and boosts
- A simple system with two or three pickups
- A health bar for the player
- A health bar for the base to defend
- A score based on the number of enemies killed

My new project is not:
- A multiplayer game (for now)
- No dozens of weapons, and no progression system or skill tree
- No multiple characters either, just one coyote (for now too)
- No shields
- No complicated system of points, combos, or anything like that

## The prototype
To quickly test whether my idea could be fun, engaging, and above all doable, I started by making a prototype. To avoid wasting time, I reduced the number of features even more, focusing on the core idea:
- A solo game
- A third-person shooter because I prefer that camera angle
- ~~Few different weapons, but no more than 5, with a simple system to use them~~ -> just projectiles fired from the player for now
- ~~A zombie-style mode with a point to defend and waves of enemies to fight~~ -> just basic ennemies, no waves in the prototype
- ~~3 or 4 enemy types at most~~ -> just basic ennemies, no waves in the prototype
- ~~Three to five levels maximum~~ -> a very basic level for test purposes

With this in mind, I spend two to three days making this prototype. I made very basic assets of a fox and a snake in Blender. Then I imported them into Unreal and, using blueprints, I quickly got a third person character and functional enemies.

<p style="text-align:center;"><img src="/images/Pasted%20image%2020260121215510.png" alt="Image Description"></p>
<p style="text-align:center; font-style:italic;">My basic assets, such a fine piece of art</p>

I also added the following elements:
- Projectiles (fired from the center of the character) that destroy the snakes
- A base for the enemies to attack
- Two types of enemies with some snakes following the player and others going straight to the base
- And finally, a top left widget that counts snakes killed and a crosshair in the middle of the screen

<p style="text-align:center;"><img src="/images/2024-09-28_19-14-47-ezgif.com-crop.gif" alt="Image Description"></p><p style="text-align:center; font-style:italic;">The result: a playable prototype</p>
